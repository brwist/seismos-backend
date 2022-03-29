from app.models.mixin_models import TimestampMixin, ModelMixin
from sqlalchemy.dialects.mysql import JSON
from app import db


class FormationTop(TimestampMixin, ModelMixin, db.Model):

    __tablename__ = "formation_top"

    id = db.Column(db.BigInteger, autoincrement=True)
    well_id = db.Column(db.Integer, primary_key=True, nullable=False)
    measured_depth = db.Column(db.Float)
    inclination = db.Column(db.Float)
    azimuth = db.Column(db.Float)
    X = db.Column(db.Float)
    Y = db.Column(db.Float)
    Z = db.Column(db.Float)
    target_upper = db.Column(db.Float)
    target_lower = db.Column(db.Float)
    l1_upper = db.Column(db.Float)
    l1_lower = db.Column(db.Float)
    l2_upper = db.Column(db.Float)
    l2_lower = db.Column(db.Float)
    l3_upper = db.Column(db.Float)
    l3_lower = db.Column(db.Float)
    l4_upper = db.Column(db.Float)
    l4_lower = db.Column(db.Float)
    l5_uppper = db.Column(db.Float)
    l5_lower = db.Column(db.Float)
    l6_uppper = db.Column(db.Float)
    l6_lower = db.Column(db.Float)
    l7_uppper = db.Column(db.Float)
    l7_lower = db.Column(db.Float)
    l8_upper = db.Column(db.Float)
    l8_lower = db.Column(db.Float)
    l9_upper = db.Column(db.Float)
    l9_lower = db.Column(db.Float)
    l10_upper = db.Column(db.Float)
    l10_lower = db.Column(db.Float)
    additional = db.Column(JSON)


class FormationTopReference(TimestampMixin, ModelMixin, db.Model):

    __tablename__ = "formation_top_reference"

    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    formation_top_id = db.Column(db.Integer, nullable=False)
    l1 = db.Column(db.Text)
    l2 = db.Column(db.Text)
    l3 = db.Column(db.Text)
    l4 = db.Column(db.Text)
    l5 = db.Column(db.Text)
    l6 = db.Column(db.Text)
    l7 = db.Column(db.Text)
    l8 = db.Column(db.Text)
    l9 = db.Column(db.Text)
    l10 = db.Column(db.Text)
