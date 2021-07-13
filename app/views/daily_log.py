from flask import request
from flask_jwt_extended import jwt_required
from flask_restful import Resource
from flasgger_marshmallow import swagger_decorator

from app.schemas import (
    SuccessSchema,
    ErrorSchema,
    DailyLogSchema,
)


class DailyLog(Resource):
    @jwt_required()
    @swagger_decorator(
        response_schema={200: DailyLogSchema},
        tag="Daily log",
    )
    def get(self):
        """ Get daily log """
        return {"log": "This is log..."}

    @jwt_required()
    @swagger_decorator(
        json_schema=DailyLogSchema,
        response_schema={200: SuccessSchema, 401: ErrorSchema},
        tag="Daily log",
    )
    def post(self):
        """ Create daily log """
        req = request.json_schema

        return {"msg": f"created {req['data']}"}
