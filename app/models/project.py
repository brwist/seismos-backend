from sqlalchemy.orm import backref
from sqlalchemy.dialects.mysql import TINYINT
from app.models.mixin_models import TimestampMixin, ModelMixin, uuid_string
from app import db


class Project(TimestampMixin, ModelMixin, db.Model):

    __tablename__ = "project"

    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, nullable=False)
    project_uuid = db.Column(db.String(36), nullable=False, default=uuid_string)
    project_name = db.Column(db.Text, nullable=False)
    client_id = db.Column(db.Integer, nullable=False)

    client = db.relationship(
        "Client",
        foreign_keys=[client_id],
        primaryjoin="Project.client_id == Client.id",
        cascade="all,delete",
    )

    pad = db.relationship(
        "Pad",
        foreign_keys=[id],
        primaryjoin="Project.id == Pad.project_id",
        backref=backref("project", uselist=False),
        lazy=True,
        cascade="all,delete",
    )

    job_info = db.relationship(
        "JobInfo",
        foreign_keys=[id],
        primaryjoin="Project.id == JobInfo.project_id",
        cascade="all,delete",
    )

    project_crew = db.relationship(
        "ProjectCrew",
        foreign_keys=[id],
        primaryjoin="Project.id == ProjectCrew.project_id",
        backref=backref("project", uselist=False),
        cascade="all,delete",
    )


class QualityControl(TimestampMixin, ModelMixin, db.Model):

    __tablename__ = "quality_control"

    id = db.Column(db.BigInteger, autoincrement=True)
    project_id = db.Column(db.BigInteger, primary_key=True)
    is_checked = db.Column(TINYINT)
    checked_by = db.Column(db.Text)


class Software(TimestampMixin, ModelMixin, db.Model):

    __tablename__ = "software"

    id = db.Column(db.BigInteger, autoincrement=True)
    project_id = db.Column(db.BigInteger, primary_key=True)
    inpute_app_version = db.Column(db.Float)
    processing_version = db.Column(db.Float)
    db_version = db.Column(db.Float)
    mqtt_version = db.Column(db.Float)
