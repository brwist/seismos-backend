from app.models.mixin_models import TimestampMixin, ModelMixin
from sqlalchemy.dialects.mysql import JSON
from app import db


class SurveyReport(TimestampMixin, ModelMixin, db.Model):

    __tablename__ = "survey_report"

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    file_metadata_id = db.Column(db.Integer, nullable=False)
    measured_depth = db.Column(db.Float)
    inclination = db.Column(db.Float)
    tvd = db.Column(db.Float)
    ns = db.Column(db.Float)
    ew = db.Column(db.Float)
    vs = db.Column(db.Float)
    dls = db.Column(db.Float)
    closure_direction = db.Column(db.Float)
    dogleg_severity = db.Column(db.Float)
    additional = db.Column(JSON)
