from flask_jwt_extended import jwt_required
from flask_restful import Resource
from flasgger_marshmallow import swagger_decorator

from app.schemas import (
    SuccessSchema,
    ErrorSchema,
    TrackingSheetSchema,
    TrackingSheetIdSchema,
    TrackingSheetStageSchema,
    WellPathIdSchema,
)


class TrackingSheet(Resource):
    @jwt_required()
    @swagger_decorator(
        response_schema={200: TrackingSheetSchema},
        path_schema=TrackingSheetIdSchema,
        tag="Tracking Sheet",
    )
    def get(self, tracking_sheet_id):
        """ Get Tracking sheet """
        return {"name": f"Tracking sheet with id: {tracking_sheet_id}"}

    @jwt_required()
    @swagger_decorator(
        response_schema={200: SuccessSchema},
        path_schema=TrackingSheetIdSchema,
        json_schema=TrackingSheetStageSchema,
        tag="Tracking Sheet",
    )
    def post(self, tracking_sheet_id):
        """ Add stage to tracking sheet """
        # req = request.json_schema
        # stage = req["stage"]
        # TODO create stage
        return {"msg": f"stage in {tracking_sheet_id} created"}

    @jwt_required()
    @swagger_decorator(
        response_schema={200: SuccessSchema},
        path_schema=TrackingSheetIdSchema,
        json_schema=TrackingSheetSchema,
        tag="Tracking Sheet",
    )
    def put(self, tracking_sheet_id):
        """ Update tracking sheet """
        return {"msg": f"Tracking sheet with id {tracking_sheet_id} updated"}


class CreateTrackingSheet(Resource):
    @jwt_required()
    @swagger_decorator(
        json_schema=TrackingSheetSchema,
        path_schema=WellPathIdSchema,
        response_schema={200: SuccessSchema, 401: ErrorSchema},
        tag="Tracking Sheet",
    )
    def post(self):
        """ Create tracking sheet """
        return {"msg": "tracking sheet was created"}
