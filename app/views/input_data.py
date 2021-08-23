from flask import request
from flask_jwt_extended import jwt_required
from flask_restful import Resource
from flasgger_marshmallow import swagger_decorator
import flasgger
import marshmallow
from app.schemas import (
    InputFileSchema,
    MessageSchema,
    InputDataRequestSchema,
    DataInputResponseSchema,
)


class InputData(Resource):
    @jwt_required()
    @flasgger.swag_from(
        {
            "tags": ["Input data"],
            "requestBody": {
                "description": "Upload file with data input",
                "required": True,
                "content": {
                    "multipart/form-data": {
                        "schema": flasgger.marshmallow_apispec.schema2jsonschema(
                            marshmallow.Schema.from_dict(
                                {
                                    **InputFileSchema().fields,
                                }
                            )
                        ),
                        "encoding": {
                            "watchers": {"style": "form", "explode": True},
                            "attachments": {"style": "form", "explode": True},
                        },
                    }
                },
            },
            "responses": {
                "204": {
                    "description": "Success message",
                    "content": {
                        "application/json": {
                            "schema": flasgger.marshmallow_apispec.schema2jsonschema(
                                marshmallow.Schema.from_dict({**MessageSchema().fields})
                            ),
                        }
                    }
                },
            },
            "security": {"bearerAuth": []},  # TODO swagger not alow send JWT token
        }
    )
    def post(self):
        """ Upload file into server """
        f = request.files["file"]
        f.save(f"static/{f.filename}")
        return {"msg": "OK"}

    @jwt_required()
    @swagger_decorator(
        response_schema={200: DataInputResponseSchema},
        json_schema=InputDataRequestSchema,
        tag="Input data"
    )
    def get(self):
        """Get file wich has been uploaded earler"""
        return {
            "status": 200,
            "message": "Data input details",
            "data": {
                "data_input": {
                    "hydrophone": {
                        "file": "plug",
                    },
                    "pumping_data": {
                        "file": "plug",
                    },
                    "pressure": {
                        "file": "plug",
                    },
                    "survey": {
                        "file": "plug",
                    },
                    "gamma_ray": {
                        "file": "plug",
                    },
                    "mud_log": {
                        "file": "plug",
                    }
                }
            }
        }
