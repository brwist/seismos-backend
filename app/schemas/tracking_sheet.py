from marshmallow import Schema, fields


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
    displacement_volume = fields.Nested(PerfInterInfoDisplacementSchema)


class StageTrackingShema(Schema):
    bottomhole_bht = fields.Float()
    bottomhole_bhp = fields.Float()
    frac_design = fields.String()
    plug_type = fields.String()
    plug_seat_technique = fields.String()
    did_an_event_occur = fields.String()
    seismos_data_collection = fields.String()


# # class QCStageDataShema(Schema):
# #     stage_n = fields.Int()
# #     stage_tracking = fields.Nested(StageTrackingShema)


# # class QCReportSchema(Schema):
# #     report = fields.List(fields.Nested(QCStageDataShema))


class StageDataFluidParam(Schema):
    base_fluid_type = fields.String()
    base_fluid_density = fields.Float()
    max_conc_density = fields.Float()


class FluidsInjected(Schema):
    description = fields.String()
    bbls = fields.Integer()
    ppg = fields.Float()


class ProppantDataSchema(Schema):
    description = fields.String()
    specific_gravity = fields.Float()
    bulk_density = fields.Integer()
    amount_pumped = fields.Float()


class PumpingSummaryValuesSchema(Schema):
    design = fields.Float()
    actual = fields.Float()


class PumpingSummarySchema(Schema):
    max_prop_conc = fields.Nested(PumpingSummaryValuesSchema)
    total_pad_volume = fields.Nested(PumpingSummaryValuesSchema)
    total_clean_fluid_volume = fields.Nested(PumpingSummaryValuesSchema)
    proppant = fields.Nested(PumpingSummaryValuesSchema)
    total_proppant = fields.Nested(PumpingSummaryValuesSchema)
    acid_volume = fields.Nested(PumpingSummaryValuesSchema)
    flush_volume = fields.Nested(PumpingSummaryValuesSchema)
    slurry_volume = fields.Nested(PumpingSummaryValuesSchema)


class PulsingParameters(Schema):
    wave_type = fields.String()
    frequency = fields.Float()
    amplitude = fields.Integer()
    period = fields.Integer()
    offset = fields.Integer()


# class FracPulsesSchema(Schema):
#     start_time = fields.Int()
#     end_time = fields.Int()
#     n_pulses = fields.Int()


class StageDataSchema(Schema):
    stage_start_time = fields.Int()
    stage_end_time = fields.Int()
    opening_well = fields.Int()
    # isip = fields.Float()
    fluid_parameters = fields.Nested(StageDataFluidParam)
    fluids_injected_into_formation = fields.List(fields.Nested(FluidsInjected))
    proppant_data = fields.List(fields.Nested(ProppantDataSchema))
    pumping_summary = fields.Nested(PumpingSummarySchema)


# # class StageDataCreateSchema(Schema):
# #     stage = fields.Int()
# #     stage_data = fields.Nested(StageDataSchema)


# class TrackingSheetNotes(Schema):
#     pre_frac_pulses = fields.String()
#     post_frac_pulses = fields.String()
#     other = fields.String()


class PreFracPulsesSchema(Schema):
    pre_frac_start_time = fields.Integer()
    pre_frac_end_time = fields.Integer()
    pre_frac_num_pulse = fields.Integer()


class PostFracPulsesSchema(Schema):
    post_frac_start_time = fields.Integer()
    post_frac_end_time = fields.Integer()
    post_frac_num_pulse = fields.Integer()


class ActiveDataSchema(Schema):
    pulsing_parameteres = fields.Nested(PulsingParameters)
    pre_frac_pulses = fields.Nested(PreFracPulsesSchema)
    post_frac_pulses = fields.Nested(PostFracPulsesSchema)


class NotesSchema(Schema):
    pre_frac_pulse_note = fields.String()
    post_frac_pulse_note = fields.String()
    additional_note = fields.String()


class TrackingSheetSchema(Schema):
    stage = fields.Int()
    stage_tracking = fields.Nested(StageTrackingShema)
    perforation_interval_information = fields.Nested(PerforationIntervalInformation)
    stage_data = fields.Nested(StageDataSchema)
    active_data = fields.Nested(ActiveDataSchema)
    notes = fields.Nested(NotesSchema)


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
    remove = fields.Nested(RemoveTrackingSheetDataSchema)
    add = fields.Nested(AddProppantFluidsSchema)
