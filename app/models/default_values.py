from app.models.mixin_models import ModelMixin, JsonModelMixin
from app import db


class DefaultVal(ModelMixin, JsonModelMixin, db.Model):

    __tablename__ = "default_val"

    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    well_id = db.Column(db.Integer, nullable=False)
    pres = db.Column(db.Float)
    young = db.Column(db.Float)
    overburden = db.Column(db.Float)
    poisson = db.Column(db.Float)
    eta_cp = db.Column(db.Integer)
    fuildt = db.Column(db.Integer)
    tect = db.Column(db.Float)
    fuild_density = db.Column(db.Float)
    diverter_time = db.Column(db.Float)
    met_res = db.Column(db.Float)
    ffkw_correction = db.Column(db.Integer)
    k_mpa = db.Column(db.Integer)
    nu_lim = db.Column(db.Integer)
    per_red = db.Column(db.Integer)
    start1 = db.Column(db.Integer)
    beta_ss = db.Column(db.Float)
    st_lim = db.Column(db.Integer)
    biot = db.Column(db.Integer)
    shadow = db.Column(db.Integer)
    fit_end_point = db.Column(db.Integer)
    NG = db.Column(db.Integer)
    breaker_YN = db.Column(db.String(30))
    passion_method = db.Column(db.Integer)
    plotraw_YN = db.Column(db.String(30))
    use_wns_YN = db.Column(db.String(30))
    fit_iteration = db.Column(db.Integer)
    strat2 = db.Column(db.Integer)
    stage_ques = db.Column(db.Integer)
    stress_shadow_YN = db.Column(db.String(30))
    skip_losses_YN = db.Column(db.String(30))
    use_wncuts_YN = db.Column(db.String(30))
    poisson_var_YN = db.Column(db.String(30))

    json_fields = (
        "pres", "young", "overburden",
        "poisson", "eta_cp", "fuildt",
        "tect", "fuild_density", "diverter_time",
        "met_res", "ffkw_correction", "k_mpa",
        "nu_lim", "per_red", "start1",
        "beta_ss", "st_lim", "biot",
        "shadow", "fit_end_point", "NG",
        "breaker_YN", "passion_method", "plotraw_YN",
        "use_wns_YN", "fit_iteration", "strat2",
        "stage_ques", "stress_shadow_YN", "skip_losses_YN",
        "use_wncuts_YN", "poisson_var_YN",
    )


class DefaultAdvanceVal(ModelMixin, JsonModelMixin, db.Model):

    __tablename__ = "default_advance_val"

    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    well_id = db.Column(db.Integer)
    model = db.Column(db.String(40))
    response = db.Column(db.String(40))
    source = db.Column(db.String(40))
    viscosity = db.Column(db.Float)
    density = db.Column(db.Float)
    compresssibility = db.Column(db.Float)
    f_low_hz = db.Column(db.Float)
    f_high_hz = db.Column(db.Float)
    new_sample_rate = db.Column(db.Float)
    data_sample_rate = db.Column(db.Float)
    algorithm = db.Column(db.String(40))
    grid_density = db.Column(db.Float)
    weighting = db.Column(db.String(10))
    wlevexp = db.Column(db.Float)
    loop = db.Column(db.String(10))
    method = db.Column(db.String(20))
    tolerance = db.Column(db.Float)
    interation = db.Column(db.Integer)
    layer = db.Column(db.Integer)
    total_width = db.Column(db.Float)

    json_fields = (
        "model", "response", "source",
        "viscosity", "density", "compresssibility",
        "f_low_hz", "f_high_hz", "new_sample_rate",
        "data_sample_rate", "algorithm", "grid_density",
        "weighting", "wlevexp", "loop",
        "method", "tolerance", "interation",
        "layer", "total_width"
    )


class DefaultParamVal(ModelMixin, JsonModelMixin, db.Model):

    __tablename__ = "default_param_val"

    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    well_id = db.Column(db.Integer)
    c1_min = db.Column(db.Float)
    c2_min = db.Column(db.Float)
    c1_max = db.Column(db.Float)
    c2_max = db.Column(db.Float)
    c3_min = db.Column(db.Float)
    c3_max = db.Column(db.Float)
    q_min = db.Column(db.Integer)
    q_max = db.Column(db.Integer)
    k_min = db.Column(db.Float)
    k_max = db.Column(db.Float)

    json_fields = (
        "c1_min", "c2_min", "c1_max",
        "c2_max", "c3_min", "c3_max",
        "q_min", "q_max", "k_min",
        "k_max",
    )
