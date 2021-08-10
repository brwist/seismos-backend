from marshmallow import Schema, fields


class PerfInterInfoDisplacementSchema(Schema):
    top_perf = fields.String()
    bottom_perf = fields.String()
    plug = fields.String()


class PerforationIntervalInformation(Schema):
    top_perf = fields.String()
    bottom_perf = fields.String()
    plug_depth = fields.String()
    n_clusters = fields.Int()
    perf_gun_description = fields.String()
    perf_daiameter = fields.String()
    spf = fields.String()
    pumped_diverter = fields.String()
    diverter_type = fields.String()
    acid = fields.String()
    displacement_volume = fields.Nested(PerfInterInfoDisplacementSchema)


class FieldEngineerSchema(Schema):
    days = fields.String()
    nights = fields.String()


class StageTrackingShema(Schema):
    date = fields.Int()
    customer = fields.String()
    well = fields.String()
    stage = fields.String()
    bht_f = fields.String()
    bht_psi = fields.String()
    frac_design = fields.String()
    field_engineer = fields.Nested(FieldEngineerSchema)
    plug_type = fields.String()
    plug_seat_technique = fields.String()
    did_an_event_occur = fields.String()
    seismos_data_collection = fields.String()


class StageDataFluidParam(Schema):
    base_fluid_type = fields.String()
    base_fluid_density = fields.String()
    max_conc_density = fields.String()


class FluidsInjected(Schema):
    description = fields.String()
    bbls = fields.String()
    ppg = fields.String()


class FluidsInjectedIntoFormation(Schema):
    last = fields.Nested(FluidsInjected)
    second_to_last = fields.Nested(FluidsInjected)
    third_to_last = fields.Nested(FluidsInjected)


class PropantDataSchema(Schema):
    description = fields.String()
    specific_gravity = fields.String()
    bulk_density = fields.String()


class PumpingSummaryValuesSchema(Schema):
    design = fields.String()
    actual = fields.String()


class PumpingSummarySchema(Schema):
    max_prop_conc = fields.Nested(PumpingSummaryValuesSchema)
    total_pad_volume = fields.Nested(PumpingSummaryValuesSchema)
    total_clean_fluid_volume = fields.Nested(PumpingSummaryValuesSchema)
    total_forty_seventy = fields.Nested(PumpingSummaryValuesSchema)
    total_sand = fields.Nested(PumpingSummaryValuesSchema)
    acid_volume = fields.Nested(PumpingSummaryValuesSchema)
    flush_volume = fields.Nested(PumpingSummaryValuesSchema)
    slurry_volume = fields.Nested(PumpingSummaryValuesSchema)


class PilsingParameters(Schema):
    wave_type = fields.String()
    periods = fields.String()
    freq = fields.String()
    offset = fields.String()
    amplitude = fields.String()


class FracPulsesSchema(Schema):
    start_time = fields.Int()
    end_time = fields.Int()
    n_pulses = fields.Int()


class StageDataSchema(Schema):
    stage_start_time = fields.Int()
    stage_end_time = fields.Int()
    opening_well = fields.String()
    isip = fields.String()
    fluid_parameters = fields.Nested(StageDataFluidParam)
    fluids_injected_into_formation = fields.Nested(FluidsInjectedIntoFormation)
    propant_data = fields.List(fields.Nested(PropantDataSchema))
    pumping_summary = fields.Nested(PumpingSummarySchema)


class TrackingSheetActiveData(Schema):
    pilsing_parameters = fields.Nested(PilsingParameters)
    pre_frac_pulses = fields.Nested(FracPulsesSchema)
    post_frac_pulses = fields.Nested(FracPulsesSchema)


class TrackingSheetNotes(Schema):
    pre_frac_pulse = fields.String()
    post_frac_pulse = fields.String()
    other = fields.String()


class TrackingSheetSchema(Schema):
    stage = fields.Int()
    stage_tracking = fields.Nested(StageTrackingShema)
    perforation_interval_information = fields.Nested(PerforationIntervalInformation)
    stage_data = fields.Nested(StageDataSchema)
    active_data = fields.Nested(TrackingSheetActiveData)
    notes = fields.Nested(TrackingSheetNotes)


class TrackingSheetIdSchema(Schema):
    tracking_sheet_id = fields.Str(required=True)


class TrackingSheetStageSchema(Schema):
    stage = fields.Str(required=True)


class TrackingSheetStageIdSchema(Schema):
    stage = fields.Int()
    sheet_id = fields.Int()


class TrackingSheetStagesListResponse(Schema):
    stages = fields.List(fields.Nested(TrackingSheetStageIdSchema))
