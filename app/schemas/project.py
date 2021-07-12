from marshmallow import Schema, fields


class ProjectSchema(Schema):
    name = fields.Str(required=True)


class ProjectIdPathSchema(Schema):
    project_id = fields.Str(required=True)
