from marshmallow import Schema, fields


class UserLoginSchema(Schema):
    username = fields.String(required=True, description="Username for login")
    password = fields.String(required=True, description="Password for login")


class UserDataSchema(Schema):
    username = fields.Str(description="username")
    email = fields.Str(description="email")


class AccessTokenResponseSchema(Schema):
    access_token = fields.Str()
