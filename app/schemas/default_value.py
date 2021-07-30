from marshmallow import Schema, fields


class DefaultValueSchema(Schema):
    default_value = fields.Str(required=True, description="Default value")


class DeafultValueDataSchema(Schema):
    test_fields = fields.Str()


class DefaultValuesResponseSchema(Schema):
    status = fields.Int()
    message = fields.Str()
    data = fields.Nested(DeafultValueDataSchema)


class DefaultValueRequestSchema(Schema):
    project_id = fields.Int()
    well_id = fields.Int()
