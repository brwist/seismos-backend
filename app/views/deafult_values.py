from app.models.default_values import DefaultAdvanceVal
from flask import request
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_restful import Resource
from flasgger_marshmallow import swagger_decorator

from app.models import (
    Well,
    DefaultVal,
    DefaultParamVal,
)

from app.schemas import (
    MessageSchema,
    DefaultValuesSchema,
    WellPathUuidSchema,
)


class DefaultValuesResource(Resource):
    category_class_map = {
        "default_value": DefaultVal,
        "default_advance_val": DefaultAdvanceVal,
        "default_param_val": DefaultParamVal,
    }

    @jwt_required()
    @swagger_decorator(
        path_schema=WellPathUuidSchema,
        json_schema=DefaultValuesSchema,
        response_schema={200: MessageSchema, 401: MessageSchema},
        tag="Default Values",
    )
    def put(self, well_uuid):
        """ Create, update well default volumes """
        well = Well.query.filter(Well.well_uuid == well_uuid).first()
        if not well or well.pad.project.user_id != get_jwt_identity():
            return {"msg": f"Well with uuid {well_uuid} not found"}, 401

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
        path_schema=WellPathUuidSchema,
        response_schema={200: DefaultValuesSchema, 401: MessageSchema, 204: MessageSchema},
        tag="Default Values"
    )
    def get(self, well_uuid):
        well = Well.query.filter(Well.well_uuid == well_uuid).first()
        if not well:
            return {"msg": f"Well with uuid {well_uuid} not found"}, 401

        default_values = {}
        for default_valumes_field in self.category_class_map.keys():

            if not getattr(well, default_valumes_field):
                return {"msg": "Default volumes not created for this well"}, 204

            default_values[default_valumes_field] = getattr(well, default_valumes_field).to_json()

        return default_values
