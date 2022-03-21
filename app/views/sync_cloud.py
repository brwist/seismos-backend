import csv
import datetime
import os
import shutil
from dotenv import load_dotenv
from sqlalchemy import create_engine
import pandas as pd
from flask_jwt_extended import jwt_required
from flask_restful import Resource
from flasgger_marshmallow import swagger_decorator
from app.models import Project, LocationInfo, Well
from app.schemas import MessageSchema, SyncCloudRequestScehma

load_dotenv()

DATABASE_URL = os.environ.get("DATABASE_URL")
CLOUD_DB_URL = os.environ.get("CLOUD_DB_URL")


class SyncCloud(Resource):
    @jwt_required()
    @swagger_decorator(
        response_schema={401: MessageSchema},
        path_schema=SyncCloudRequestScehma,
        tag="Sync Cloud",
    )
    def exportCSV(cls, conn, query, id, path):
        frame = pd.read_sql_query(query, conn, params={"id": id})
        frame.to_csv(path, index=False)

    def importCSVToStore(cls, path, tableName, connection):
        with open(path, "r") as f:
            reader = csv.reader(f)
            columns = next(reader)
            query = "insert into " + tableName + "({0}) values ({1})"
            query = query.format(",".join(columns), ("%s," * (len(columns) - 1)) + "%s")
            for data in reader:
                # print("query: ", query)
                # print("values: ", data)
                result = connection.execute(query, data)
                print("query result: ", result.rowcount)

    def get(self, project_uuid):
        # Connect to managed store
        sqlEngine = create_engine(CLOUD_DB_URL, pool_recycle=3600)
        connection = sqlEngine.connect()

        result = connection.execute(
            "select * from project where project_uuid=%s", [project_uuid]
        )

        if result.rowcount > 0:
            print("store has already synced")
            return {"msg": "project is already synced"}, 401
        else:
            # Get project list
            project = Project.query.filter(
                (Project.project_uuid == project_uuid)
            ).first()
            location_info = LocationInfo.query.filter(
                (LocationInfo.job_info_id == project.job_info.id)
            ).first()
            well = Well.query.filter((Well.pad_id == project.pad.id)).first()
            # stage = Stage.query.filter((Stage.well_id == well.id)).first()

            if project:
                # Get default system path
                mydir = os.path.join(
                    os.getcwd(),
                    project_uuid
                    + "_"
                    + datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S"),
                )
                os.mkdir(mydir)
                tableNames = [
                    "project",
                    "client",
                    "customer_field_rep",
                    "pad",
                    "job_info",
                    "job_type",
                    "location_info",
                    "county_name",
                    "state",
                    "basin_name",
                    "project_crew",
                    "project_user",
                    "crew",
                    "user",
                    "well",
                    "equipment",
                    "field_notes",
                    "default_val",
                    "default_param_val",
                    "default_advance_val",
                    # "stage",
                    # "proppant",
                    # "perforation",
                    # "chem_fluids",
                    # "stage_avg",
                    # "ff_processing_result",
                    # "nf_processing_result",
                    # "active_data",
                    # "formation_fluid_injection",
                ]
                queries = [
                    "SELECT * FROM project WHERE project_uuid=%(id)s",
                    "SELECT * FROM client WHERE id=%(id)s",
                    "SELECT * FROM customer_field_rep WHERE id=%(id)s",
                    "SELECT * FROM pad WHERE project_id=%(id)s",
                    "SELECT * FROM job_info WHERE project_id=%(id)s",
                    "SELECT * FROM job_type WHERE id=%(id)s",
                    "SELECT * FROM location_info WHERE job_info_id=%(id)s",
                    "SELECT * FROM county_name WHERE id=%(id)s",
                    "SELECT * FROM state WHERE id=%(id)s",
                    "SELECT * FROM basin_name WHERE id=%(id)s",
                    "SELECT * FROM project_crew WHERE project_id=%(id)s",
                    "SELECT * FROM project_user WHERE project_id=%(id)s",
                    "SELECT * FROM crew WHERE id=%(id)s",
                    "SELECT * FROM user WHERE id=%(id)s",
                    "SELECT * FROM well WHERE pad_id=%(id)s",
                    "SELECT * FROM equipment WHERE id=%(id)s",
                    "SELECT * FROM field_notes WHERE well_id=%(id)s",
                    "SELECT * FROM default_val WHERE well_id=%(id)s",
                    "SELECT * FROM default_param_val WHERE well_id=%(id)s",
                    "SELECT * FROM default_advance_val WHERE well_id=%(id)s",
                    # "SELECT * FROM stage WHERE well_id=%(id)s",
                    # "SELECT * FROM proppant WHERE stage_id=%(id)s",
                    # "SELECT * FROM perforation WHERE stage_id=%(id)s",
                    # "SELECT * FROM chem_fluids WHERE stage_id=%(id)s",
                    # "SELECT * FROM stage_avg WHERE stage_id=%(id)s",
                    # "SELECT * FROM ff_processing_result WHERE stage_id=%(id)s",
                    # "SELECT * FROM nf_processing_result WHERE stage_id=%(id)s",
                    # "SELECT * FROM active_data WHERE stage_id=%(id)s",
                    # "SELECT * FROM formation_fluid_injection WHERE chem_fluid_id=%(id)s",
                ]
                ids = [
                    project_uuid,
                    project.client_id,
                    project.client.customer_field_rep_id,
                    project.id,
                    project.id,
                    project.job_info.job_type_id,
                    project.job_info.id,
                    location_info.county_name_id,
                    location_info.state_id,
                    location_info.basin_name_id,
                    project.id,
                    project.id,
                    project.project_crew.crew_id,
                    project.user_id,
                    project.pad.id,
                    well.equipment_id,
                    well.id,
                    well.id,
                    well.id,
                    well.id,
                    # well.id,
                    # stage.id,
                    # stage.id,
                    # stage.id,
                    # stage.id,
                    # stage.id,
                    # stage.id,
                    # stage.id,
                    # stage.chem_fluids.id,
                ]
                # Connect to local DB
                localEngine = create_engine(DATABASE_URL, pool_recycle=3600)
                localConn = localEngine.connect()

                for idx, name in enumerate(tableNames):
                    path = os.path.join(mydir, name + ".csv")
                    # export
                    self.exportCSV(localConn, queries[idx], ids[idx], path)
                    # import
                    self.importCSVToStore(path, name, connection)

                # Remove synced directory
                if os.path.exists(mydir):
                    shutil.rmtree(mydir)

                return {"msg": "sync successed"}, 200
            else:
                return {"msg": "project not found"}, 401
