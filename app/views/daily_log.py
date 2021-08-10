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
    DailyLogResponseSchema,
    WellPathIdSchema,
)


class DailyLogResource(Resource):
    @jwt_required()
    @swagger_decorator(
        response_schema={200: DailyLogResponseSchema, 401: ErrorSchema},
        path_schema=WellPathIdSchema,
        tag="Daily log",
    )
    def get(self, well_id):
        """ Get dealy log """

        well = Well.query.filter(Well.id == well_id).first()
        if not well:
            return {"msg": f"Well with id {well_id} not found"}, 401

        logs = well.get_logs()

        resp = {
            "message": "Daily log details",
            "logs": logs
        }

        return resp, 200


class DailyLogCreateResource(Resource):
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
            timestamp = log["date"] // 1000
            log["date"] = datetime.fromtimestamp(timestamp)
            log["well_id"] = req["well_id"]
            DailyLog(**log).save()

        return {
            "status": 201,
            "message": "Daily logs created",
        }, 201
