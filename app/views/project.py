from datetime import datetime
from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity
from flasgger_marshmallow import swagger_decorator
from uuid import uuid4


from app.schemas import (
    ProjectSchema,
    ProjectIdPathSchema,
    CreateProjectSuccessSchema,
    ErrorSchema,
    ProjectReturnSchema,
)


from app.models import (
    Project,
    JobInfo,
    JobType,
    Equipment,
    Client,
    Pad,
    LocationInfo,
    CountryName,
    BasinName,
    State,
    CustomerFieldRep,
    Crew,
    ProjectCrew,
    Well,
    Formation,
)

from marshmallow.exceptions import ValidationError


class ProjectGet(Resource):
    @jwt_required()
    @swagger_decorator(
        response_schema={200: ProjectReturnSchema, 404: ErrorSchema},
        path_schema=ProjectIdPathSchema,
        tag="Project",
    )
    def get(self, project_id):
        """ Get project data"""
        project = Project.query.filter(Project.id == project_id).first()
        if not project:
            msg = f"Project with id: {project_id} not found"
            return {"msg": msg}, 404

        wells = []
        for well in project.pad.wells:
            wells.append({
                "id": well.id,
                "well_name": well.well_name,
                "num_stages": well.num_stages,
            })

        return {
            "status": 200,
            "message": "Project details",
            "data": {
                "project": {
                    "id": project.id,
                    "project_name": project.project_name,
                    "wells": wells
                }
            }
        }


class ProjectCreate(Resource):
    @jwt_required()
    @swagger_decorator(
        json_schema=ProjectSchema,
        response_schema={200: CreateProjectSuccessSchema},
        tag="Project",
    )
    def post(self):
        """ Create project """
        req = request.json_schema
        equip_req = req["equipmentValues"]
        equipment = Equipment(
            trailer_id=equip_req["trailers_id"],
            powerpack_id=equip_req["powerpack_id"],
            source_id=equip_req["source_id"],
            accumulator_id=equip_req["accumulator_id"],
            hydrophones_id=equip_req["hydrophones_id"],
            hotspot_id=equip_req["hotspot_id"],
            transducer_id=equip_req["transducer_id"],
        )
        equipment.save()

        project_name = req["projectValues"]["project_name"]
        project_uuid = req["projectValues"]["project_uuid"]

        project = Project(
            project_name=project_name,
            project_uuid=project_uuid,
            client_id=0,
            user_id=get_jwt_identity(),
            equipment_id=equipment.id
        )

        project.save()

        # Pad data
        pad_data = req["padInfoValues"]
        customer_field_rep = CustomerFieldRep(
            name=pad_data["customer_field_rep"],
            customer_field_rep_num=pad_data["rep_contact_number"]
        )

        customer_field_rep.save()

        client = Client(
            client_uuid=str(uuid4()),
            client_name=pad_data["client_name"],
            customer_field_rep_id=customer_field_rep.id,
            project_id=project.id,
            operator_name=pad_data["operator_name"],
            service_company_name=pad_data["service_company_name"],
            wireline_company=pad_data["wireline_company"],
            # TODO Why list? (Make clean up)
            password=req["clientInfoValues"][0]["password"],
            title=req["clientInfoValues"][0]["title"]
        )

        client.save()
        project.client_id = client.id
        project.save()

        pad = Pad(
            project_id=project.id,
            pad_name=pad_data["pad_name"],
            pad_uuid=pad_data["pad_uuid"],
            number_of_wells=len(req["wellInfoValues"])
        )

        pad.save()

        # Job data
        job_data = req["jobInfoValues"]
        job_type = JobType(value=job_data["job_type"])
        job_type.save()

        job = JobInfo(
            job_name=job_data["job_name"],
            job_type_id=job_type.id,
            job_id=job_data["job_id"],
            afe_id=job_data["afe_id"],
            job_start_date=datetime.fromtimestamp(job_data["job_start_date"]),
            job_end_date=datetime.fromtimestamp(job_data["job_end_date"]),
            project_id=project.id,
        )

        job.save()

        # crew entity
        crew_data_list = req["crewInfoValues"]
        for crew_data in crew_data_list:
            crew = Crew(
                name=crew_data["name"],
                phone_number=crew_data["phone_number"],
                role=crew_data["role"]
            )

            crew.save()

            ProjectCrew(project_id=project.id, crew_id=crew.id).save()

        # well entity
        well_data_list = req["wellInfoValues"]

        for i, well_info in enumerate(well_data_list):
            formation = Formation(value=well_info["formation"])
            formation.save()

            casing, linear, linear_sec = {}, {}, {}
            for well_values in req["wellVolumeValues"][i]:
                if well_values["type"] == "Casing":
                    casing = well_values
                elif well_values["type"] == "Linear1":
                    linear = well_values
                elif well_values["type"] == "Linear2":
                    linear_sec = well_values
                else:
                    raise ValidationError(
                        message=f'unsupported well value type: {well_values["type"]}'
                    )

            wellEstim = req["wellVolumeEstimationsValues"][i]

            well = Well(
                well_uuid=str(uuid4()),
                pad_id=pad.id,
                well_name=well_info["well_name"],
                well_api=well_info["well_api"],
                formation_id=formation.id,
                num_stages=well_info["num_stages"],

                lat=well_info["lat"],
                easting=well_info["easting"],
                northing=well_info["northing"],

                casing_od=casing["od"],
                casing_wt=casing["wt"],
                casing_id=casing["id"],
                casing_depth_md=casing["depth_md"],
                casing_tol=casing["tol"],

                liner1_od=linear["od"],
                liner1_wt=linear["wt"],
                liner1_id=linear["id"],
                liner1_depth_md=linear["depth_md"],
                liner1_tol=linear["tol"],

                liner2_od=linear_sec["od"],
                liner2_wt=linear_sec["wt"],
                liner2_id=linear_sec["id"],
                liner2_depth_md=linear_sec["depth_md"],
                liner2_tol=linear_sec["tol"],

                estimated_surface_vol=wellEstim["surface_vol"],
                estimated_bbls=wellEstim["bbls"],
                estimated_gallons=wellEstim["gallons"],
            )
            well.save()

        # location entity
        country_name = CountryName(county_name=job_data["country_name"])
        basin_name = BasinName(basin_name=job_data["basin_name"])
        state = State(value=job_data["state"])

        country_name.save()
        basin_name.save()
        state.save()

        LocationInfo(
            county_name_id=country_name.id,
            basin_name_id=basin_name.id,
            state_id=state.id,
            job_info_id=job.id,
        ).save()

        return {
            "status": 200,
            "message": "Project created successfully!",
            "data": {
                "project": {
                    "id": project.id,
                }
            }
        }
