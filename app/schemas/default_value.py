from marshmallow import Schema, fields


class DefaultValueSchema(Schema):
    default_value = fields.Str(required=True, description="Default value")
