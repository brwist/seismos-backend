from marshmallow import Schema, fields


class UserLoginSchema(Schema):
    username = fields.String(required=True, description="Username for login")
    password = fields.String(required=True, description="Password for login")


class UserRegisterSchema(Schema):
    username = fields.String(required=True, description="Username for login")
    email = fields.String(required=True, description="Email")
    password = fields.String(required=True, description="Password for login")


class UserSchema(Schema):
    id = fields.Int()
    username = fields.String()
    email = fields.Email()
    active = fields.Boolean()
    created_at = fields.Int()


class UserStatusDataScheme(Schema):
    user = fields.Nested(UserSchema)
    project_ids = fields.List(fields.Integer())


class AccessTokenSuccessSchema(Schema):
    access_token = fields.Str()
    user = fields.Nested(UserSchema)
    project_ids = fields.List(fields.Int())


class AccessTokenResponseSchema(Schema):
    status = fields.Int()
    message = fields.Str()
    data = fields.Nested(AccessTokenSuccessSchema)


class UserStatusResponseSchema(Schema):
    status = fields.Int()
    message = fields.Str()
    data = fields.Nested(UserStatusDataScheme)


class UserUpdateSchema(Schema):
    old_password = fields.Str()
    new_password = fields.Str()
