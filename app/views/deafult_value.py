from flask import request
from flask_jwt_extended import jwt_required
from flask_restful import Resource
from flasgger_marshmallow import swagger_decorator

from app.schemas import (
    SuccessSchema,
    ErrorSchema,
    DefaultValueSchema,
)


class DefaultValue(Resource):
    @jwt_required()
    @swagger_decorator(
        response_schema={200: DefaultValueSchema},
        tag="Default Value"
    )
    def get(self):
        """ Get default value """
        return {"default_value": "1100"}

    @jwt_required()
    @swagger_decorator(
        json_schema=DefaultValueSchema,
        response_schema={200: SuccessSchema, 401: ErrorSchema},
        tag="Default Value"
    )
    def put(self):
        """ Update default value """
        req = request.json_schema

        return {"msg": f"Default value updated {req['data']}"}
