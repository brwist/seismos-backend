from datetime import datetime
from flask import request
from flask_jwt_extended import jwt_required, get_jwt_identity, current_user
from flask_restful import Resource
from flasgger_marshmallow import swagger_decorator
from app.models import Well, FieldNotes

from app.schemas import (
    MessageSchema,
    DailyLogCreateSchema,
    DailyLogCreateResponseSchema,
    DailyLogResponseSchema,
    WellPathUuidSchema,
)


class DailyLogResource(Resource):
    @jwt_required()
    @swagger_decorator(
        response_schema={200: DailyLogResponseSchema, 401: MessageSchema},
        path_schema=WellPathUuidSchema,
        tag="Daily log",
    )
    def get(self, well_uuid):
        """ Get dealy log """

        well = Well.query.filter(Well.well_uuid == well_uuid).first()
        if not well:
            return {"msg": f"Well with uuid {well_uuid} not found"}, 401

        logs = well.get_logs()

        resp = {
            "message": "Daily log details",
            "logs": logs
        }

        return resp, 200

    @jwt_required()
    @swagger_decorator(
        path_schema=WellPathUuidSchema,
        json_schema=DailyLogCreateSchema,
        response_schema={201: DailyLogCreateResponseSchema, 401: MessageSchema},
        tag="Daily log",
    )
    def post(self, well_uuid):
        """Create daily log"""
        req = request.json_schema
        well = Well.query.filter(Well.well_uuid == well_uuid).first()

        if not well or well.pad.project.user_id != get_jwt_identity():
            return {"msg": "Well not found"}, 401

        if "logs" not in req:
            return {"msg": "Logs data are corrupt"}, 401

        for log in req["logs"]:
            timestamp = log["date"] // 1000
            timestamp = datetime.fromtimestamp(timestamp)
            FieldNotes(
                comment_timestamp=timestamp,
                well_id=well.id,
                comment_content=log["description"],
                comment_by=current_user.username
            ).save()

        return {
            "status": 201,
            "message": "Daily logs created",
        }, 201
