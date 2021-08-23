import re
from flask import request
from flask_restful import Resource
from app.models import User, Project

from app.schemas import (
    UserLoginSchema,
    AccessTokenResponseSchema,
    UserStatusResponseSchema,
    MessageSchema,
    UserRegisterSchema,
    UserUpdateSchema,
)

from flask_jwt_extended import (
    create_access_token,
    jwt_required,
    get_jwt_identity
)
from flasgger_marshmallow import swagger_decorator


EMAIL_REGEX = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'


class Login(Resource):
    @swagger_decorator(
        json_schema=UserLoginSchema,
        response_schema={200: AccessTokenResponseSchema, 403: MessageSchema},
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


class UserResource(Resource):
    @swagger_decorator(
        json_schema=UserRegisterSchema,
        response_schema={200: AccessTokenResponseSchema, 403: MessageSchema},
        tag="Auth",
        jwt_required=False,
    )
    def post(self):
        if not re.fullmatch(EMAIL_REGEX, request.json["email"]):
            return {"msg": "Invalid email"}, 403

        user = User(
            username=request.json["username"],
            email=request.json["email"],
            password=request.json["password"],
        )

        user.save()
        access_token = create_access_token(identity=user.id)

        return {
                "status": 200,
                "message": "Login Successful",
                "data": {
                    "access_token": access_token,
                    "user": user.to_dict(),
                    "project_ids": [],
                },
            }

    @swagger_decorator(
        json_schema=UserUpdateSchema,
        response_schema={200: MessageSchema, 403: MessageSchema},
        tag="Auth",
        jwt_required=True,
    )
    def put(self):
        req = request.json
        user_id = get_jwt_identity()
        user = User.authenticate(user_id, req["old_password"])

        if not user:
            return {
                "msg": "User not found",
            }

        user.password = req["new_password"]
        user.save()
        return {
            "msg": "User password was updated",
        }
