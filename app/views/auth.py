from flask import request
from flask_restful import Resource
from app.models import User

from app.schemas import (
    UserLoginSchema,
    UserDataSchema,
    AccessTokenResponseSchema,
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
    )
    def post(self):
        """ Login user and return JWT token """
        req = request.json_schema

        user = User.authenticate(req["username"], req["password"])
        if user:
            access_token = create_access_token(identity=user.username)
            return {"access_token": access_token}

        return {"msg": "User not found"}, 401

    @jwt_required()
    @swagger_decorator(response_schema={200: UserDataSchema}, tag="Auth")
    def get(self):
        """ Get User Data """
        username = get_jwt_identity()
        user = User.filter(User.username == username).first()
        if not user:
            return {'error': True, 'err_str': f'User {username} not found'}

        return {"username": user.username, "email": user.email}
