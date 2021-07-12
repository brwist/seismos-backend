from marshmallow import Schema, fields


class InputFileSchema(Schema):
    file = fields.Raw(
        required=True,
        metadata=dict(description='File to upload'),
        type="file",
        name="filename",
    )
