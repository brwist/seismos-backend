from app.models.mixin_models import TimestampMixin, ModelMixin
from app import db


class JobInfo(TimestampMixin, ModelMixin, db.Model):

    __tablename__ = "job_info"

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    job_id = db.Column(db.Integer)
    job_name = db.Column(db.Text, nullable=False)
    afe_id = db.Column(db.Integer)
    job_type_id = db.Column(db.Integer)
    job_start_date = db.Column(db.DateTime)
    job_end_date = db.Column(db.DateTime)
    project_id = db.Column(db.BigInteger)

    job_type = db.relationship(
        "JobType",
        foreign_keys=[job_type_id],
        primaryjoin="JobInfo.job_type_id == JobType.id",
        cascade="all,delete",
    )

    location = db.relationship(
        "LocationInfo",
        foreign_keys=[id],
        primaryjoin="JobInfo.id == LocationInfo.job_info_id",
        cascade="all,delete",
    )
