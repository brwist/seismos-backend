from marshmallow import Schema, fields


class DeafultValueDataSchema(Schema):
    test_fields = fields.Str(required=True)


class DefaultVolumesResponseSchema(Schema):
    status = fields.Int(required=True)
    message = fields.Str(required=True)
    data = fields.Nested(DeafultValueDataSchema)


class DefaultVolumesRequestSchema(Schema):
    project_id = fields.Int(required=True)
    well_id = fields.Int(required=True)


class DefaultValueSchema(Schema):
    pres = fields.Float(required=True)
    young = fields.Float(required=True)
    overburden = fields.Float(required=True)
    poisson = fields.Float(required=True)
    eta_cp = fields.Int(required=True)
    fuildt = fields.Int(required=True)
    tect = fields.Float(required=True)
    fuild_density = fields.Float(required=True)
    diverter_time = fields.Float(required=True)
    met_res = fields.Float(required=True)
    ffkw_correction = fields.Int(required=True)
    k_mpa = fields.Int(required=True)
    nu_lim = fields.Int(required=True)
    per_red = fields.Int(required=True)
    start1 = fields.Int(required=True)
    beta_ss = fields.Float(required=True)
    st_lim = fields.Int(required=True)
    biot = fields.Int(required=True)
    shadow = fields.Int(required=True)
    fit_end_point = fields.Int(required=True)
    NG = fields.Int(required=True)
    breaker_YN = fields.String(required=True)
    passion_method = fields.Int(required=True)
    plotraw_YN = fields.String(required=True)
    use_wns_YN = fields.String(required=True)
    fit_iteration = fields.Int(required=True)
    strat2 = fields.Int(required=True)
    stage_ques = fields.Int(required=True)
    stress_shadow_YN = fields.String(required=True)
    use_wncuts_YN = fields.String(required=True)
    skip_losses_YN = fields.String(required=True)
    poisson_var_YN = fields.String(required=True)


class DefaultAdvanceVal(Schema):
    model = fields.String(required=True)
    response = fields.String(required=True)
    source = fields.String(required=True)
    viscosity = fields.Float(required=True)
    density = fields.Float(required=True)
    compresssibility = fields.Float(required=True)
    f_low_hz = fields.Float(required=True)
    f_high_hz = fields.Float(required=True)
    new_sample_rate = fields.Float(required=True)
    data_sample_rate = fields.Float(required=True)
    algorithm = fields.String(required=True)
    grid_density = fields.Float(required=True)
    weighting = fields.String(required=True)
    wlevexp = fields.Float(required=True)
    loop = fields.String(required=True)
    method = fields.String(required=True)
    tolerance = fields.Float(required=True)
    interation = fields.Int(required=True)
    layer = fields.Int(required=True)
    total_width = fields.Int(required=True)


class DefaultParamVal(Schema):
    c1_min = fields.Float(required=True)
    c2_min = fields.Float(required=True)
    c1_max = fields.Float(required=True)
    c2_max = fields.Float(required=True)
    c3_min = fields.Float(required=True)
    c3_max = fields.Float(required=True)
    q_min = fields.Int(required=True)
    q_max = fields.Int(required=True)
    k_min = fields.Float(required=True)
    k_max = fields.Float(required=True)


class DefaultValuesSchema(Schema):
    default_value = fields.Nested(DefaultValueSchema)
    default_advance_val = fields.Nested(DefaultAdvanceVal)
    default_param_val = fields.Nested(DefaultParamVal)
