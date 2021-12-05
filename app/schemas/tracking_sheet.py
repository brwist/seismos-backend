from marshmallow import Schema, fields


class PerfInterInfoDisplacementSchema(Schema):
    top_perf = fields.Float()
    bottom_perf = fields.Float()
    plug = fields.String()


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
    acid = fields.Float()
    displacement_volume = fields.Nested(PerfInterInfoDisplacementSchema)


class StageTrackingShema(Schema):
    bottomhole_bht = fields.Float()
    bottomhole_bhp = fields.Float()
    frac_design = fields.String()
    plug_type = fields.String()
    plug_seat_technique = fields.String()
    did_an_event_occur = fields.String()
    seismos_data_collection = fields.String()


class QCStageDataShema(Schema):
    stage_n = fields.Int()
    stage_tracking = fields.Nested(StageTrackingShema)


class QCReportSchema(Schema):
    report = fields.List(fields.Nested(QCStageDataShema))


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
    specific_gravity = fields.String()
    bulk_density = fields.String()
    amount_pumped = fields.Float()


class PumpingSummaryValuesSchema(Schema):
    design = fields.Float()
    actual = fields.Float()


class PumpingSummarySchema(Schema):
    max_prop_conc = fields.Nested(PumpingSummaryValuesSchema)
    total_pad_volume = fields.Nested(PumpingSummaryValuesSchema)
    total_clean_fluid_volume = fields.Nested(PumpingSummaryValuesSchema)
    # proppant = fields.Nested(PumpingSummaryValuesSchema)
    total_proppant = fields.Nested(PumpingSummaryValuesSchema)
    acid_volume = fields.Nested(PumpingSummaryValuesSchema)
    flush_volume = fields.Nested(PumpingSummaryValuesSchema)
    slurry_volume = fields.Nested(PumpingSummaryValuesSchema)


class PulsingParameters(Schema):
    wave_type = fields.String()
    period = fields.Int()
    freq = fields.Float()
    offset = fields.Int()
    amplitude = fields.Int()


class FracPulsesSchema(Schema):
    start_time = fields.Int()
    end_time = fields.Int()
    n_pulses = fields.Int()


class StageDataSchema(Schema):
    stage_start_time = fields.Int()
    stage_end_time = fields.Int()
    opening_well = fields.Int()
    # isip = fields.Float()
    fluid_parameters = fields.Nested(StageDataFluidParam)
    fluids_injected_into_formation = fields.List(fields.Nested(FluidsInjected))
    proppant_data = fields.List(fields.Nested(ProppantDataSchema))
    pumping_summary = fields.Nested(PumpingSummarySchema)


class StageDataCreateSchema(Schema):
    stage = fields.Int()
    stage_data = fields.Nested(StageDataSchema)


class TrackingSheetNotes(Schema):
    pre_frac_pulses = fields.String()
    post_frac_pulses = fields.String()
    other = fields.String()


class PulsingParameters(Schema):
    wave_type = fields.String()
    frequency = fields.Float()
    amplitude = fields.Integer()
    period = fields.Integer()
    offset = fields.Integer()


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


class TrackingSheetStageSchema(Schema):
    stage = fields.Str(required=True)


class TrackingSheetStageIdSchema(Schema):
    uuid = fields.String()
    stage_n = fields.Int()


class TrackingSheetStagesListResponse(Schema):
    stages = fields.List(fields.Nested(TrackingSheetStageIdSchema))


class StagesUuidsSchema(Schema):
    stage_uuids = fields.List(fields.UUID)


class StageDataUpdateSchema(Schema):
    stage_start_time = fields.Int()
    stage_end_time = fields.Int()
    plug_depth = fields.Float()
    pumping_fluid_density = fields.Float()
    pumping_fluid_type = fields.Str()
    number_of_cluster = fields.Int()
    bottomhole_bht = fields.Float()
    bottomhole_bhp = fields.Float()
    diverter_type = fields.Str()
    plug_name = fields.Str()
    pumped_diverter = fields.Str()
    spf = fields.Str()
    stage_event = fields.Str()
    designed_acid_vol = fields.Float()
    designed_flush_vol = fields.Float()
    designed_max_prop = fields.Float()
    designed_slurry_vol = fields.Float()
    designed_total_clean_fluid_vol = fields.Float()
    designed_pad_vol = fields.Float()
    frac_design = fields.Str()
    plug_seat_technique = fields.Str()
    plug_type = fields.Str()
    data_collection = fields.Str()


class StageChemFluidsSchema(Schema):
    acid = fields.Float()
    base_fluid_density = fields.Float()
    base_fluid_type = fields.Str()
    max_conc_density = fields.Float()


class StagePerforationSchema(Schema):
    bottom_measured_depth = fields.Float()
    top_measured_depth = fields.Float()
    estimated_hole_diameter = fields.Float()
    perf_gun_description = fields.Str()
    bottom_perf = fields.Float()
    top_perf = fields.Float()


class StageAvgSchema(Schema):
    # isip = fields.Float()
    open_well_pressure = fields.Float()
    acid = fields.Float()
    max_prop_conc = fields.Float()
    total_slurry = fields.Float()
    total_clean = fields.Float()
    pad_vol = fields.Str()
    flush_volume = fields.Float()


class UpdateStageSchema(Schema):
    stage = fields.Nested(StageDataUpdateSchema)
    chem_fluids = fields.Nested(StageChemFluidsSchema)
    perforation = fields.Nested(StagePerforationSchema)
    stage_avg = fields.Nested(StageAvgSchema)
