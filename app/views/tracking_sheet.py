from datetime import datetime
from flask import request
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_restful import Resource
from flasgger_marshmallow import swagger_decorator
from app.models import (
    Well,
    TrackingSheet,
    StageTracking,
    FieldEngineer,
    PerforationIntervalInformation,
    DisplacementVolume,
    StageData,
    FluidParameters,
    FluidsInjectedIntoFormation,
    PropantData,
    PumpingSummary,
    ActiveData,
    Notes,
)

from app.schemas import (
    MessageSchema,
    TrackingSheetSchema,
    TrackingSheetIdSchema,
    TrackingSheetStageSchema,
    WellPathIdSchema,
    TrackingSheetStagesListResponse,
)


class TrackingSheetResource(Resource):
    @jwt_required()
    @swagger_decorator(
        response_schema={200: TrackingSheetSchema, 401: MessageSchema},
        path_schema=TrackingSheetIdSchema,
        tag="Tracking Sheet",
    )
    def get(self, tracking_sheet_id):
        """ Get Tracking sheet """
        tracksheet = TrackingSheet.query.filter(TrackingSheet.id == tracking_sheet_id).first()
        if not tracksheet or tracksheet.well.pad.project.user_id != get_jwt_identity():
            return {"msg": "tracksheet not found"}, 401

        return tracksheet.to_json()

    @jwt_required()
    @swagger_decorator(
        response_schema={200: MessageSchema},
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
        response_schema={200: MessageSchema},
        path_schema=TrackingSheetIdSchema,
        json_schema=TrackingSheetSchema,
        tag="Tracking Sheet",
    )
    def put(self, tracking_sheet_id):
        """ Update tracking sheet """
        return {"msg": f"Tracking sheet with id {tracking_sheet_id} updated"}


class TrackingSheetStageList(Resource):
    @jwt_required()
    @swagger_decorator(
        path_schema=WellPathIdSchema,
        response_schema={200: TrackingSheetStagesListResponse, 401: MessageSchema},
        tag="Tracking Sheet",
    )
    def get(self, well_id):
        well = Well.query.filter(Well.id == well_id).first()
        if not well or well.pad.project.user_id != get_jwt_identity():
            return {"msg": "Well not found"}, 401

        stages = []
        for sheet in well.tracking_sheet:
            stages.append({
                "stage": sheet.stage,
                "sheet_id": sheet.id,
            })

        return {
            "stages": stages,
        }, 200


class CreateTrackingSheet(Resource):
    @jwt_required()
    @swagger_decorator(
        json_schema=TrackingSheetSchema,
        path_schema=WellPathIdSchema,
        response_schema={201: MessageSchema, 401: MessageSchema},
        tag="Tracking Sheet",
    )
    def post(self, well_id):
        """ Create tracking sheet """

        well = Well.query.filter(Well.id == well_id).first()
        if not well or well.pad.project.user_id != get_jwt_identity():
            return {"msg": "Well not found"}, 401

        req = request.json
        stage_tracking_data = req["stage_tracking"]
        perforation_interval_information_data = req["perforation_interval_information"]
        stage_data = req["stage_data"]
        active_data = req["active_data"]

        # Timestamps inverting to python DATETIME format
        stage_tracking_data["date"] = datetime.fromtimestamp(stage_tracking_data["date"] // 1000)
        stage_data["stage_start_time"] = datetime.fromtimestamp(stage_data["stage_start_time"] // 1000)
        stage_data["stage_end_time"] = datetime.fromtimestamp(stage_data["stage_end_time"] // 1000)
        active_data["pre_frac_pulses"]["start_time"] = datetime.fromtimestamp(
            active_data["pre_frac_pulses"]["start_time"] // 1000
        )
        active_data["pre_frac_pulses"]["end_time"] = datetime.fromtimestamp(
            active_data["pre_frac_pulses"]["end_time"] // 1000
        )
        active_data["post_frac_pulses"]["start_time"] = datetime.fromtimestamp(
            active_data["post_frac_pulses"]["start_time"] // 1000
        )
        active_data["post_frac_pulses"]["end_time"] = datetime.fromtimestamp(
            active_data["post_frac_pulses"]["end_time"] // 1000
        )

        field_engineer = FieldEngineer(
            days=stage_tracking_data["field_engineer"]["days"],
            nights=stage_tracking_data["field_engineer"]["nights"],
        )
        field_engineer.save()

        stage_tracking_model = StageTracking(
            date=stage_tracking_data["date"],
            customer=stage_tracking_data["customer"],
            well=stage_tracking_data["well"],
            stage=stage_tracking_data["stage"],
            bht_f=stage_tracking_data["bht_f"],
            bht_psi=stage_tracking_data["bht_psi"],
            frac_design=stage_tracking_data["frac_design"],
            field_engineer_id=field_engineer.id,
            plug_type=stage_tracking_data["plug_type"],
            plug_seat_technique=stage_tracking_data["plug_type"],
            did_an_event_occur=stage_tracking_data["did_an_event_occur"],
            seismos_data_collection=stage_tracking_data["seismos_data_collection"]
        )

        displacement_volume_model = DisplacementVolume(
            top_perf=perforation_interval_information_data["displacement_volume"]["top_perf"],
            bottom_perf=perforation_interval_information_data["displacement_volume"]["bottom_perf"],
            plug=perforation_interval_information_data["displacement_volume"]["plug"],
        )

        displacement_volume_model.save()

        perforation_interval_information_model = PerforationIntervalInformation(
            top_perf=perforation_interval_information_data["top_perf"],
            bottom_perf=perforation_interval_information_data["bottom_perf"],
            plug_depth=perforation_interval_information_data["plug_depth"],
            n_clusters=perforation_interval_information_data["n_clusters"],
            perf_gun_description=perforation_interval_information_data["perf_gun_description"],
            perf_daiameter=perforation_interval_information_data["perf_daiameter"],
            spf=perforation_interval_information_data["spf"],
            pumped_diverter=perforation_interval_information_data["pumped_diverter"],
            diverter_type=perforation_interval_information_data["diverter_type"],
            acid=perforation_interval_information_data["diverter_type"],
            displacement_volume_id=displacement_volume_model.id,
        )

        fluid_parameters_model = FluidParameters(
            base_fluid_type=stage_data["fluid_parameters"]["base_fluid_type"],
            base_fluid_density=stage_data["fluid_parameters"]["base_fluid_density"],
            max_conc_density=stage_data["fluid_parameters"]["base_fluid_density"],
        )

        fluids_injected_into_formation_model = FluidsInjectedIntoFormation(
            last_description=stage_data["fluids_injected_into_formation"]["last"]["description"],
            last_bbls=stage_data["fluids_injected_into_formation"]["last"]["bbls"],
            last_ppg=stage_data["fluids_injected_into_formation"]["last"]["ppg"],
            second_to_last_description=stage_data["fluids_injected_into_formation"]["second_to_last"]["description"],
            second_to_last_bbls=stage_data["fluids_injected_into_formation"]["second_to_last"]["bbls"],
            second_to_last_ppg=stage_data["fluids_injected_into_formation"]["second_to_last"]["ppg"],
            third_to_last_description=stage_data["fluids_injected_into_formation"]["third_to_last"]["description"],
            third_to_last_bbls=stage_data["fluids_injected_into_formation"]["third_to_last"]["bbls"],
            third_to_last_ppg=stage_data["fluids_injected_into_formation"]["third_to_last"]["ppg"],
        )

        pumping_summary_model = PumpingSummary(
            max_prop_conc_design=stage_data["pumping_summary"]["max_prop_conc"]["design"],
            max_prop_conc_actual=stage_data["pumping_summary"]["max_prop_conc"]["actual"],
            total_pad_volume_design=stage_data["pumping_summary"]["total_pad_volume"]["design"],
            total_pad_volume_actual=stage_data["pumping_summary"]["total_pad_volume"]["actual"],
            total_clean_fluid_volume_design=stage_data["pumping_summary"]["total_clean_fluid_volume"]["design"],
            total_clean_fluid_volume_actual=stage_data["pumping_summary"]["total_clean_fluid_volume"]["actual"],
            total_forty_seventy_design=stage_data["pumping_summary"]["total_forty_seventy"]["design"],
            total_forty_seventy_actual=stage_data["pumping_summary"]["total_forty_seventy"]["actual"],
            total_sand_design=stage_data["pumping_summary"]["total_sand"]["design"],
            total_sand_actual=stage_data["pumping_summary"]["total_sand"]["actual"],
            acid_volume_design=stage_data["pumping_summary"]["acid_volume"]["design"],
            acid_volume_actual=stage_data["pumping_summary"]["acid_volume"]["actual"],
            flush_volume_design=stage_data["pumping_summary"]["flush_volume"]["design"],
            flush_volume_actual=stage_data["pumping_summary"]["flush_volume"]["actual"],
            slurry_volume_design=stage_data["pumping_summary"]["slurry_volume"]["design"],
            slurry_volume_actual=stage_data["pumping_summary"]["slurry_volume"]["actual"],
        )

        fluid_parameters_model.save()
        fluids_injected_into_formation_model.save()
        pumping_summary_model.save()

        stage_data_model = StageData(
            stage_start_time=stage_data["stage_start_time"],
            stage_end_time=stage_data["stage_end_time"],
            opening_well=stage_data["opening_well"],
            isip=stage_data["isip"],
            fluid_parameters_id=fluid_parameters_model.id,
            fluids_injected_into_formation_id=fluids_injected_into_formation_model.id,
            pumping_summary_id=pumping_summary_model.id,
        )

        active_data_model = ActiveData(
            pilsing_parameters_wave_type=active_data["pilsing_parameters"]["wave_type"],
            pilsing_parameters_periods=active_data["pilsing_parameters"]["periods"],
            pilsing_parameters_freq=active_data["pilsing_parameters"]["freq"],
            pilsing_parameters_offset=active_data["pilsing_parameters"]["offset"],
            pilsing_parameters_amplitude=active_data["pilsing_parameters"]["amplitude"],

            pre_frac_pulses_start_time=active_data["pre_frac_pulses"]["start_time"],
            pre_frac_pulses_end_time=active_data["pre_frac_pulses"]["end_time"],
            pre_frac_pulses_n_pulses=active_data["pre_frac_pulses"]["n_pulses"],

            post_frac_pulses_start_time=active_data["post_frac_pulses"]["start_time"],
            post_frac_pulses_end_time=active_data["post_frac_pulses"]["end_time"],
            post_frac_pulses_n_pulses=active_data["post_frac_pulses"]["n_pulses"],
        )

        notes = Notes(
            pre_frac_pulse=req["notes"]["pre_frac_pulse"],
            post_frac_pulse=req["notes"]["post_frac_pulse"],
            other=req["notes"]["other"],
        )

        stage_tracking_model.save()
        perforation_interval_information_model.save()
        stage_data_model.save()
        for propant_data in stage_data["propant_data"]:
            PropantData(
                stage_data_id=stage_data_model.id,
                description=propant_data["description"],
                specific_gravity=propant_data["specific_gravity"],
                bulk_density=propant_data["bulk_density"],
            ).save()
        active_data_model.save()
        notes.save()

        TrackingSheet(
            well_id=well.id,
            stage=req["stage"],
            stage_tracking_id=stage_tracking_model.id,
            perforation_interval_information_id=perforation_interval_information_model.id,
            stage_data_id=stage_data_model.id,
            active_data_id=active_data_model.id,
            notes_id=notes.id,
        ).save()

        well.num_stages += 1
        well.save()

        return {"msg": "tracking sheet was created"}, 201
