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
    TrackingSheetResponseSchema,
    TrackingSheetUuidSchema,
    WellPathUuidSchema,
    TrackingSheetStagesListResponse,
    TrackingSheetUpdateSchema,
    TrackingSheetCreatedSchema
)


TRACKINGSHEET_MAP = {
    Stage: {
        "bottomhole_bht": ("stage_tracking", "bottomhole_bht"),
        "bottomhole_bhp": ("stage_tracking", "bottomhole_bhp"),
        "frac_design": ("stage_tracking", "frac_design"),
        "plug_type": ("stage_tracking", "plug_type"),
        "plug_seat_technique": ("stage_tracking", "plug_seat_technique"),
        "stage_event": ("stage_tracking", "did_an_event_occur"),
        "data_collection": ("stage_tracking", "seismos_data_collection"),
        "stage_number": ("stage", ),
        "stage_start_time": ("stage_data", "stage_start_time"),
        "stage_end_time": ("stage_data", "stage_end_time"),
        "designed_max_prop": ("stage_data", "pumping_summary", "max_prop_conc", "design"),
        "designed_pad_vol": ("stage_data", "pumping_summary", "total_pad_volume", "design"),
        "designed_total_clean_fluid_vol": ("stage_data", "pumping_summary", "total_clean_fluid_volume", "design"),
        "designed_flush_vol": ("stage_data", "pumping_summary", "flush_volume", "design"),
        "diverter_type": ("perforation_interval_information", "diverter_type"),
        "pumped_diverter": ("perforation_interval_information", "pumped_diverter",),
        "designed_slurry_vol": ("stage_data", "pumping_summary", "slurry_volume", "design"),
        "designed_proppant": ("stage_data", "pumping_summary", "total_proppant", "design"),
        "spf": ("perforation_interval_information", "spf"),
        "plug_depth": ("perforation_interval_information", "plug_depth"),
        "number_of_cluster": ("perforation_interval_information", "n_clusters"),
        "is_acid": ("perforation_interval_information", "acid"),
        "top_perf_Displacement_volume": ("perforation_interval_information", "displacement_volume", "top_perf"),
        "bottom_perf_Displacement_volume": ("perforation_interval_information", "displacement_volume", "bottom_perf"),
        "plug_displacement_volume": ("perforation_interval_information", "displacement_volume", "plug"),
    },
    ChemFluids: {
        "base_fluid_density": ("stage_data", "fluid_parameters", "base_fluid_density"),
        "base_fluid_type": ("stage_data", "fluid_parameters", "base_fluid_type"),
        "max_conc_density": ("stage_data", "fluid_parameters", "max_conc_density"),
        "design_acid_vol": ("stage_data", "pumping_summary", "acid_volume", "design"),
    },

    Perforation: {
        "top_measured_depth": ("perforation_interval_information", "top_measured_depth"),
        "bottom_measured_depth": ("perforation_interval_information", "bottom_measured_depth"),
        "perf_gun_description": ("perforation_interval_information", "perf_gun_description"),
        "estimated_hole_diameter": ("perforation_interval_information", "perf_daiameter"),
    },
    StageAVG: {
        "opening_well": ("stage_data", "opening_well"),
        "max_prop_conc": ("stage_data", "pumping_summary", "max_prop_conc", "actual"),
        "pad_vol": ("stage_data", "pumping_summary", "total_pad_volume", "actual"),
        "total_clean": ("stage_data", "pumping_summary", "total_clean_fluid_volume", "actual"),
        "acid": ("stage_data", "pumping_summary", "acid_volume", "actual"),
        "flush_volume": ("stage_data", "pumping_summary", "flush_volume", "actual"),
        "total_slurry": ("stage_data", "pumping_summary", "slurry_volume", "actual"),
        # isip: ("stage_data", "isip") disable
    }
}

PROPPANT_MAP = {
    "bulk_density": "bulk_density",
    "proppant_name": "description",
    "specific_gravity": "specific_gravity",
    "total_pumped_lbs": "amount_pumped",
}


def unpack_json_data(json_data, data_map):
    res = {}
    for base_model, data_path_map in data_map.items():
        res[base_model] = {}

        for attr, path in data_path_map.items():
            current_data_point = json_data
            for data_point in path:
                if data_point in current_data_point:
                    current_data_point = current_data_point[data_point]
                    continue
                current_data_point = {}
                break

            if current_data_point != {} and current_data_point != json_data:
                res[base_model][attr] = current_data_point
    return res


def parse_tracking_sheet_data(json_data):
    return unpack_json_data(json_data, TRACKINGSHEET_MAP)


def unpack_proppant(json_data, stage_id):
    proppants = []
    proppant_json = {"stage_id": stage_id}
    total_proppant = json_data["stage_data"]["pumping_summary"]["total_proppant"]

    for field_db, field_json in {"designed_lbs": "design"}.items():  # "actual_lbs": "actual",  removed
        if field_json in total_proppant:
            proppant_json[field_db] = total_proppant[field_json]

    for raw_proppant in json_data["stage_data"]["proppant_data"]:
        proppant = proppant_json.copy()
        for db_field, json_field in PROPPANT_MAP.items():
            proppant[db_field] = raw_proppant[json_field]
        proppants.append(proppant)
    return proppants


def unpack_active_data(json_data, stage_id=None):
    active_data = {}
    for _, data in json_data["active_data"].items():
        for field, value in data.items():
            active_data[field] = value
    for field, value in json_data["notes"].items():
        active_data[field] = value
    if stage_id:
        active_data["stage_id"] = stage_id

    for time_field in (
        "post_frac_start_time",
        "post_frac_end_time",
        "pre_frac_start_time",
        "pre_frac_end_time",
    ):
        if time_field in active_data:
            active_data[time_field] //= 1000
    return active_data


class TrackingSheetResource(Resource):
    @jwt_required()
    @swagger_decorator(
        # response_schema={200: TrackingSheetResponseSchema, 401: MessageSchema},
        path_schema=TrackingSheetUuidSchema,
        tag="Tracking Sheet",
    )
    def get(self, stage_uuid):
        """ Get Tracking sheet """
        stage = Stage.query.filter(Stage.stage_uuid == stage_uuid).first()
        if not stage or stage.well.pad.project.user_id != get_jwt_identity():
            return {"msg": "Stage not found"}, 401

        unpacking_map = {
            Stage: stage,
            ChemFluids: stage.chem_fluids,
            Perforation: stage.perforation,
            StageAVG: stage.stage_avg,
        }

        # pack stage
        response = {}
        for model, data_map in TRACKINGSHEET_MAP.items():
            for db_field, path in data_map.items():
                current_leaf = response
                for leaf in path[:-1]:
                    if leaf not in current_leaf:
                        current_leaf[leaf] = {}
                    current_leaf = current_leaf[leaf]
                last_leaf = path[-1]
                current_leaf[last_leaf] = getattr(unpacking_map[model], db_field)

        for date_field in ("stage_start_time", "stage_end_time"):
            if date_field in response["stage_data"] and response["stage_data"][date_field] is not None: 
                response["stage_data"][date_field] = int(response["stage_data"][date_field])

        active_data_map = ({
            "post_frac_pulses": ("post_frac_end_time", "post_frac_num_pulse", "post_frac_start_time"),
            "pre_frac_pulses": ("pre_frac_end_time", "pre_frac_num_pulse", "pre_frac_start_time"),
            "pulsing_parameteres": ("amplitude", "frequency", "offset", "period", "wave_type"),
        })

        active_data = {}
        for resp_field, db_fields in active_data_map.items():
            active_data[resp_field] = {}
            for field in db_fields:
                active_data[resp_field][field] = getattr(stage.active_data, field)

        response["notes"] = {}
        for field in ("additional_note", "post_frac_pulse_note", "pre_frac_pulse_note"):
            response["notes"][field] = getattr(stage.active_data, field)

        # fluids formation
        fluids_formation = []
        for fluid_item_model in stage.chem_fluids.formation_fuild_injection:
            fluid_item_data = {}
            for fluid_field in ("id", "bbls", "description", "ppg"):
                fluid_item_data[fluid_field] = getattr(fluid_item_model, fluid_field)
            fluids_formation.append(fluid_item_data)

        response["stage_data"]["fluids_injected_into_formation"] = fluids_formation

        # proppant data
        all_proppant = []
        proppant_map = {
            "proppant_name": "description",
            "total_pumped_lbs": "amount_pumped"
        }

        for proppant in stage.proppant_data:
            proppant_data = {}
            for field in ("bulk_density", "specific_gravity", "id"):
                proppant_data[field] = getattr(proppant, field)

            for db_field, json_field in proppant_map.items():
                proppant_data[json_field] = getattr(proppant, db_field)
            all_proppant.append(proppant_data)

        response["stage_data"]["pumping_summary"]["total_proppant"] = {
            "actual": stage.stage_avg.total_proppant_lbs,
            "design": stage.designed_proppant,
        }

        response["stage_data"]["proppant_data"] = all_proppant
        response["active_data"] = active_data
        return response, 200

    @jwt_required()
    @swagger_decorator(
        path_schema=TrackingSheetUuidSchema,
        json_schema=TrackingSheetUpdateSchema,
        response_schema={200: MessageSchema, 401: MessageSchema},
        tag="Tracking Sheet",
    )
    def put(self, stage_uuid):
        req = request.json
        stage = Stage.query.filter(Stage.stage_uuid == stage_uuid).first()
        if not stage or stage.well.pad.project.user_id != get_jwt_identity():
            return {"msg": "Stage not found"}, 401

        if "stage" in req and stage.stage_number != req["stage"] and Stage.query.filter(Stage.stage_number == req["stage"], Stage.well_id == stage.well_id).first():
            return {"msg": f"Stage with number: {stage.stage_number} already exist"}, 401
        # update stage
        tracking_sheet_data = parse_tracking_sheet_data(req)
        for field, value in tracking_sheet_data[Stage].items():
            setattr(stage, field, value)

        stage.save()

        # update fluids
        for field, value in tracking_sheet_data[ChemFluids].items():
            setattr(stage.chem_fluids, field, value)
        stage.chem_fluids.save()

        # updae formation_fuild_injection
        FluidModel = FormationFuildInjection
        for fluid_item in req["stage_data"]["fluids_injected_into_formation"]:
            fluid_model = FluidModel.query.filter(FluidModel.id == fluid_item["id"], FluidModel.chem_fluid_id == stage.chem_fluids.id).first()
            if fluid_model:
                del fluid_item["id"]
                for field, value in fluid_item.items():
                    setattr(fluid_model, field, value)
                fluid_model.save()

        # update proppant
        for raw_proppant in req["stage_data"]["proppant_data"]:
            proppant_id = raw_proppant["id"]
            proppant = Proppant.query.filter(Proppant.id == proppant_id, Proppant.stage_id == stage.id).first()
            if proppant:
                for db_field, json_field in PROPPANT_MAP.items():
                    setattr(proppant, db_field, raw_proppant[json_field])
                proppant.save()

        # update active_data with notes
        active_data = unpack_active_data(req)
        for field, value in active_data.items():
            setattr(stage.active_data, field, value)
        stage.active_data.save()

        # update Perforation and StageAVG
        for db_model, model_instance in ({Perforation: stage.perforation, StageAVG: stage.stage_avg}).items():
            for field, value in tracking_sheet_data[db_model].items():
                setattr(model_instance, field, value)
            model_instance.save()

        # remove proppant data and fluids
        if "remove" in req:
            for proppant_id in req["remove"]["proppant_data_ids"]:
                proppant = Proppant.query.filter(Proppant.id == proppant_id, Proppant.stage_id == stage.id).first()
                if proppant:
                    proppant.delete()

        for fluids_id in req["remove"]["fluids_injected_into_formation_ids"]:
            fluid_model = FluidModel.query.filter(FluidModel.id == fluids_id, FluidModel.chem_fluid_id == stage.chem_fluids.id).first()
            if fluid_model:
                fluid_model.delete()

        if "add" in req:
            for fluid_item in req["add"]["fluids_injected_into_formation"]:
                fluid_item["chem_fluid_id"] = stage.chem_fluids.id
                FormationFuildInjection(**fluid_item).save()

        if "add" in req and "proppant" in req["add"]:
            req["stage_data"]["proppant_data"] = req["add"]["proppant"]

        # save proppant
        for proppant_data in unpack_proppant(req, stage.id):
            Proppant(**proppant_data).save()

        total_proppant = 0
        stage = Stage.query.filter(Stage.id == stage.id).first()
        for proppant in stage.proppant_data:
            total_proppant += proppant.total_pumped_lbs

        stage.stage_avg.total_proppant_lbs = total_proppant
        stage.stage_avg.save()

        return {"msg": "Stage updated"}

    @jwt_required()
    @swagger_decorator(
        path_schema=TrackingSheetUuidSchema,
        response_schema={200: MessageSchema, 401: MessageSchema},
        tag="Tracking Sheet",
    )
    def delete(self, stage_uuid):
        stage = Stage.query.filter(Stage.stage_uuid == stage_uuid).first()
        if not stage or stage.well.pad.project.user_id != get_jwt_identity():
            return {"msg": "Stage not found"}, 401

        stage.delete()
        stage.well.save()
        return {"msg": "Stage deleted"}


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


class TrackingSheetCreateResource(Resource):
    @jwt_required()
    @swagger_decorator(
        json_schema=TrackingSheetSchema,
        path_schema=WellPathUuidSchema,
        response_schema={201: TrackingSheetCreatedSchema, 401: MessageSchema},
        tag="Tracking Sheet",
    )
    def post(self, well_uuid):
        """ Create tracking sheet """
        well = Well.query.filter(Well.well_uuid == well_uuid).first()

        if not well or well.pad.project.user_id != get_jwt_identity():
            return {"msg": f"Well with id {well_uuid} not found"}, 401

        req = request.json
        db_model_requests = {}

        for stage in well.stages:
            if stage.stage_number == req["stage"]:
                return {"msg": f"Stage with number: {stage.stage_number} already exist"}, 401

        tracking_sheet_data = parse_tracking_sheet_data(req)
        tracking_sheet_data[Stage]["well_id"] = well.id

        # save stage
        stage = Stage(**tracking_sheet_data[Stage])
        stage.save()

        if req["stage"] > well.num_stages:
            well.num_stages = req["stage"]

        well.save()

        # save fluids
        chem_fluids = ChemFluids(**tracking_sheet_data[ChemFluids])
        chem_fluids.stage_id = stage.id
        chem_fluids.save()

        for fluid_item in req["stage_data"]["fluids_injected_into_formation"]:
            fluid_item["chem_fluid_id"] = chem_fluids.id
            FormationFuildInjection(**fluid_item).save()

        # save proppant
        total_proppant_lbs = 0
        for proppant_data in unpack_proppant(req, stage.id):
            total_proppant_lbs += proppant_data["total_pumped_lbs"]
            Proppant(**proppant_data).save()

        # save active_data with notes
        active_data = unpack_active_data(req, stage.id)
        ActiveData(**active_data).save()

        # save Perforation and StageAVG
        for db_model in (Perforation, StageAVG):
            tracking_sheet_data[db_model]["stage_id"] = stage.id
            db_model_requests[db_model] = db_model(**tracking_sheet_data[db_model])
            # db_model(**tracking_sheet_data[db_model]).save()

        db_model_requests[StageAVG].total_proppant_lbs = total_proppant_lbs

        for model in db_model_requests.values():
            model.save()

        return {"msg": "tracking sheet was created", "uuid": stage.stage_uuid}, 201


# class TrackingSheetTestData(Resource):
#     @jwt_required()
#     @swagger_decorator(
#         # TODO path_schema=TrackingSheetUuidSchema,
#         response_schema={200: MessageSchema, 401: MessageSchema},
#         tag="Tracking Sheet",
#     )
#     def get(self, stage_uuid):
#         """ Get Tracking sheet """
#         stage = Stage.query.filter(Stage.stage_uuid == stage_uuid).first()
#         if not stage or stage.well.pad.project.user_id != get_jwt_identity():
#             return {"msg": "Stage not found"}, 401

#         with open("static/singlestore/test_trackingsheet_data.json", "r") as f_data:
#             data = json.load(f_data)
#             for key, value in data["stage"]["fields"].items():
#                 setattr(stage, key, value)

#             for key, value in data["stage"]["arrays"].items():
#                 array_field = getattr(stage, key)
#                 for field in array_field:
#                     for field_name, field_value in value["fields"].items():
#                         setattr(field, field_name, field_value)
#                     for field_name, field_value in value["datetime_fields"].items():
#                         setattr(field, field_name, datetime.fromtimestamp(field_value))

#         stage.save()
#         return {"msg": "Test data inserted"}
