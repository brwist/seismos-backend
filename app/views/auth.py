import re
from flask import request
from flask_restful import Resource
from werkzeug.security import generate_password_hash
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

            user_projects = Project.query.all()
            project_uuids = []
            for project in user_projects:
                project_uuids.append(project.project_uuid)

            return {
                "status": 200,
                "message": "Login Successful",
                "data": {
                    "access_token": access_token,
                    "user": user_data,
                    "projects": project_uuids,
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

        user_projects = Project.query.all()
        project_uuids = []
        for project in user_projects:
            project_uuids.append(project.project_uuid)

        return {
            "status": 200,
            "message": "User details",
            "data": {
                "user": user.to_dict(),
                "project_uuids": project_uuids,
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
            password=generate_password_hash(request.json["password"]),
        )

        user.save()
        access_token = create_access_token(identity=user.id)

        return {
                "status": 200,
                "message": "Login Successful",
                "data": {
                    "access_token": access_token,
                    "user": user.to_dict(),
                    "projects": [],
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
