from marshmallow import Schema, fields


class DailyLogSchema(Schema):
    data = fields.Str(required=True, description="Some data about daily log")
