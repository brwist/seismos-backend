import os
from flask import request
from flask_jwt_extended import jwt_required
from flask_restful import Resource
from flasgger_marshmallow import swagger_decorator
from app.schemas import (
    InputFileSchema,
    MessageSchema,
    InputDataRequestSchema,
    DataInputResponseSchema,
    DataInputFileUploadSchema,
    DataInputAreaPathSchema
)
from app.service import azure_client


STATIC_PATH = "static/filebuffer"
# Create directory for files
os.makedirs(STATIC_PATH, exist_ok=True)


class InputData(Resource):
    @jwt_required()
    @swagger_decorator(
        response_schema={200: MessageSchema, 400: MessageSchema},
        file_form_schema=DataInputFileUploadSchema,
        path_schema=DataInputAreaPathSchema,
        tag="Input data"
    )
    def post(self, data_area):
        """ Upload file into server """
        if not request.files:
            return {"msg": "File missing"}, 400

        f = request.files["file"]
        filepath = f"{STATIC_PATH}/{f.filename}"
        f.save(filepath)
        azure_client.upload_file(data_area, filepath)
        os.remove(filepath)

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
