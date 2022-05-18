import datetime
import os
from os.path import basename
import shutil
from io import BytesIO
from zipfile import ZipFile
from dotenv import load_dotenv
import pandas as pd
from sqlalchemy import create_engine
from flask import Response, request, send_file, make_response
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity, current_user
from flasgger_marshmallow import swagger_decorator
from app.schemas import (
    ProjectSchema,
    ProjectUuidPathSchema,
    ProjectReturnSchema,
    ProjectListSchema,
    CreateProjectSuccessSchema,
    MessageSchema,
)
from app.models import (
    Project,
    JobInfo,
    JobType,
    Equipment,
    Client,
    Pad,
    LocationInfo,
    CountyName,
    BasinName,
    State,
    CustomerFieldRep,
    Crew,
    ProjectCrew,
    Well,
    User,
    CloudSyncTableList,
    CloudSyncTableLog,
)

from marshmallow.exceptions import ValidationError

load_dotenv()

DATABASE_URL = os.environ.get("DATABASE_URL")
CLOUD_DB_URL = os.environ.get("CLOUD_DB_URL")


class ProjectGeneral(Resource):
    @jwt_required()
    @swagger_decorator(
        response_schema={200: ProjectReturnSchema, 404: MessageSchema},
        path_schema=ProjectUuidPathSchema,
        tag="Project",
    )
    def get(self, project_uuid):
        """Get project data"""
        project = Project.query.filter(Project.project_uuid == project_uuid).first()
        projectSync = CloudSyncTableLog.query.filter(
            CloudSyncTableLog.table_name == "project"
        ).first()
        if not project or project.user_id != current_user.id:
            msg = f"Project with uuid: {project_uuid} not found"
            return {"msg": msg}, 404

        wells = []
        for well in project.pad.wells:
            wells.append(
                {
                    "uuid": well.well_uuid,
                    "well_name": well.well_name,
                    "num_stages": well.num_stages,
                }
            )

        if projectSync:
            last_sync_date = datetime.timestamp(projectSync.synch_date)
        else:
            last_sync_date = 0

        return {
            "status": 200,
            "message": "Project details",
            "data": {
                "project": {
                    "uuid": project.project_uuid,
                    "project_name": project.project_name,
                    "wells": wells,
                },
                "last_sync_date": last_sync_date,
            },
        }

    @jwt_required()
    @swagger_decorator(
        response_schema={200: MessageSchema, 404: MessageSchema},
        path_schema=ProjectUuidPathSchema,
        tag="Project",
    )
    def delete(self, project_uuid):
        """Delete project"""
        project = Project.query.filter(Project.project_uuid == project_uuid).first()
        if not project or project.user_id != current_user.id:
            msg = f"Project with uuid: {project_uuid} not found"
            return {"msg": msg}, 404

        project.delete()
        return {"msg": "Project deleted"}, 200


class ProjectCreate(Resource):
    @jwt_required()
    @swagger_decorator(
        json_schema=ProjectSchema,
        response_schema={200: CreateProjectSuccessSchema},
        tag="Project",
    )
    def post(self):
        """Create project"""
        user_id = get_jwt_identity()
        req = request.json_schema

        project_name = req["projectValues"]["project_name"]

        project = Project(
            project_name=project_name,
            client_id=0,
            user_id=user_id,
        )

        project.save()

        # Pad data
        pad_data = req["padInfoValues"]

        if pad_data.get("customer_email", "") == "":
            pad_data["customer_email"] = None

        customer_field_rep = CustomerFieldRep(
            name=pad_data["customer_name"],
            email=pad_data["customer_email"],
            customer_field_rep_num=pad_data["rep_contact_number"],
        )
        customer_field_rep.save()

        client = Client(
            client_name=pad_data["customer_name"],
            customer_field_rep_id=customer_field_rep.id,
            project_id=project.id,
            operator_name=pad_data["operator_name"],
            service_company_name=pad_data["service_company_name"],
            wireline_company=pad_data["wireline_company"],
        )

        client.save()
        project.client_id = client.id
        project.save()

        pad = Pad(
            project_id=project.id,
            pad_name=pad_data["pad_name"],
            number_of_wells=len(req["wellInfoValues"]),
        )

        pad.save()

        # Job data
        job_data = req["jobInfoValues"]
        job_type = JobType.query.filter(JobType.value == job_data["job_type"]).first()
        if not job_type:
            job_type = JobType(value=job_data["job_type"])
            job_type.save()

        if job_data.get("job_end_date", "") == "":
            job_data["job_end_date"] = None
        else:
            job_data["job_end_date"] = datetime.fromtimestamp(
                job_data["job_end_date"] // 1000
            )

        job = JobInfo(
            job_name=job_data["job_name"],
            job_type_id=job_type.id,
            job_id=job_data["job_id"],
            afe_id=job_data["afe_id"],
            job_start_date=datetime.fromtimestamp(job_data["job_start_date"] // 1000),
            job_end_date=job_data["job_end_date"],
            project_id=project.id,
        )

        job.save()

        # crew entity
        crew_data_list = req["crewInfoValues"]
        for crew_data in crew_data_list:
            crew = Crew(
                name=crew_data["name"], shift=crew_data["shift"], role=crew_data["role"]
            )

            crew.save()

            ProjectCrew(project_id=project.id, crew_id=crew.id).save()

        # well entity
        well_data_list = req["wellInfoValues"]

        for i, well_info in enumerate(well_data_list):
            # equipment
            equip = req["equipmentValues"][i]
            equipment = Equipment(
                trailer_id=equip["trailers_id"],
                powerpack_id=equip["powerpack_id"],
                source_id=equip["source_id"],
                accumulator_id=equip["accumulator_id"],
                hydrophones_id=equip["hydrophones_id"],
                hotspot_id=equip["hotspot_id"],
                transducer_id=equip["transducer_id"],
            )
            equipment.save()

            casing, liner, liner_sec = {}, {}, {}
            for well_values in req["wellVolumeValues"][i]:
                if well_values["type"] == "casing":
                    casing = well_values
                elif well_values["type"] == "liner":
                    liner = well_values
                elif well_values["type"] == "liner_sec":
                    liner_sec = well_values
                else:
                    raise ValidationError(
                        message=f'unsupported well value type: {well_values["type"]}'
                    )

            for values_type_name, values_type in {
                "casing": casing,
                "liner": liner,
                "liner_sec": liner_sec,
            }.items():
                if not values_type:
                    raise ValidationError(
                        message=f"Missing well type: {values_type_name}"
                    )

            wellEstim = req["wellVolumeEstimationsValues"][i]

            well = Well(
                equipment_id=equipment.id,
                pad_id=pad.id,
                well_name=well_info["well_name"],
                well_api=well_info["well_api"],
                formation=well_info["formation"],
                surface_latitude=well_info["surface_latitude"],
                surface_longitude=well_info["surface_longitude"],
                casing_od=casing["od"],
                casing_wt=casing["wt"],
                casing_id=casing["id"],
                casing_depth_md=casing["depth_md"],
                casing_tol=casing["tol"],
                liner1_od=liner["od"],
                liner1_wt=liner["wt"],
                liner1_id=liner["id"],
                liner1_depth_md=liner["depth_md"],
                liner1_tol=liner["tol"],
                liner2_od=liner_sec["od"],
                liner2_wt=liner_sec["wt"],
                liner2_id=liner_sec["id"],
                liner2_depth_md=liner_sec["depth_md"],
                liner2_tol=liner_sec["tol"],
                estimated_surface_vol=wellEstim["surface_vol"],
                estimated_bbls=wellEstim["bbls"],
                estimated_gallons=wellEstim["gallons"],
                num_stages=well_info["num_stages"],
            )
            well.save()

        # location entity
        county_name = CountyName.query.filter(
            CountyName.county_name == job_data["county_name"]
        ).first()
        if not county_name:
            county_name = CountyName(county_name=job_data["county_name"])
            county_name.save()

        basin_name = BasinName.query.filter(
            BasinName.basin_name == job_data["basin_name"]
        ).first()
        if not basin_name:
            basin_name = BasinName(basin_name=job_data["basin_name"])
            basin_name.save()

        state = State.query.filter(State.value == job_data["state"]).first()
        if not state:
            state = State(value=job_data["state"])
            state.save()

        LocationInfo(
            county_name_id=county_name.id,
            basin_name_id=basin_name.id,
            state_id=state.id,
            job_info_id=job.id,
        ).save()

        return {
            "status": 200,
            "message": "Project created successfully!",
            "data": {
                "project": {
                    "uuid": project.project_uuid,
                }
            },
        }


class ProjectListGet(Resource):
    @jwt_required()
    @swagger_decorator(
        response_schema={200: ProjectListSchema, 404: MessageSchema},
        tag="Project",
    )
    def get(self):
        """Get project list"""
        user_id = get_jwt_identity()
        user = User.query.filter(User.id == user_id).first()
        if not user:
            return {"msg": "Invalid user"}

        user_projects = Project.query.filter(Project.user_id == user_id).all()
        projects = []
        for project in user_projects:
            projects.append(
                {
                    "uuid": project.project_uuid,
                    "project_name": project.project_name,
                    "job_name": project.job_info.job_name,
                    "job_id": project.job_info.job_id,
                    "created_date": project.created_at.strftime("%m/%d/%Y"),
                    "created_by": user.username,
                    "created_time": project.created_at.strftime("%H:%M:%S"),
                }
            )

        return {"projects": projects}, 200


class ProjectDownload(Resource):
    @jwt_required()
    @swagger_decorator(
        response_schema={404: MessageSchema},
        path_schema=ProjectUuidPathSchema,
        tag="Project",
    )
    def exportCSV(cls, conn, query, id, path):
        frame = pd.read_sql_query(query, conn, params={id})
        frame.to_csv(path, index=False)

    def generateZIP(cls, dir):
        memory_file = BytesIO()
        # create a ZipFile object
        with ZipFile(memory_file, "w") as zipObj:
            # Iterate over all the files in directory
            for folderName, subfolders, filenames in os.walk(dir):
                for filename in filenames:
                    # create complete filepath of file in directory
                    filePath = os.path.join(folderName, filename)
                    # Add file to zip
                    zipObj.write(filePath, basename(filePath))
        memory_file.seek(0)
        return memory_file

    def get(self, project_uuid):
        # Get table list
        tableList = CloudSyncTableList.query.filter(
            (CloudSyncTableList.sql_string != None)
        ).all()

        if tableList:
            # Get default system path
            mydir = os.path.join(
                os.getcwd(),
                project_uuid + "_" + datetime.datetime.now().strftime("%Y_%m_%d_%H_%M"),
            )
            os.mkdir(mydir)

            # Connect to local DB
            localEngine = create_engine(DATABASE_URL, pool_recycle=3600)
            localConn = localEngine.connect()
            # Export db data into csv
            for table in tableList:
                path = os.path.join(mydir, table.table_name + ".csv")
                if table.sql_string != "":
                    self.exportCSV(localConn, table.sql_string, project_uuid, path)
            # generate zip from the exported csv directory
            memory_file = self.generateZIP(mydir)
            # Remove synced directory
            if os.path.exists(mydir):
                shutil.rmtree(mydir)

            response = Response(memory_file, mimetype="application/zip")
            response.headers["Content-Disposition"] = "attachment; filename={}".format(
                "seismos.zip"
            )
            return response
        else:
            return {"msg": "no active table found"}, 401
