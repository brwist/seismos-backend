from app.models.mixin_models import TimestampMixin, ModelMixin
from sqlalchemy.dialects.mysql import JSON
from app import db


class Pumpdown(TimestampMixin, ModelMixin, db.Model):

    __tablename__ = "pumpdown"

    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    stage_id = db.Column(db.Integer, nullable=False)
    timestamp = db.Column(db.DateTime)
    pressure = db.Column(db.Float)
    rate = db.Column(db.Float)
    total_pumdown_value = db.Column(db.Float)


class Pumping(TimestampMixin, ModelMixin, db.Model):

    __tablename__ = "pumping"

    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    stage_id = db.Column(db.Integer, nullable=False)
    timestamp = db.Column(db.DateTime)
    treating_pressure = db.Column(db.Float)
    total_slurry_volume = db.Column(db.Float)
    total_clean_volume = db.Column(db.Float)
    slurry_rate = db.Column(db.Float)
    clean_rate = db.Column(db.Float)
    surface_prop_conc = db.Column(db.Float)
    bottom_prop_conc = db.Column(db.Float)
    bottom_pressure = db.Column(db.Float)
    net_pressure = db.Column(db.Float)
    backside_pressure = db.Column(db.Float)
    friction_reducer = db.Column(db.Float)
    gel = db.Column(db.Float)
    crosslink = db.Column(db.Float)
    additional_column = db.Column(JSON)
