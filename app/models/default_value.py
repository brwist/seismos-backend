from app.models.mixin_models import ModelMixin, JsonModelMixin
from app import db
from sqlalchemy.dialects.mysql import INTEGER


class DefaultVolumes(ModelMixin, JsonModelMixin, db.Model):

    __tablename__ = "default_volumes"

    id = db.Column(db.Integer, primary_key=True)
    well_id = db.Column(db.Integer, nullable=False)
    field_engineer = db.Column(db.String(255))
    bht_temp = db.Column(db.String(255))
    bhp_temp = db.Column(db.String(255))
    frac_design = db.Column(db.String(255))
    plug_type = db.Column(db.String(255))
    plug_seat_technique = db.Column(db.String(255))
    n_clusters = db.Column(INTEGER(unsigned=True))
    perf_gun = db.Column(db.String(255))
    description = db.Column(db.String(255))
    perf_diameter = db.Column(db.String(255))
    spf = db.Column(db.String(255))
    field = db.Column(db.String(255))
    acid = db.Column(db.String(255))
    base = db.Column(db.String(255))
    fluid_type = db.Column(db.String(255))
    proppant_data = db.Column(db.String(255))
    pulsing_parameters = db.Column(db.String(255))
    pumping_summary = db.Column(db.String(255))

    json_fields = [
        "field_engineer",
        "bht_temp",
        "bhp_temp",
        "frac_design",
        "plug_type",
        "plug_seat_technique",
        "n_clusters",
        "perf_gun",
        "description",
        "perf_diameter",
        "spf",
        "field",
        "acid",
        "base",
        "fluid_type",
        "proppant_data",
        "pulsing_parameters",
        "pumping_summary",
    ]
