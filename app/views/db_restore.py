import os
from flask_jwt_extended.view_decorators import jwt_required
from flask_jwt_extended import current_user
from flask_restful import Resource
from app.schemas import BackupIndexSchema, MessageSchema
from flasgger_marshmallow import swagger_decorator
from dotenv import load_dotenv
from worker_db_backup import make_db_restor


load_dotenv()

ADMINS_EMAILS = os.environ.get("ADMINS", "").strip().split(" ")


class DatabaseRestore(Resource):
    @jwt_required()
    @swagger_decorator(
        response_schema={200: MessageSchema, 403: MessageSchema},
        tag="Restore Database",
        path_schema=BackupIndexSchema,
    )
    def put(self, backup_index):
        """ Login user and return JWT token """
        if current_user.email not in ADMINS_EMAILS:
            return {"msg": "You are not admin"}, 403

        make_db_restor.delay(int(backup_index))
        return {"msg": f"Database backup from index : {backup_index} started"}, 200
