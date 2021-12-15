from sqlalchemy.dialects.mysql import JSON, TINYINT
from app.models.mixin_models import TimestampMixin, ModelMixin, JsonModelMixin, uuid_string
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
    stage_number = db.Column(db.Integer, default=0)
    number_of_cluster = db.Column(db.Integer, default=0)
    stage_start_time = db.Column(db.Numeric(25, 10), default=0)
    stage_end_time = db.Column(db.Numeric(25, 10), default=0)
    plug_depth = db.Column(db.Float, default=0)
    calc_net_pressure_result = db.Column(db.Float, default=0)
    observed_net_pressure = db.Column(db.Float, default=0)
    inline_density = db.Column(db.Float, default=0)
    blender_density = db.Column(db.Float, default=0)
    calc_bh_density = db.Column(db.Float, default=0)
    bottomhole_bhp = db.Column(db.Float, default=0)
    bottomhole_bht = db.Column(db.Float, default=0)
    frac_model_bhp = db.Column(db.Float, default=0)
    total_pumpdown_volume = db.Column(db.Float, default=0)
    poisson_ratio = db.Column(db.Float, default=0)
    pr_gradient = db.Column(db.Float, default=0)
    overburden_num = db.Column(db.Float, default=0)
    pumping_fluid_viscosity = db.Column(db.Float, default=0)
    pumping_fluid_density = db.Column(db.Float, default=0)
    pumping_fluid_type = db.Column(db.Text, default="")
    tectonic_gradient = db.Column(db.Float, default=0)
    pore_pressure = db.Column(db.Float, default=0)
    sleeve_name = db.Column(db.Text, default="")
    sleeve_ordinal = db.Column(db.Integer, default=0)
    sleeve_top_measured_depth = db.Column(db.Float, default=0)
    sleeve_bottom_measured_depth = db.Column(db.Float, default=0)
    sleeve_depth_unit = db.Column(db.Text, default="")
    sleeve_port_size = db.Column(db.Float, default=0)
    sleeve_port_size_unit = db.Column(db.Text, default="")
    sleeve_ball_size = db.Column(db.Float, default=0)
    sleeve_ball_size_unit = db.Column(db.Text, default="")
    sleeve_seat_id = db.Column(db.Text, default="")
    sleeve_manufacturer = db.Column(db.Text, default="")
    sleeve_model = db.Column(db.Text, default="")
    sleeve_toe_shift_pressure = db.Column(db.Integer, default=0)
    sleeve_toe_burst_pressure = db.Column(db.Integer, default=0)
    additional = db.Column(JSON, default="{}")
    is_approved = db.Column(TINYINT, default=0)
    diverter_type = db.Column(db.String(255), default="")
    pumped_diverter = db.Column(db.String(255), default="")
    spf = db.Column(db.String(255), default="")
    stage_event = db.Column(db.String(255), default="")
    designed_acid_vol = db.Column(db.Float, default=0)
    designed_flush_vol = db.Column(db.Float, default=0)
    designed_max_prop = db.Column(db.Float, default=0)
    designed_slurry_vol = db.Column(db.Float, default=0)
    designed_total_clean_fluid_vol = db.Column(db.Float, default=0)
    designed_proppant = db.Column(db.Float, default=0)
    designed_pad_vol = db.Column(db.Float, default=0)
    frac_design = db.Column(db.String(255), default="")
    plug_seat_technique = db.Column(db.String(255), default="")
    plug_type = db.Column(db.String(255), default="")
    plug_name = db.Column(db.String(50), default="")
    data_collection = db.Column(db.String(255), default=0)
    is_acid = db.Column(db.String(55), default="")
    # displacement
    top_perf_Displacement_volume = db.Column(db.Float, default=0)
    bottom_perf_Displacement_volume = db.Column(db.Float, default=0)
    plug_displacement_volume = db.Column(db.Float, default=0)

    well = db.relationship(
        "Well",
        foreign_keys=[well_id],
        primaryjoin="Well.id == Stage.well_id",
    )

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
        report["stage_start_time"] = int(report["stage_start_time"])
        report["stage_end_time"] = int(report["stage_end_time"])
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


class NFProcessingResult(TimestampMixin, ModelMixin, db.Model, QCReportDataModel, JsonModelMixin):
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
        "c0", "c1", "c2", "c3",
        "q0", "q1", "q2", "q3",
        "fit_error", "nf_param_id",
        "connect_ops_risk",
        "connect_efficiency",
        "connect_condition",
    ]

    json_fields = (
        "timestamp", "user_id", "c0",
        "c1", "c2", "c3",
        "q0", "q1", "q2",
        "q3", "fit_error", "nf_param_id",
        "connect_ops_risk", "connect_efficiency", "connect_condition",
    )


class StageAVG(TimestampMixin, ModelMixin, db.Model, QCReportDataModel, JsonModelMixin):
    __tablename__ = "stage_avg"

    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    stage_id = db.Column(db.Integer, nullable=False)
    breakdown_pressure = db.Column(db.Float, default=0)
    isip = db.Column(db.Float, default=0)
    frac_gradient = db.Column(db.Float, default=0)
    diverter = db.Column(db.Float, default=0)
    acid = db.Column(db.Float, default=0)
    open_well_pressure = db.Column(db.Float, default=0)
    isip_5min = db.Column(db.Float, default=0)
    isip_10min = db.Column(db.Float, default=0)
    isip_15min = db.Column(db.Float, default=0)
    time_to_max_rate = db.Column(db.Float, default=0)
    avg_pressure = db.Column(db.Float, default=0)
    max_pressure = db.Column(db.Float, default=0)
    slickwater_volume = db.Column(db.Float, default=0)
    total_slurry = db.Column(db.Float, default=0)
    total_clean = db.Column(db.Float, default=0)
    avg_rate = db.Column(db.Float, default=0)
    max_rate = db.Column(db.Float, default=0)
    mesh_100 = db.Column("100_mesh", db.Float, default=0)
    mesh_30_50 = db.Column("30_50_mesh", db.Float, default=0)
    mesh_40_70 = db.Column("40_70_mesh", db.Float, default=0)
    mesh_20_40 = db.Column("20_40_mesh", db.Float, default=0)
    micro_prop = db.Column(db.Float, default=0)
    friction_reducer = db.Column(db.Float, default=0)
    gel = db.Column(db.Float, default=0)
    crosslink = db.Column(db.Float, default=0)
    additional = db.Column(JSON, default="{}")
    flush_volume = db.Column(db.Float, default=0)
    max_prop_conc = db.Column(db.Float, default=0)
    pad_vol = db.Column(db.Integer, default=0)
    opening_well = db.Column(db.Integer, default=0)
    to_report = [
        "breakdown_pressure", "isip", "frac_gradient",
        "diverter", "acid", "opening_well",
        "isip_5min", "isip_10min", "isip_15min",
        "time_to_max_rate", "mesh_100", "mesh_30_50",
        "mesh_40_70", "mesh_20_40", "micro_prop",
        "friction_reducer", "gel", "crosslink",
    ]

    json_fields = (
        "breakdown_pressure", "isip", "frac_gradient",
        "diverter", "acid", "open_well_pressure",
        "isip_5min", "isip_10min", "isip_15min",
        "time_to_max_rate", "avg_pressure", "max_pressure",
        "slickwater_volume", "total_slurry", "total_clean",
        "avg_rate", "max_rate", "mesh_100",
        "mesh_30_50", "mesh_40_70", "mesh_20_40",
        "micro_prop", "friction_reducer", "gel",
        "crosslink", "additional", "pad_vol",
        "flush_volume", "max_prop_conc", "pad_vol",
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
