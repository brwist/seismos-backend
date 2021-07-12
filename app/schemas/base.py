from marshmallow import Schema, fields


class ErrorSchema(Schema):
    msg = fields.Str()


class SuccessSchema(Schema):
    msg = fields.Str()
