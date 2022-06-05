from datetime import datetime
from sqlalchemy.dialects.mysql import JSON, TINYINT
from app.models.mixin_models import (
    TimestampMixin,
    ModelMixin,
    JsonModelMixin,
    uuid_string,
)
from app import db


class QCReportDataModel:
    def generate_report(self, include_none=False):
        result = {}

        if not include_none:
            for field in self.to_report:
                result[field] = getattr(self, field)
        else:
            for field in self.to_report:
                value = getattr(self, field)
                if value is not None:
                    result[field] = value

        return result


class Stage(TimestampMixin, ModelMixin, db.Model, QCReportDataModel):
    __tablename__ = "stage"

    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    stage_uuid = db.Column(db.String(36), nullable=False, default=uuid_string)
    well_id = db.Column(db.Integer)
    stage_number = db.Column(db.Integer)
    number_of_cluster = db.Column(db.Integer, default=0)
    stage_start_time = db.Column(db.DateTime)
    stage_end_time = db.Column(db.DateTime)
    plug_depth = db.Column(db.Float)
    calc_net_pressure_result = db.Column(db.Float)
    observed_net_pressure = db.Column(db.Float)
    inline_density = db.Column(db.Float)
    blender_density = db.Column(db.Float)
    calc_bh_density = db.Column(db.Float)
    bottomhole_bhp = db.Column(db.Float)
    bottomhole_bht = db.Column(db.Float)
    frac_model_bhp = db.Column(db.Float)
    total_pumpdown_volume = db.Column(db.Float)
    poisson_ratio = db.Column(db.Float)
    pr_gradient = db.Column(db.Float)
    overburden_num = db.Column(db.Float)
    pumping_fluid_viscosity = db.Column(db.Float)
    pumping_fluid_density = db.Column(db.Float)
    pumping_fluid_type = db.Column(db.Text)
    tectonic_gradient = db.Column(db.Float)
    pore_pressure = db.Column(db.Float)
    sleeve_name = db.Column(db.Text)
    sleeve_ordinal = db.Column(db.Integer)
    sleeve_top_measured_depth = db.Column(db.Float)
    sleeve_bottom_measured_depth = db.Column(db.Float)
    sleeve_depth_unit = db.Column(db.Text)
    sleeve_port_size = db.Column(db.Float)
    sleeve_port_size_unit = db.Column(db.Text)
    sleeve_ball_size = db.Column(db.Float)
    sleeve_ball_size_unit = db.Column(db.Text)
    sleeve_seat_id = db.Column(db.Text)
    sleeve_manufacturer = db.Column(db.Text)
    sleeve_model = db.Column(db.Text)
    sleeve_toe_shift_pressure = db.Column(db.Integer)
    sleeve_toe_burst_pressure = db.Column(db.Integer)
    additional = db.Column(JSON)
    is_approved = db.Column(TINYINT, default=0)
    diverter_type = db.Column(db.String(255))
    pumped_diverter = db.Column(db.String(255))
    spf = db.Column(db.String(255))
    stage_event = db.Column(db.String(255))
    designed_acid_vol = db.Column(db.Float)
    designed_flush_vol = db.Column(db.Float)
    designed_max_prop = db.Column(db.Float)
    designed_slurry_vol = db.Column(db.Float)
    designed_total_clean_fluid_vol = db.Column(db.Float)
    designed_proppant = db.Column(db.Float)
    designed_pad_vol = db.Column(db.Float)
    frac_design = db.Column(db.String(255))
    plug_seat_technique = db.Column(db.String(255))
    plug_type = db.Column(db.String(255))
    plug_name = db.Column(db.String(50))
    data_collection = db.Column(db.String(255))
    is_acid = db.Column(db.String(55))
    # displacement
    top_perf_Displacement_volume = db.Column(db.Float)
    bottom_perf_Displacement_volume = db.Column(db.Float)
    plug_displacement_volume = db.Column(db.Float)

    # well = db.relationship(
    #     "Well",
    #     foreign_keys=[well_id],
    #     primaryjoin="Well.id == Stage.well_id",
    # )

    nf_processing_result = db.relationship(
        "NFProcessingResult",
        foreign_keys=[id],
        primaryjoin="Stage.id == NFProcessingResult.stage_id",
        cascade="all,delete",
    )

    stage_avg = db.relation(
        "StageAVG",
        foreign_keys=[id],
        primaryjoin="Stage.id == StageAVG.stage_id",
        cascade="all,delete",
    )

    ff_processing_result = db.relation(
        "FFProcessingResult",
        foreign_keys=[id],
        primaryjoin="Stage.id == FFProcessingResult.stage_id",
        cascade="all,delete",
    )

    chem_fluids = db.relation(
        "ChemFluids",
        foreign_keys=[id],
        primaryjoin="Stage.id == ChemFluids.stage_id",
        cascade="all,delete",
    )

    perforation = db.relation(
        "Perforation",
        foreign_keys=[id],
        primaryjoin="Stage.id == Perforation.stage_id",
        cascade="all,delete",
    )

    proppant_data = db.relation(
        "Proppant",
        foreign_keys=[id],
        primaryjoin="Stage.id == Proppant.stage_id",
        uselist=True,
        cascade="all,delete",
    )

    active_data = db.relation(
        "ActiveData",
        primaryjoin="Stage.id == ActiveData.stage_id",
        foreign_keys=[id],
        cascade="all,delete",
    )

    to_report = [
        "stage_number",
        "number_of_cluster",
        "stage_start_time",
        "stage_end_time",
    ]

    def generate_report(self, include_none=False):
        report = super().generate_report(include_none)
        report["stage_start_time"] = datetime.fromtimestamp(report["stage_start_time"])
        report["stage_end_time"] = datetime.fromtimestamp(report["stage_end_time"])
        return report

    def to_json(self):
        data = {
            "stage": {},
        }

        for field in self.json_fields:
            value = getattr(self, field)
            if value is not None:
                data["stage"][field] = value

        return data


class NFProcessingResult(
    TimestampMixin, ModelMixin, db.Model, QCReportDataModel, JsonModelMixin
):
    __tablename__ = "nf_processing_result"

    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    stage_id = db.Column(db.Integer, nullable=False)
    timestamp = db.Column(db.DateTime)
    user_id = db.Column(db.Text)
    c0 = db.Column(db.Float)
    c1 = db.Column(db.Float)
    c2 = db.Column(db.Float)
    c3 = db.Column(db.Float)
    q0 = db.Column(db.Float)
    q1 = db.Column(db.Float)
    q2 = db.Column(db.Float)
    q3 = db.Column(db.Float)
    fit_error = db.Column(db.Float)
    nf_param_id = db.Column(db.Integer)
    connect_ops_risk = db.Column(db.Float)
    connect_efficiency = db.Column(db.Float)
    connect_condition = db.Column(db.Float)

    to_report = [
        "c0",
        "c1",
        "c2",
        "c3",
        "q0",
        "q1",
        "q2",
        "q3",
        "fit_error",
        "nf_param_id",
        "connect_ops_risk",
        "connect_efficiency",
        "connect_condition",
    ]

    json_fields = (
        "timestamp",
        "user_id",
        "c0",
        "c1",
        "c2",
        "c3",
        "q0",
        "q1",
        "q2",
        "q3",
        "fit_error",
        "nf_param_id",
        "connect_ops_risk",
        "connect_efficiency",
        "connect_condition",
    )


class StageAVG(TimestampMixin, ModelMixin, db.Model, QCReportDataModel, JsonModelMixin):
    __tablename__ = "stage_avg"

    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    stage_id = db.Column(db.Integer, nullable=False)
    breakdown_pressure = db.Column(db.Float)
    isip = db.Column(db.Float)
    frac_gradient = db.Column(db.Float)
    diverter = db.Column(db.Float)
    acid = db.Column(db.Float)
    open_well_pressure = db.Column(db.Float)
    isip_5min = db.Column(db.Float)
    isip_10min = db.Column(db.Float)
    isip_15min = db.Column(db.Float)
    time_to_max_rate = db.Column(db.Float)
    avg_pressure = db.Column(db.Float)
    max_pressure = db.Column(db.Float)
    slickwater_volume = db.Column(db.Float)
    total_slurry = db.Column(db.Float)
    total_clean = db.Column(db.Float)
    total_proppant_lbs = db.Column(db.Float)
    avg_rate = db.Column(db.Float)
    max_rate = db.Column(db.Float)
    mesh_100 = db.Column("100_mesh", db.Float)
    mesh_30_50 = db.Column("30_50_mesh", db.Float)
    mesh_40_70 = db.Column("40_70_mesh", db.Float)
    mesh_20_40 = db.Column("20_40_mesh", db.Float)
    micro_prop = db.Column(db.Float)
    friction_reducer = db.Column(db.Float)
    gel = db.Column(db.Float)
    crosslink = db.Column(db.Float)
    additional = db.Column(JSON)
    flush_volume = db.Column(db.Float)
    max_prop_conc = db.Column(db.Float)
    pad_vol = db.Column(db.Integer)

    opening_well = db.Column(db.Integer)
    to_report = [
        "breakdown_pressure",
        "isip",
        "frac_gradient",
        "diverter",
        "acid",
        "opening_well",
        "isip_5min",
        "isip_10min",
        "isip_15min",
        "time_to_max_rate",
        "mesh_100",
        "mesh_30_50",
        "mesh_40_70",
        "mesh_20_40",
        "micro_prop",
        "friction_reducer",
        "gel",
        "crosslink",
    ]

    json_fields = (
        "breakdown_pressure",
        "isip",
        "frac_gradient",
        "diverter",
        "acid",
        "open_well_pressure",
        "isip_5min",
        "isip_10min",
        "isip_15min",
        "time_to_max_rate",
        "avg_pressure",
        "max_pressure",
        "slickwater_volume",
        "total_slurry",
        "total_clean",
        "avg_rate",
        "max_rate",
        "mesh_100",
        "mesh_30_50",
        "mesh_40_70",
        "mesh_20_40",
        "micro_prop",
        "friction_reducer",
        "gel",
        "crosslink",
        "additional",
        "pad_vol",
        "flush_volume",
        "max_prop_conc",
        "pad_vol",
    )


class FFProcessingResult(TimestampMixin, ModelMixin, db.Model, QCReportDataModel):
    __tablename__ = "ff_processing_result"

    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime)
    length = db.Column(db.Float)
    width = db.Column(db.Float)
    height = db.Column(db.Float)
    conductivity = db.Column(db.Float)
    minimum_stress = db.Column(db.Float)
    minimun_stress_gradient = db.Column(db.Float)
    net_pressure = db.Column(db.Float)
    fracture_pressure_gradient = db.Column(db.Float)
    reservoir_pressure = db.Column(db.Float)
    reservoir_pressure_gradient = db.Column(db.Float)
    pressure_match = db.Column(db.Float)
    fracture_efficiency = db.Column(db.Float)
    stress_shadow_pressure = db.Column(db.Float)
    calculated_poisson_ratio = db.Column(db.Float)
    stage_id = db.Column(db.Integer)
    ff_parameter_id = db.Column(db.Integer)
    nwb_region_size = db.Column(db.Float)
    nwb_compressibility = db.Column(db.Float)
    ff_version = db.Column(db.Text)
    unit = db.Column(db.Text)

    to_report = [
        "length",
        "width",
        "height",
        "conductivity",
        "minimum_stress",
        "minimun_stress_gradient",
        "net_pressure",
        "fracture_pressure_gradient",
        "reservoir_pressure",
        "reservoir_pressure_gradient",
        "pressure_match",
        "fracture_efficiency",
        "stress_shadow_pressure",
        "calculated_poisson_ratio",
        "stage_id",
        "ff_parameter_id",
        "nwb_region_size",
        "nwb_compressibility",
        "ff_version",
        "unit",
    ]


class Slurry(TimestampMixin, ModelMixin, db.Model):

    __tablename__ = "slurry"

    id = db.Column(db.BigInteger, autoincrement=True, primary_key=True)
    stage_id = db.Column(db.Integer, nullable=False)
    total_slurry_rate = db.Column(db.Float)


class TreatingPressure(TimestampMixin, ModelMixin, db.Model):

    __tablename__ = "treating_pressure"

    id = db.Column(db.BigInteger, autoincrement=True, primary_key=True)
    stage_id = db.Column(db.Integer, nullable=False)
    wellhead_pressure = db.Column(db.Float)
    treating_pressure = db.Column(db.Float)
    annulus_pressure = db.Column(db.Float)
    calc_hydrostatic_pressure = db.Column(db.Float)
    calc_bhp = db.Column(db.Float)


class Wireline(TimestampMixin, ModelMixin, db.Model):

    __tablename__ = "wireline"

    id = db.Column(db.BigInteger, autoincrement=True, primary_key=True)
    stage_id = db.Column(db.Integer, nullable=False)
    ccl = db.Column(db.Float)
    current = db.Column(db.Float)
    line_speed = db.Column(db.Float)
    line_tension = db.Column(db.Float)
    trigger_perfs = db.Column(db.DateTime)
    weight = db.Column(db.Float)
    measured_depth = db.Column(db.Float)
    voltage = db.Column(db.Float)
    timestamp = db.Column(db.DateTime)
    elapsed_time = db.Column(db.DateTime)
    additional = db.Column(JSON)


class ResultProcessed(TimestampMixin, ModelMixin, db.Model):

    __tablename__ = "result_processed"

    id = db.Column(db.BigInteger, autoincrement=True, primary_key=True)
    stage_id = db.Column(db.Integer, nullable=False)
    well_id = db.Column(db.BigInteger)


class SinglePulseParameter(TimestampMixin, ModelMixin, db.Model):

    __tablename__ = "single_pulse_parameter"

    id = db.Column(db.BigInteger, autoincrement=True, primary_key=True)
    stage_id = db.Column(db.Integer, nullable=False)
    crew_id = db.Column(db.Integer, nullable=False)
    pulse_ordinal = db.Column(db.Integer)
    t_trigger = db.Column(db.DateTime)
    t_send = db.Column(db.Float)
    t_ref_0 = db.Column(db.DateTime)
    t_ref_1 = db.Column(db.Float)


class SinglePulseNfResult(TimestampMixin, ModelMixin, db.Model):

    __tablename__ = "single_pulse_nf_result"

    id = db.Column(db.BigInteger, autoincrement=True, primary_key=True)
    stage_id = db.Column(db.Integer, nullable=False)
    single_pulse_param_id = db.Column(db.Integer, nullable=False)
    crew_id = db.Column(db.Integer, nullable=False)
    nf_parameter_set_id = db.Column(db.Integer, nullable=False)
    pulse_ordinal = db.Column(db.Integer, nullable=False, default=1)
    inv_ver = db.Column(db.Float)
    reprocessed = db.Column(db.Integer)
    reprocessed_t = db.Column(db.DateTime)
    t_0 = db.Column(db.DateTime)
    t_end = db.Column(db.Float)
    nfci = db.Column(db.Float)
    w_inch = db.Column(db.Float)
    polarity = db.Column(db.Float)
    fit_error = db.Column(db.Float)
    runtime_s = db.Column(db.Float)
    k_d = db.Column(db.Float)
    q1 = db.Column(db.Float)
    q2 = db.Column(db.Float)
    q3 = db.Column(db.Float)
    c1 = db.Column(db.Float)
    c2 = db.Column(db.Float)
    c3 = db.Column(db.Float)
    tof1 = db.Column(db.Float)
    tof2 = db.Column(db.Float)
    tof3 = db.Column(db.Float)
    ld = db.Column(db.Float)
    ss_change = db.Column(db.Integer)
    qc_passed = db.Column(db.Integer)
    wco1 = db.Column(db.Float)
    wco2 = db.Column(db.Float)
    additional = db.Column(JSON)
    processing_note = db.Column(db.Text)


class Ff3Parameter(TimestampMixin, ModelMixin, db.Model):

    __tablename__ = "ff3_parameter"

    id = db.Column(db.BigInteger, autoincrement=True, primary_key=True)
    stage_id = db.Column(db.Integer, nullable=False)
    crew_id = db.Column(db.Integer, nullable=False)
    daq_sensor_id = db.Column(db.Integer, nullable=False)
    ff3_type = db.Column(db.Text)
    t_0 = db.Column(db.DateTime)
    t_length_s = db.Column(db.Float)
    avg_injection_rate = db.Column(db.Float)
    p_r = db.Column(db.Float)
    e_y = db.Column(db.Float)
    reservoir_press_psiperft = db.Column(db.Float)
    overburden_press = db.Column(db.Float)
    biot_coeff = db.Column(db.Float)
    tectonic_press = db.Column(db.Float)
    nu_lim_var = db.Column(db.Float)
    treatment_fluid_type = db.Column(db.Text)
    beta = db.Column(db.Float)
    compressibility_mpa = db.Column(db.Float)
    flags_PDL = db.Column(db.Integer)
    flags_stress_shadow = db.Column(db.Integer)
    flags_poisson_ver = db.Column(db.Integer)
    flags_breaker = db.Column(db.Integer)
    ff3_wci1 = db.Column(db.Float)
    ff3_wci2 = db.Column(db.Float)
    additional = db.Column(JSON)
    processing_note = db.Column(db.Text)


class Ff3Result(TimestampMixin, ModelMixin, db.Model):

    __tablename__ = "ff3_result"

    id = db.Column(db.BigInteger, autoincrement=True, primary_key=True)
    stage_id = db.Column(db.Integer, nullable=False)
    ff3_parameter_id = db.Column(db.Integer, nullable=False)
    crew_id = db.Column(db.Integer, nullable=False)
    inv_ver = db.Column(db.Float)
    ff3_reprocessed = db.Column(db.Integer, nullable=False, default=0)
    reprocessed_t = db.Column(db.DateTime)
    t_0 = db.Column(db.DateTime)
    t_length_s = db.Column(db.Float)
    ffkw_isip = db.Column(db.Float)
    ffkw_prop = db.Column(db.Float)
    min_stress = db.Column(db.Float)
    ff3_frac_pressure = db.Column(db.Float)
    min_stress_gradient = db.Column(db.Float)
    net_pressure = db.Column(db.Float)
    st_well_potential = db.Column(db.Float)
    st_reservoir_potential = db.Column(db.Float)
    leakoff_par1 = db.Column(db.Float)
    leakoff_par2 = db.Column(db.Float)
    nwb_drop_psi = db.Column(db.Float)
    c_nwb = db.Column(db.Float)
    v_nwb = db.Column(db.Float)
    nwb_compressibility = db.Column(db.Float)
    nwb_length = db.Column(db.Float)
    ff3_wc01 = db.Column(db.Float)
    ff3_wc02 = db.Column(db.Float)
    stress_shadow_psi = db.Column(db.Float)
    res_pressure_psi = db.Column(db.Float)
    ff3_poisson_rat = db.Column(db.Float)
    processing_note = db.Column(db.Text)
    frac_efficiency = db.Column(db.Float)
    H = db.Column(db.Float)
    R = db.Column(db.Float)
    W0 = db.Column(db.Float)
    shift_psi = db.Column(db.Float)
    r2 = db.Column(db.Float)
    calc_isip = db.Column(db.Float)
    l_max = db.Column(db.Float)
    l_min = db.Column(db.Float)
    h_max = db.Column(db.Float)
    h_min = db.Column(db.Float)
    additional = db.Column(JSON)


class Ff3Tvd(TimestampMixin, ModelMixin, db.Model):

    __tablename__ = "ff3_tvd"

    id = db.Column(db.BigInteger, autoincrement=True, primary_key=True)
    stage_id = db.Column(db.Integer, nullable=False)
    sigt = db.Column(db.Float)
    pres = db.Column(db.Float)
    p_r_calc = db.Column(db.Float)
    latepress = db.Column(db.Float)


class CloudSyncTableList(TimestampMixin, ModelMixin, db.Model):

    __tablename__ = "cloud_sync_table_list"

    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    table_name = db.Column(db.Text, nullable=False)
    sql_string = db.Column(db.Text, nullable=False)
    is_active = db.Column(TINYINT, default=1)


class CloudSyncTableLog(TimestampMixin, ModelMixin, db.Model):

    __tablename__ = "cloud_sync_table_log"

    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    table_name = db.Column(db.Text, nullable=False)
    sync_status = db.Column(db.String(25), nullable=False)
    synch_date = db.Column(db.DateTime)
