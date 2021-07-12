from marshmallow import Schema, fields


class OCReportSchema(Schema):
    raport = fields.Str()
