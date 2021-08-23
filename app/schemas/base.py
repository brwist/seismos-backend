from marshmallow import Schema, fields

class PathIdSchema(Schema):
    id = fields.Int()


class WellPathIdSchema(Schema):
    well_id = fields.Str()


class MessageSchema(Schema):
    msg = fields.Str()
