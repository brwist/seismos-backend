from flask import request
from flask_restful import Resource
from app.models import User

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
        response_schema={200: AccessTokenResponseSchema, 401: ErrorSchema},
        tag="Auth",
        jwt_required=False,
    )
    def post(self):
        """ Login user and return JWT token """
        req = request.json_schema

        user = User.authenticate(req["username"], req["password"])
        if user:
            user_data = user.to_dict()
            access_token = create_access_token(identity=user.username)
            return {
                "status": 200,
                "message": "Login Successful",
                "data": {
                    "access_token": access_token,
                    "user": user_data,
                    "project_ids": [],  # TODO fill projects
                },
            }

        return {"msg": "User not found"}, 401

    @jwt_required()
    @swagger_decorator(response_schema={200: UserStatusResponseSchema}, tag="Auth")
    def get(self):
        """ Get User Data """
        username = get_jwt_identity()
        user = User.query.filter(User.username == username).first()
        if not user:
            return {'error': True, 'err_str': f'User {username} not found'}

        return {
            "status": 200,
            "message": "User details",
            "data": {
                "user": user.to_dict(),
                "project_ids": [],  # TODO fill projects
            }
        }
