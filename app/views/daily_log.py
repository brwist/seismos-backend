from datetime import datetime
from flask import request
from flask_jwt_extended import jwt_required
from flask_restful import Resource
from flasgger_marshmallow import swagger_decorator
from app.models import DailyLog, Well

from app.schemas import (
    ErrorSchema,
    DailyLogCreateSchema,
    DailyLogCreateResponseSchema,
    DailyLogRequestSchema,
    DailyLogResponseSchema,
    WellPathIdSchema,
)


class DailyLogResource(Resource):
    @jwt_required()
    @swagger_decorator(
        response_schema={200: DailyLogResponseSchema},
        path_schema=WellPathIdSchema,
        tag="Daily log",
    )
    def get(self, well_id):
        """Get daily log"""

        return {
            "status": 200,
            "message": "Daily log details",
            "data": {
                "logs": [
                    {"date": 1112345, "time": "plug", "Description": "first_log"},
                    {"date": 1112345, "time": "plug", "Description": "second_log"},
                ]
            },
        }

    @jwt_required()
    @swagger_decorator(
        json_schema=DailyLogCreateSchema,
        response_schema={201: DailyLogCreateResponseSchema, 401: ErrorSchema},
        tag="Daily log",
    )
    def post(self):
        """Create daily log"""
        req = request.json_schema
        well = Well.query.filter(Well.id == req["well_id"]).first()
        if not well:
            return {"msg": "Well not found"}, 401

        for log in req["logs"]:
            log["date"] = datetime.fromtimestamp(log["date"])
            log["well_id"] = req["well_id"]
            DailyLog(**log).save()

        return {
            "status": 201,
            "message": "Daily logs created",
        }, 201
