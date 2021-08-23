from app.models.default_volumes import DefaultAdvanceVal
import sys
import re
from flask import request
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_restful import Resource
from flasgger_marshmallow import swagger_decorator

from app.models import (
    Well,
    DefaultVal,
    DefaultAdvanceVal,
    DefaultParamVal,
)

from app.schemas import (
    MessageSchema,
    DefaultVolumesSchema,
    WellPathIdSchema,
)


class DefaultVolumesResource(Resource):
    category_class_map = {
        "default_value": DefaultVal,
        "default_advance_val": DefaultAdvanceVal,
        "default_param_val": DefaultParamVal,
    }

    @jwt_required()
    @swagger_decorator(
        json_schema=DefaultVolumesSchema,
        path_schema=WellPathIdSchema,
        response_schema={200: MessageSchema, 401: MessageSchema},
        tag="Default Volumes",
    )
    def put(self, well_id):
        """ Create, update well default volumes """
        well = Well.query.filter(Well.id == well_id).first()
        if not well or well.pad.project.user_id != get_jwt_identity():
            return {
                "msg": "Well not found",
            }, 401

        req = request.json_schema

        for category in req.keys():
            category_model = getattr(well, category)
            if not category_model:
                category_model = self.category_class_map[category](
                    **req[category]
                )
                category_model.well_id = well.id
                category_model.save()

            else:
                category_model.update(req[category])

        return {"msg": "Well's default value has been updated"}, 200


    @jwt_required()
    @swagger_decorator(
        path_schema=WellPathIdSchema,
        response_schema={200: DefaultVolumesSchema, 401: MessageSchema, 204: MessageSchema},
        tag="Default Volumes"
    )
    def get(self, well_id):
        well = Well.query.filter(Well.id == well_id).first()
        if not well or well.pad.project.user_id != get_jwt_identity():
            return {
                "msg": "Well not found",
            }, 401

        default_volumes = {}
        for default_valumes_field in self.category_class_map.keys():

            if not getattr(well, default_valumes_field):
                return {"msg": "Default volumes not created for this well"}, 204

            default_volumes[default_valumes_field] = getattr(well, default_valumes_field).to_json()

        return default_volumes
