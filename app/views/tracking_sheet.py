from datetime import datetime
import json
from flask import request
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_restful import Resource
from flasgger_marshmallow import swagger_decorator
from app.models import (
    Well,
    Stage,
    StageAVG,
    ChemFluids,
    FormationFuildInjection,
    Perforation,
    Proppant,
    ActiveData,
)

from app.schemas import (
    MessageSchema,
    TrackingSheetSchema,
    TrackingSheetUuidSchema,
    WellPathUuidSchema,
    TrackingSheetStagesListResponse,
    UpdateStageSchema,
)


class TrackingSheetResource(Resource):
    @jwt_required()
    @swagger_decorator(
        # TODO response_schema={200: TrackingSheetSchema, 401: MessageSchema},
        path_schema=TrackingSheetUuidSchema,
        tag="Tracking Sheet",
    )
    def get(self, stage_uuid):
        """ Get Tracking sheet """
        stage = Stage.query.filter(Stage.stage_uuid == stage_uuid).first()
        if not stage or stage.well.pad.project.user_id != get_jwt_identity():
            return {"msg": "Stage not found"}, 401

        data = stage.to_json()

        for stage_field in (
            "nf_processing_result", "stage_avg", "ff_processing_result",
            "chem_fluids", "perforation"
        ):
            stage_data = getattr(stage, stage_field)
            if stage_data:
                data["stage"][stage_field] = stage_data.to_json(True)

        data["stage"]["proppant"] = []
        for proppant in stage.proppant:
            data["stage"]["proppant"].append(proppant.to_json())

        data["stage"]["stage_start_time"] = int(data["stage"]["stage_start_time"])

        return data

    @jwt_required()
    @swagger_decorator(
        path_schema=TrackingSheetUuidSchema,
        json_schema=UpdateStageSchema,
        response_schema={200: MessageSchema, 401: MessageSchema},
        tag="Tracking Sheet",
    )
    def put(self, stage_uuid):
        stage = Stage.query.filter(Stage.stage_uuid == stage_uuid).first()
        if not stage or stage.well.pad.project.user_id != get_jwt_identity():
            return {"msg": "Stage not found"}, 401

        stage_data_map = {
            "stage": stage,
            "chem_fluids": stage.chem_fluids,
            "perforation": stage.perforation,
            "stage_avg": stage.stage_avg,
        }

        req = request.json
        for req_field, data in req.items():
            obj_data = stage_data_map.get(req_field)
            if obj_data is not None:
                for field, value in data.items():
                    setattr(obj_data, field, value)
                obj_data.save()

        return {"msg": "Stage updated"}


class TrackingSheetStageList(Resource):
    @jwt_required()
    @swagger_decorator(
        path_schema=WellPathUuidSchema,
        response_schema={200: TrackingSheetStagesListResponse, 401: MessageSchema},
        tag="Tracking Sheet",
    )
    def get(self, well_uuid):
        well = Well.query.filter(Well.well_uuid == well_uuid).first()

        if not well or well.pad.project.user_id != get_jwt_identity():
            return {"msg": f"Well with id {well_uuid} not found"}, 401

        stages = []
        for stage in well.stages:
            stages.append({
                "uuid": stage.stage_uuid,
                "stage_n": stage.stage_number,
            })

        return {
            "stages": stages,
        }, 200


class CreateTrackingSheet(Resource):
    @jwt_required()
    @swagger_decorator(
        json_schema=TrackingSheetSchema,
        path_schema=WellPathUuidSchema,
        response_schema={201: MessageSchema, 401: MessageSchema},
        tag="Tracking Sheet",
    )
    def post(self, well_uuid):
        """ Create tracking sheet """
        well = Well.query.filter(Well.well_uuid == well_uuid).first()

        if not well or well.pad.project.user_id != get_jwt_identity():
            return {"msg": f"Well with id {well_uuid} not found"}, 401

        req = request.json
        stage_data = req["stage_data"]

        for stage in well.stages:
            if stage.stage_number == req["stage"]:
                return {"msg": f"Stage with number: {stage.stage_number} already exist"}, 401

        stage = Stage(
            well_id=well.id,

            bottomhole_bht=req["stage_tracking"]["bottomhole_bht"],
            bottomhole_bhp=req["stage_tracking"]["bottomhole_bhp"],
            frac_design=req["stage_tracking"]["frac_design"],
            plug_type=req["stage_tracking"]["plug_type"],
            plug_seat_technique=req["stage_tracking"]["plug_seat_technique"],
            stage_event=req["stage_tracking"]["did_an_event_occur"],
            data_collection=req["stage_tracking"]["seismos_data_collection"],

            stage_number=req["stage"],
            stage_start_time=stage_data["stage_start_time"],
            stage_end_time=stage_data["stage_end_time"],

            designed_max_prop=stage_data["pumping_summary"]["max_prop_conc"]["design"],
            designed_pad_vol=stage_data["pumping_summary"]["total_pad_volume"]["design"],
            designed_total_clean_fluid_vol=stage_data["pumping_summary"]["total_clean_fluid_volume"]["design"],
            designed_flush_vol=stage_data["pumping_summary"]["flush_volume"]["design"],

            diverter_type=req["perforation_interval_information"]["diverter_type"],
            pumped_diverter=req["perforation_interval_information"]["pumped_diverter"],
            designed_slurry_vol=stage_data["pumping_summary"]["slurry_volume"]["design"],

            spf=req["perforation_interval_information"]["spf"],
            plug_depth=req["perforation_interval_information"]["plug_depth"],
            number_of_cluster=req["perforation_interval_information"]["n_clusters"],
            is_acid=req["perforation_interval_information"]["acid"],
            top_perf_Displacement_volume=req["perforation_interval_information"]["displacement_volume"]["top_perf"],
            bottom_perf_Displacement_volume=req["perforation_interval_information"]["displacement_volume"]["bottom_perf"],
            plug_displacement_volume=req["perforation_interval_information"]["displacement_volume"]["plug"],
        ).save()

        chem_fluids = ChemFluids(
            stage_id=stage.id,
            base_fluid_density=req["stage_data"]["fluid_parameters"]["base_fluid_density"],
            base_fluid_type=req["stage_data"]["fluid_parameters"]["base_fluid_type"],
            max_conc_density=req["stage_data"]["fluid_parameters"]["max_conc_density"],
            design_acid_vol=req["stage_data"]["pumping_summary"]["acid_volume"]["design"],
        ).save()

        for fluid_item in req["stage_data"]["fluids_injected_into_formation"]:
            fluid_item["chem_fluid_id"] = chem_fluids.id
            FormationFuildInjection(**fluid_item).save()

        Perforation(
            stage_id=stage.id,
            top_measured_depth=req["perforation_interval_information"]["top_measured_depth"],
            bottom_measured_depth=req["perforation_interval_information"]["bottom_measured_depth"],
            perf_gun_description=req["perforation_interval_information"]["perf_gun_description"],
            estimated_hole_diameter=req["perforation_interval_information"]["perf_daiameter"],
        ).save()

        StageAVG(
            stage_id=stage.id,

            opening_well=req["stage_data"]["opening_well"],
            max_prop_conc=req["stage_data"]["pumping_summary"]["max_prop_conc"]["actual"],
            pad_vol=req["stage_data"]["pumping_summary"]["total_pad_volume"]["actual"],
            total_clean=req["stage_data"]["pumping_summary"]["total_clean_fluid_volume"]["actual"],
            acid=req["stage_data"]["pumping_summary"]["acid_volume"]["actual"],
            flush_volume=stage_data["pumping_summary"]["flush_volume"]["actual"],
            total_slurry=req["stage_data"]["pumping_summary"]["slurry_volume"]["actual"],
            # isip=req["stage_data"]["isip"], disable
        ).save()

        # proppant data
        for proppant in req["stage_data"]["proppant_data"]:
            Proppant(
                stage_id=stage.id,
                bulk_density=proppant["bulk_density"],
                proppant_name=proppant["description"],
                specific_gravity=proppant["specific_gravity"],
                total_pumped_lbs=proppant["amount_pumped"],
                actual_lbs=req["stage_data"]["pumping_summary"]["total_proppant"]["actual"],
                designed_lbs=req["stage_data"]["pumping_summary"]["total_proppant"]["design"],
            ).save()

        well.num_stages += 1
        well.save()

        active_data = {}
        # unpack active data
        for _, data in req["active_data"].items():
            for field, value in data.items():
                active_data[field] = value
        for field, value in req["notes"].items():
            active_data[field] = value
        active_data["stage_id"] = stage.id

        for time_field in (
            "post_frac_start_time",
            "post_frac_end_time",
            "pre_frac_start_time",
            "pre_frac_end_time",
        ):
            active_data[time_field] //= 1000

        ActiveData(**active_data).save()

        return {"msg": "tracking sheet was created"}, 201


class TrackingSheetTestData(Resource):
    @jwt_required()
    @swagger_decorator(
        path_schema=TrackingSheetUuidSchema,
        response_schema={200: MessageSchema, 401: MessageSchema},
        tag="Tracking Sheet",
    )
    def get(self, stage_uuid):
        """ Get Tracking sheet """
        stage = Stage.query.filter(Stage.stage_uuid == stage_uuid).first()
        if not stage or stage.well.pad.project.user_id != get_jwt_identity():
            return {"msg": "Stage not found"}, 401

        with open("static/singlestore/test_trackingsheet_data.json", "r") as f_data:
            data = json.load(f_data)
            for key, value in data["stage"]["fields"].items():
                setattr(stage, key, value)

            for key, value in data["stage"]["arrays"].items():
                array_field = getattr(stage, key)
                for field in array_field:
                    for field_name, field_value in value["fields"].items():
                        setattr(field, field_name, field_value)
                    for field_name, field_value in value["datetime_fields"].items():
                        setattr(field, field_name, datetime.fromtimestamp(field_value))

        stage.save()
        return {"msg": "Test data inserted"}
