from sqlalchemy.orm import backref
from app.models.mixin_models import TimestampMixin, ModelMixin, uuid_string
from app import db


class Project(TimestampMixin, ModelMixin, db.Model):

    __tablename__ = "project"

    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer)
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
