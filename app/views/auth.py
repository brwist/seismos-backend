from flask import request
from flask_restful import Resource
from app.models import User
from marshmallow import Schema, fields
from flask_jwt_extended import (
    create_access_token,
    jwt_required,
    get_jwt_identity
)
from flasgger_marshmallow import swagger_decorator


class UserLogin(Schema):
    username = fields.String(required=True, description="Username for login")
    password = fields.String(required=True, description="Password for login")


class UserData(Schema):
    username = fields.Str(description="username")
    email = fields.Str(description="email")


class AccessTokenResponse(Schema):
    access_token = fields.Str()


class UserDataSchema(Schema):
    username = fields.Str()
    email = fields.Str()


class Login(Resource):
    class ErrorSchema(Schema):
        err_str = fields.Str(description="Error description")

    @swagger_decorator(
        json_schema=UserLogin,
        response_schema={200: AccessTokenResponse, 401: ErrorSchema},
    )
    def post(self):
        """ Login user and return JWT token """
        req = request.json_schema

        user = User.authenticate(req["username"], req["password"])
        if user:
            access_token = create_access_token(identity=user.username)
            return {"access_token": access_token}

        return {"err_str": "User not found"}, 401

    @jwt_required()
    @swagger_decorator(response_schema={200: UserData})
    def get(self):
        """ Get User Data """
        username = get_jwt_identity()
        user = User.filter(User.username == username).first()
        if not user:
            return {'error': True, 'err_str': f'User {username} not found'}

        return {"username": user.username, "email": user.email}
