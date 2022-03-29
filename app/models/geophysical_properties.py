from app.models.mixin_models import TimestampMixin, ModelMixin
from sqlalchemy.dialects.mysql import JSON
from app import db


class GeophysicalProperties(TimestampMixin, ModelMixin, db.Model):

    __tablename__ = "geophysical_properties"

    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    file_metadata_id = db.Column(db.Integer, nullable=False)
    measured_depth = db.Column(db.Float)
    young_modulus = db.Column(db.Float)
    poisson_ratio = db.Column(db.Float)
    min_stress = db.Column(db.Float)
    dynamic_horizontal_young_modulus = db.Column(db.Float)
    static_horizontal_young_modulus = db.Column(db.Float)
    static_vertical_young_modulus = db.Column(db.Float)
    horizontal_poisson_ratio = db.Column(db.Float)
    pore_pressure = db.Column(db.Float)
    tensile_strength = db.Column(db.Float)
    vertical_stress_gradient = db.Column(db.Float)
    json_data = db.Column(JSON)


class MudLog(TimestampMixin, ModelMixin, db.Model):

    __tablename__ = "mud_log"

    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    file_metadata_id = db.Column(db.Integer, nullable=False)
    measure_depth = db.Column(db.Float)
    siltstone = db.Column(db.Float)
    sand = db.Column(db.Float)
    coal = db.Column(db.Float)
    limestone = db.Column(db.Float)
    dolomite = db.Column(db.Float)
    salt = db.Column(db.Float)
    chert = db.Column(db.Float)
    chalk = db.Column(db.Float)
    anhydrite = db.Column(db.Float)
    shale = db.Column(db.Float)
    gamma_ray = db.Column(db.Float)
    clay = db.Column(db.Float)
    marl = db.Column(db.Float)
    rate_of_penetration = db.Column(db.Float)
    rpm = db.Column(db.Float)
    weight_on_bit = db.Column(db.Float)
    total_gas = db.Column(db.Float)
    methane = db.Column(db.Float)
    ethane = db.Column(db.Float)
    propane = db.Column(db.Float)
    isobutane = db.Column(db.Float)
    butane = db.Column(db.Float)
    isopentane = db.Column(db.Float)
    pentane = db.Column(db.Float)
    json_data = db.Column(JSON)


class MwdReport(TimestampMixin, ModelMixin, db.Model):

    __tablename__ = "mwd_report"

    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    file_metadata_id = db.Column(db.Integer, nullable=False)
    measured_depth = db.Column(db.Float)
    gamma_ray = db.Column(db.Float)
