from marshmallow import Schema, fields
from .base import MessageSchema


class PerfInterInfoDisplacementSchema(Schema):
    top_perf = fields.Float()
    bottom_perf = fields.Float()
    plug = fields.Float()


class PerforationIntervalInformation(Schema):
    top_measured_depth = fields.Float()
    bottom_measured_depth = fields.Float()
    plug_depth = fields.Float()
    n_clusters = fields.Int()
    perf_gun_description = fields.String()
    perf_daiameter = fields.Float()
    spf = fields.Int()
    pumped_diverter = fields.String()
    diverter_type = fields.String()
    acid = fields.String()
    displacement_volume = fields.Nested(PerfInterInfoDisplacementSchema, required=True)


class StageTrackingShema(Schema):
    bottomhole_bht = fields.Float()
    bottomhole_bhp = fields.Float()
    frac_design = fields.String()
    plug_type = fields.String()
    plug_seat_technique = fields.String()
    did_an_event_occur = fields.String()
    seismos_data_collection = fields.String()


class StageDataFluidParam(Schema):
    base_fluid_type = fields.String()
    base_fluid_density = fields.Float()
    max_conc_density = fields.Float()


class FluidsInjected(Schema):
    id = fields.Int()
    description = fields.String()
    bbls = fields.Integer()
    ppg = fields.Float()


class ProppantDataSchema(Schema):
    id = fields.Int()
    description = fields.String()
    specific_gravity = fields.Float()
    bulk_density = fields.Integer()
    amount_pumped = fields.Float()


class PumpingSummaryValuesSchema(Schema):
    design = fields.Float()
    actual = fields.Float()


class PumpingSummarySchema(Schema):
    max_prop_conc = fields.Nested(PumpingSummaryValuesSchema, required=True)
    total_pad_volume = fields.Nested(PumpingSummaryValuesSchema, required=True)
    total_clean_fluid_volume = fields.Nested(PumpingSummaryValuesSchema, required=True)
    total_proppant = fields.Nested(PumpingSummaryValuesSchema, required=True)
    acid_volume = fields.Nested(PumpingSummaryValuesSchema, required=True)
    flush_volume = fields.Nested(PumpingSummaryValuesSchema, required=True)
    slurry_volume = fields.Nested(PumpingSummaryValuesSchema, required=True)


class PulsingParameters(Schema):
    wave_type = fields.String()
    frequency = fields.Float()
    amplitude = fields.Integer()
    period = fields.Integer()
    offset = fields.Integer()


class StageDataSchema(Schema):
    stage_start_time = fields.Integer()
    stage_end_time = fields.Integer()
    opening_well = fields.Int()
    # isip = fields.Float()
    fluid_parameters = fields.Nested(StageDataFluidParam, required=True)
    fluids_injected_into_formation = fields.List(
        fields.Nested(FluidsInjected), required=True
    )
    proppant_data = fields.List(fields.Nested(ProppantDataSchema), required=True)
    pumping_summary = fields.Nested(PumpingSummarySchema, required=True)


class PreFracPulsesSchema(Schema):
    pre_frac_start_time = fields.Integer()
    pre_frac_end_time = fields.Integer()
    pre_frac_num_pulse = fields.Integer()


class PostFracPulsesSchema(Schema):
    post_frac_start_time = fields.Integer()
    post_frac_end_time = fields.Integer()
    post_frac_num_pulse = fields.Integer()


class ActiveDataSchema(Schema):
    pulsing_parameteres = fields.Nested(PulsingParameters, required=True)
    pre_frac_pulses = fields.Nested(PreFracPulsesSchema, required=True)
    post_frac_pulses = fields.Nested(PostFracPulsesSchema, required=True)


class NotesSchema(Schema):
    pre_frac_pulse_note = fields.String()
    post_frac_pulse_note = fields.String()
    additional_note = fields.String()


class TrackingSheetSchema(Schema):
    stage = fields.Int(required=True)
    stage_tracking = fields.Nested(StageTrackingShema, required=True)
    perforation_interval_information = fields.Nested(
        PerforationIntervalInformation, required=True
    )
    stage_data = fields.Nested(StageDataSchema, required=True)
    active_data = fields.Nested(ActiveDataSchema, required=True)
    notes = fields.Nested(NotesSchema, required=True)


class TrackingSheetUuidSchema(Schema):
    stage_uuid = fields.UUID(required=True)


class TrackingSheetStageIdSchema(Schema):
    uuid = fields.String()
    stage_n = fields.Int()


class TrackingSheetStagesListResponse(Schema):
    stages = fields.List(fields.Nested(TrackingSheetStageIdSchema))


class StagesUuidsSchema(Schema):
    stage_uuids = fields.List(fields.UUID)


class FluidsInjectedResponse(FluidsInjected):
    id = fields.Integer(required=True)


class ProppantDataResponseSchema(ProppantDataSchema):
    id = fields.Integer(required=True)


class StageDataResponseSchema(StageDataSchema):
    fluids_injected_into_formation = fields.List(fields.Nested(FluidsInjectedResponse))
    proppant_data = fields.List(fields.Nested(ProppantDataResponseSchema))


class TrackingSheetResponseSchema(TrackingSheetSchema):
    stage_data = fields.Nested(StageDataResponseSchema)


class RemoveTrackingSheetDataSchema(Schema):
    proppant_data_ids = fields.List(fields.Integer())
    fluids_injected_into_formation_ids = fields.List(fields.Integer())


class AddProppantFluidsSchema(Schema):
    proppant = fields.List(fields.Nested(ProppantDataSchema))
    fluids_injected_into_formation = fields.List(fields.Nested(FluidsInjected))


class TrackingSheetUpdateSchema(TrackingSheetResponseSchema):
    stage = fields.Int()
    stage_tracking = fields.Nested(StageTrackingShema)
    perforation_interval_information = fields.Nested(PerforationIntervalInformation)
    stage_data = fields.Nested(StageDataSchema)
    active_data = fields.Nested(ActiveDataSchema)
    notes = fields.Nested(NotesSchema)
    remove = fields.Nested(RemoveTrackingSheetDataSchema)


class TrackingSheetCreatedSchema(MessageSchema):
    uuid = fields.String()
