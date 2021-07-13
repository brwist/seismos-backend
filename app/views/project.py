from flask_jwt_extended import jwt_required
from flask_restful import Resource
from flasgger_marshmallow import swagger_decorator

from app.schemas import (
    ProjectSchema,
    ProjectIdPathSchema,
    SuccessSchema,
    ErrorSchema,
)


class Project(Resource):
    @jwt_required()
    @swagger_decorator(
        response_schema={200: ProjectSchema},
        path_schema=ProjectIdPathSchema,
        tag="Project",
    )
    def get(self, project_id):
        """ Get project data"""
        return {"name": f"Project with id: {project_id}"}


class ProjectCreate(Resource):
    @jwt_required()
    @swagger_decorator(
        json_schema=ProjectSchema,
        response_schema={200: SuccessSchema, 401: ErrorSchema},
        tag="Project",
    )
    def post(self):
        """ Create project """
        return {"msg": "project created"}
