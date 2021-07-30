from marshmallow import Schema, fields


class ErrorSchema(Schema):
    msg = fields.Str()


class SuccessSchema(Schema):
    msg = fields.Str()


class PathIdSchema(Schema):
    id = fields.Int()


class WellPathIdSchema(Schema):
    well_id = fields.Int()
