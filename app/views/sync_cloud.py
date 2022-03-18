import csv
import datetime
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
import pandas as pd
from flask_jwt_extended import jwt_required
from flask_restful import Resource
from flasgger_marshmallow import swagger_decorator
from app.models import Project, Well, Stage
from app.schemas import MessageSchema, SyncCloudRequestScehma

load_dotenv()

DATABASE_URL = os.environ.get("DATABASE_URL")
TEST_URL = os.environ.get("TEST_DB_URL")
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

    def importCSVToStore(cls, path, tableName, cursor):
        with open(path, "r") as f:
            reader = csv.reader(f)
            columns = next(reader)
            query = "insert into " + tableName + "({0}) values ({1})"
            query = query.format(",".join(columns), ("%s," * (len(columns) - 1)) + "%s")
            for data in reader:
                print("query: ", query)
                print("values: ", data)
                cursor.execute(query, data)
                myresult = cursor.fetchall()
                print("myresult: ", myresult)

    def get(self, project_uuid):
        # Connect to managed store
        sqlEngine = create_engine(CLOUD_DB_URL, pool_recycle=3600)
        connection = sqlEngine.raw_connection()
        cursor = connection.cursor()

        cursor.execute("select * from project where project_uuid=%s", [project_uuid])
        # cursor.execute("Show tables;")
        # myresult = cursor.fetchall()
        # print(myresult)

        # cursor.execute("show columns from project;")
        # myresult = cursor.fetchall()
        # print(myresult)

        # cursor.execute("select * from well;")
        # myresult = cursor.fetchall()
        # print(myresult)

        if len(cursor.fetchall()) == 1:
            print("store has already synced")
            cursor.execute("delete from project where project_uuid=%s", [project_uuid])
            print("delete row is succeed")
            return {"msg": "project is already synced"}, 401
        else:
            print("need to sync")
            # Get project list
            project = Project.query.filter(
                (Project.project_uuid == project_uuid)
            ).first()

            if project:
                # Get default system path
                mydir = os.path.join(
                    os.getcwd(),
                    project_uuid
                    + "_"
                    + datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S"),
                )
                os.makedirs(mydir)

                tableNames = ["project", "client", "pad", "job_info", "project_crew"]
                queries = [
                    "SELECT * FROM project WHERE project_uuid=%(id)s",
                    "SELECT * FROM client WHERE id=%(id)s",
                    "SELECT * FROM pad WHERE project_id=%(id)s",
                    "SELECT * FROM job_info WHERE project_id=%(id)s",
                    "SELECT * FROM project_crew WHERE project_id=%(id)s",
                ]
                # Connect to local DB
                localEngine = create_engine(DATABASE_URL, pool_recycle=3600)
                localConn = localEngine.connect()

                for idx, name in enumerate(tableNames):
                    path = os.path.join(mydir, name + ".csv")
                    if idx == 0:
                        id = project_uuid
                    elif idx == 1:
                        id = project.client_id
                    else:
                        id = project.id
                    # export
                    self.exportCSV(localConn, queries[idx], id, path)
                    # import
                    self.importCSVToStore(path, name, cursor)
                # Save logs and export table list

                # Remove synced directory
                # if os.path.exists(mydir):
                #     os.remove(mydir)

                return {"msg": "sync successed"}, 200
            else:
                return {"msg": "project not found"}, 401
