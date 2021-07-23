from .mixin_models import TimestampMixin, ModelMixin
from app import db


class JobInfo(TimestampMixin, ModelMixin, db.Model):

    __tablename__ = "job_info"

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    job_id = db.Column(db.Text)
    job_name = db.Column(db.Text, nullable=False)
    afe_id = db.Column(db.Integer)
    job_type_id = db.Column(db.Integer)
    job_start_date = db.Column(db.DateTime)
    job_end_date = db.Column(db.DateTime)


class JobType(TimestampMixin, ModelMixin, db.Model):

    __tablename__ = "job_type"

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    value = db.Column(db.Text)
