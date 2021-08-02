from flask import request
from flask_restful import Resource
from app.models import User, Project

from app.schemas import (
    UserLoginSchema,
    AccessTokenResponseSchema,
    UserStatusResponseSchema,
    ErrorSchema,
)

from flask_jwt_extended import (
    create_access_token,
    jwt_required,
    get_jwt_identity
)
from flasgger_marshmallow import swagger_decorator


class Login(Resource):
    @swagger_decorator(
        json_schema=UserLoginSchema,
        response_schema={200: AccessTokenResponseSchema, 403: ErrorSchema},
        tag="Auth",
        jwt_required=False,
    )
    def post(self):
        """ Login user and return JWT token """
        req = request.json_schema

        user = User.authenticate(req["username"], req["password"])
        if user:
            user_data = user.to_dict()
            access_token = create_access_token(identity=user.id)

            user_projects = Project.query.filter(Project.user_id == user.id).all()
            project_ids = []
            for project in user_projects:
                project_ids.append(project.id)

            return {
                "status": 200,
                "message": "Login Successful",
                "data": {
                    "access_token": access_token,
                    "user": user_data,
                    "project_ids": project_ids,
                },
            }

        return {"msg": "User not found"}, 403

    @jwt_required()
    @swagger_decorator(response_schema={200: UserStatusResponseSchema}, tag="Auth")
    def get(self):
        """ Get User Data """
        user_id = get_jwt_identity()
        user = User.query.filter(User.id == user_id).first()
        if not user:
            return {'error': True, 'err_str': 'User not found'}

        user_projects = Project.query.filter(Project.user_id == user_id).all()
        project_ids = []
        for project in user_projects:
            project_ids.append(project.id)

        return {
            "status": 200,
            "message": "User details",
            "data": {
                "user": user.to_dict(),
                "project_ids": project_ids,
            }
        }
