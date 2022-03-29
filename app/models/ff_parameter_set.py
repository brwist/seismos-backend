from app.models.mixin_models import TimestampMixin, ModelMixin
from app import db


class FFParameterSet(TimestampMixin, ModelMixin, db.Model):

    __tablename__ = "ff_parameter_set"

    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.Text, nullable=False)
    date_created = db.Column(db.DateTime)
    shut_in_period_start = db.Column(db.DateTime)
    sample_rate = db.Column(db.Float)
    total_samples = db.Column(db.Float)
    tvd = db.Column(db.Float)
    viscosity = db.Column(db.Float)
    compressibility_mpa = db.Column(db.Float)
    poisson_ratio = db.Column(db.Float)
    youngs_modulus_mpa = db.Column(db.Float)
    volume_pumped = db.Column(db.Float)
    proppant_volume_pumped_bbl = db.Column(db.Float)
    average_injection_rate = db.Column(db.Float)
    tectonic_component = db.Column(db.Float)
