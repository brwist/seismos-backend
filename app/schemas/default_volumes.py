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


class DefaultValueSchema(Schema):
    pres = fields.Float()
    young = fields.Float()
    overburden = fields.Float()
    poisson = fields.Float()
    eta_cp = fields.Int()
    fuildt = fields.Int()
    tect = fields.Float()
    fuild_density = fields.Float()
    diverter_time = fields.Float()
    met_res = fields.Float()
    ffkw_correction = fields.Int()
    k_mpa = fields.Int()
    nu_lim = fields.Int()
    per_red = fields.Int()
    start1 = fields.Int()
    beta_ss = fields.Float()
    st_lim = fields.Int()
    biot = fields.Int()
    shadow = fields.Int()
    fit_end_point = fields.Int()
    start2 = fields.Int()
    ng = fields.Int()
    stage_ques = fields.String()
    breaker = fields.String()
    poisson_var = fields.String()
    poisson_method = fields.Int()
    stress_shadow = fields.String()
    plotraw = fields.String()
    skip_losses = fields.String()
    use_wns = fields.String()
    use_wncuts = fields.String()
    fit_iterations = fields.Int()


class DefaultAdvanceVal(Schema):
    model = fields.String()
    response = fields.String()
    source = fields.String()
    layer = fields.Int()
    total_width = fields.Float()
    viscosity = fields.Float()
    density = fields.Float()
    compresssibility = fields.Float()
    f_low_hz = fields.Float()
    f_high_hz = fields.Float()
    new_sample_rate = fields.Float()
    data_sample_rate = fields.Float()
    algorithm = fields.String()
    grid_density = fields.Float()
    weighting = fields.String()
    wlevexp = fields.Float()
    loop = fields.String()
    method = fields.String()
    tolerance = fields.Float()
    interation = fields.Int()


class DefaultParamVal(Schema):
    c1_min = fields.Float()
    c2_min = fields.Float()
    c1_max = fields.Float()
    c2_max = fields.Float()
    c3_min = fields.Float()
    c3_max = fields.Float()
    q_min = fields.Int()
    q_max = fields.Int()
    k_min = fields.Float()
    k_max = fields.Float()


class DefaultVolumesSchema(Schema):
    default_value = fields.Nested(DefaultValueSchema)
    default_advance_val = fields.Nested(DefaultAdvanceVal)
    default_param_val = fields.Nested(DefaultParamVal)
