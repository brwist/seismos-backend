from marshmallow import Schema, fields


class TrackingSheetSchema(Schema):
    name = fields.Str(required=True)


class TrackingSheetIdSchema(Schema):
    tracking_sheet_id = fields.Str(required=True)


class TrackingSheetStageSchema(Schema):
    stage = fields.Str(required=True)
