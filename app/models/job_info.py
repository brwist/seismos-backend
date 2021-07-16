from app.models.mixin_models import TimestampMixin
from app import db


class JobInfo(TimestampMixin, db.Model):

    __tablename__ = "job_info"

    job_id = db.Column(db.Integer, primary_key=True, nullable=False)
    job_name = db.Column(db.Text, nullable=False)
    afe_id = db.Column(db.Integer)
    job_type_id = db.Column(db.Integer)
