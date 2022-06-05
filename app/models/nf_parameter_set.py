from app.models.mixin_models import TimestampMixin, ModelMixin
from sqlalchemy.dialects.mysql import JSON
from app import db


class NfParameterSet(TimestampMixin, ModelMixin, db.Model):

    __tablename__ = "nf_parameter_set"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    crew_id = db.Column(db.Integer, nullable=False)
    daq_sensor_id = db.Column(db.Integer, nullable=False)
    parameter_type = db.Column(db.Text, nullable=False)
    t_0 = db.Column(db.DateTime)
    pulsetrain_duration = db.Column(db.Float)
    clock_offset = db.Column(db.Float)
    hp_channel_id = db.Column(db.Integer)
    p_channel_id = db.Column(db.Integer)
    n_pulses = db.Column(db.Integer)
    inv_method = db.Column(db.Integer)
    pop_size = db.Column(db.Integer)
    noise_level = db.Column(db.Float)
    deconv_layer = db.Column(db.Integer)
    c1_min = db.Column(db.Integer)
    c1_max = db.Column(db.Integer)
    c2_min = db.Column(db.Integer)
    c2_max = db.Column(db.Integer)
    c3_min = db.Column(db.Integer)
    c3_max = db.Column(db.Integer)
    q1_min = db.Column(db.Float)
    q1_max = db.Column(db.Float)
    q2_min = db.Column(db.Float)
    q2_max = db.Column(db.Float)
    q3_min = db.Column(db.Float)
    q3_max = db.Column(db.Float)
    k_min = db.Column(db.Float)
    k_max = db.Column(db.Float)
    w_min = db.Column(db.Float)
    w_max = db.Column(db.Float)
    w_inch = db.Column(db.Float)
    mu_cp = db.Column(db.Float)
    rho_kgm3 = db.Column(db.Float)
    b_1_psi = db.Column(db.Float)
    json_data = db.Column(JSON)
