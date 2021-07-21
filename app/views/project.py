from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required
from flasgger_marshmallow import swagger_decorator


from app.schemas import (
    ProjectSchema,
    ProjectIdPathSchema,
    CreateProjectSuccessSchema,
)

from app.models import (
    Project,
    JobInfo,
)


class ProjectGet(Resource):
    @jwt_required()
    @swagger_decorator(
        response_schema={200: ProjectSchema},
        path_schema=ProjectIdPathSchema,
        tag="Project",
    )
    def get(self, project_id):
        """ Get project data"""
        # TODO get the project    
        return {"name": f"Project with id: {project_id}"}


class ProjectCreate(Resource):
    @jwt_required()
    @swagger_decorator(
        json_schema=ProjectSchema,
        response_schema={200: CreateProjectSuccessSchema},
        tag="Project",
    )
    def post(self):
        """ Create project """
        req = request.json_schema
        project_name = req["projectValues"]["project_name"]
        # project = Project(name=project_name)

        return {
            "status": 200,
            "message": "Project created successfully!",
            "data": {
                "project": {
                    "id": 0,
                }
            }
        }
