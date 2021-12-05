from marshmallow import Schema, fields


class PathIdSchema(Schema):
    id = fields.Int()


class WellPathUuidSchema(Schema):
    well_uuid = fields.UUID(required=True, description="Unique identifier of well")


class MessageSchema(Schema):
    msg = fields.Str()
