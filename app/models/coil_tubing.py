from app.models.mixin_models import TimestampMixin, ModelMixin
from app import db


class CoilTubing(TimestampMixin, ModelMixin, db.Model):

    __tablename__ = "coil_tubing"

    id = db.Column(db.BigInteger, autoincrement=True)
    stage_id = db.Column(db.Integer, primary_key=True, nullable=False)
    timestamp = db.Column(db.DateTime)
    pump_rate = db.Column(db.Float)
    pump_rate_unit = db.Column(db.Text)
    tubing_pressure = db.Column(db.Float)
    tubing_pressure_unit = db.Column(db.Text)
    depth = db.Column(db.Float)
    depth_unit = db.Column(db.Text)
    flowback_rate = db.Column(db.Float)
    flowback_unit = db.Column(db.Text)
    trip_in_out_rate = db.Column(db.Float)
    trip_in_out_rate_unit = db.Column(db.Text)
    weight_on_bit = db.Column(db.Float)
    weight_on_bit_unit = db.Column(db.Text)
