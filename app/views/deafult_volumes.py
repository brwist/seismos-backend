from flask import request
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_restful import Resource
from flasgger_marshmallow import swagger_decorator

from app.models import Well
from app.schemas import (
    SuccessSchema,
    ErrorSchema,
    DefaultVolumesSchema,
    WellPathIdSchema,
)


class DefaultVolumesResource(Resource):
    @jwt_required()
    @swagger_decorator(
        path_schema=WellPathIdSchema,
        response_schema={200: DefaultVolumesSchema, 401: ErrorSchema},
        tag="Default Value"
    )
    def get(self, well_id):
        well = Well.query.filter(Well.id == well_id).first()
        if not well or well.pad.project.user_id != get_jwt_identity():
            return {"msg": "Well not found"}, 401

        """ Get default value """
        return well.default_value.to_json()

    @jwt_required()
    @swagger_decorator(
        json_schema=DefaultVolumesSchema,
        path_schema=WellPathIdSchema,
        response_schema={200: SuccessSchema, 401: ErrorSchema},
        tag="Default Value",
    )
    def put(self, well_id):
        """ Create well default value """
        well = Well.query.filter(Well.id == well_id).first()
        if not well or well.pad.project.user_id != get_jwt_identity():
            return {
                "msg": "Well not found",
            }, 401

        req = request.json_schema
        req["well_id"] = well_id

        well.default_value.update(req)

        return {"msg": "Well's default value has been updated"}, 200
