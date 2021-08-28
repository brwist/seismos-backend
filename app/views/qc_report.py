from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_restful import Resource
from flasgger_marshmallow import swagger_decorator
from app.models import Well

from app.schemas import (
    MessageSchema,
    QCReportSchema,
    WellPathIdSchema,
)


class QCReport(Resource):
    @jwt_required()
    @swagger_decorator(
        response_schema={200: QCReportSchema, 401: MessageSchema},
        path_schema=WellPathIdSchema,
        tag="QC Report",
    )
    def get(self, well_id):
        """ Get QC raport data"""
        well = Well.query.filter(Well.id == well_id).first()
        if not well or well.pad.project.user_id != get_jwt_identity():
            return {"msg": "Well not found"}, 401

        stages = []
        for sheet in well.tracking_sheet:
            stages.append({
                "stage_n": sheet.stage,
                "stage_tracking": {
                    "date": sheet.stage_tracking.date.timestamp() * 1000,
                    "customer": sheet.stage_tracking.customer,
                    "well": sheet.stage_tracking.well,
                    "stage": sheet.stage_tracking.stage,
                    "bht_f": sheet.stage_tracking.bht_f,
                    "bht_psi": sheet.stage_tracking.bht_psi,
                    "frac_design": sheet.stage_tracking.frac_design,
                    "field_engineer": {
                        "days": sheet.stage_tracking.field_engineer.days,
                        "nights": sheet.stage_tracking.field_engineer.nights
                    },

                    "plug_type": sheet.stage_tracking.plug_type,
                    "plug_seat_technique": sheet.stage_tracking.plug_seat_technique,
                    "did_an_event_occur": sheet.stage_tracking.did_an_event_occur,
                    "seismos_data_collection": sheet.stage_tracking.seismos_data_collection
                },
            })

        return {"report": stages}, 200


class QCReportExport(Resource):
    @jwt_required()
    @swagger_decorator(
        response_schema={200: MessageSchema, 401: MessageSchema},
        tag="QC Report",
    )
    def post(self):
        """ Export QC TODO """
        return {"msg": "OC export"}
