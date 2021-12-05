from marshmallow import Schema, fields


class BackupIndexSchema(Schema):
    backup_index = fields.Int()
