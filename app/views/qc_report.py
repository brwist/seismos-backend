from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_restful import Resource, request
from flasgger_marshmallow import swagger_decorator
from app.models import Well, Stage
from app.schemas import (
    MessageSchema,
    WellPathUuidSchema,
    StagesUuidsSchema
)


class QCReport(Resource):
    @jwt_required()
    @swagger_decorator(
        response_schema={401: MessageSchema},
        path_schema=WellPathUuidSchema,
        tag="QC Report",
    )
    def get(self, well_uuid):
        """ Get QC raport data"""
        well = Well.query.filter(Well.well_uuid == well_uuid).first()
        # current point
        if not well or well.pad.project.user_id != get_jwt_identity():
            return {"msg": "Well not found"}, 401

        report_fields = ["nf_processing_result", "stage_avg", "ff_processing_result"]

        report = {
            "stages": well.num_stages,
        }

        for stage in well.stages:
            report[stage.stage_number] = {"stage": stage.generate_report(True)}
            for report_field in report_fields:
                model_field = getattr(stage, report_field)
                if model_field:
                    report[stage.stage_number][report_field] = model_field.generate_report(True)

        return {"report": report}, 200


class QCReportApprove(Resource):
    @jwt_required()
    @swagger_decorator(
        response_schema={200: MessageSchema, 401: MessageSchema},
        json_schema=StagesUuidsSchema,
        tag="QC Report",
    )
    def post(self):
        """Approve stages"""
        req = request.json_schema

        for stage_id in req["stage_ids"]:
            stage = Stage.query.filter(Stage.id == stage_id).first()

            if not stage or stage.well.pad.project.user_id != get_jwt_identity():
                return {"msg": "Stage with id {stage_id} not found"}, 401

            stage.is_approved = 1
            stage.save()

        return {"msg": "Stages approved"}, 200
