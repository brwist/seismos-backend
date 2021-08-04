from marshmallow import Schema, fields


class DeafultValueDataSchema(Schema):
    test_fields = fields.Str()


class DefaultVolumesResponseSchema(Schema):
    status = fields.Int()
    message = fields.Str()
    data = fields.Nested(DeafultValueDataSchema)


class DefaultVolumesRequestSchema(Schema):
    project_id = fields.Int()
    well_id = fields.Int()


class DefaultVolumesSchema(Schema):
    field_engineer = fields.String()
    bht_temp = fields.String()
    bhp_temp = fields.String()
    frac_design = fields.String()
    plug_type = fields.String()
    plug_seat_technique = fields.String()
    n_clusters = fields.Int()
    perf_gun = fields.String()
    description = fields.String()
    perf_diameter = fields.String()
    spf = fields.String()
    field = fields.String()
    acid = fields.String()
    base = fields.String()
    fluid_type = fields.String()
    proppant_data = fields.String()
    pulsing_parameters = fields.String()
    pumping_summary = fields.String()
