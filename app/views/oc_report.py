from flask_jwt_extended import jwt_required
from flask_restful import Resource
from flasgger_marshmallow import swagger_decorator

from app.schemas import (
    SuccessSchema,
    ErrorSchema,
    OCReportSchema,
)


class QCReport(Resource):
    @jwt_required()
    @swagger_decorator(
        response_schema={200: OCReportSchema},
        tag="OC Report",
    )
    def get(self):
        """ Get OC raport data"""
        return {"report": "OC report data"}

    @jwt_required()
    @swagger_decorator(
        json_schema=OCReportSchema,
        response_schema={200: SuccessSchema, 401: ErrorSchema},
        tag="OC Report",
    )
    def post(self):
        """ Approve OC report """
        return {"msg": "Report approve"}


class QCReportExport(Resource):
    @jwt_required()
    @swagger_decorator(
        json_schema=OCReportSchema,
        response_schema={200: SuccessSchema, 401: ErrorSchema},
        tag="OC Report",
    )
    def post(self):
        """ Export OC """
        return {"msg": "OC export"}
