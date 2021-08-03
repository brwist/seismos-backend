from sqlalchemy.orm import backref
from app.models.mixin_models import TimestampMixin, ModelMixin
from app import db


class Project(TimestampMixin, ModelMixin, db.Model):

    __tablename__ = "project"

    id = db.Column(db.Integer, primary_key=True)
    project_uuid = db.Column(db.String(36), nullable=False)
    project_name = db.Column(db.Text, nullable=False)  # TODO make it string with fix max width
    client_id = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, nullable=False)
    equipment_id = db.Column(db.Integer)

    equipment = db.relationship(
        "Equipment",
        foreign_keys=[equipment_id],
        primaryjoin="Project.equipment_id == Equipment.id"
    )

    client = db.relationship(
        "Client",
        foreign_keys=[client_id],
        primaryjoin="Project.client_id == Client.id"
    )

    pad = db.relationship(
        "Pad",
        foreign_keys=[id],
        primaryjoin="Project.id == Pad.project_id",
        backref=backref("project", uselist=False),
        lazy=True,
    )

    job_info = db.relationship(
        "JobInfo",
        foreign_keys=[id],
        primaryjoin="Project.id == JobInfo.project_id"
    )

    project_crew = db.relationship(
        "ProjectCrew",
        foreign_keys=[id],
        primaryjoin="Project.id == ProjectCrew.project_id",
        uselist=True
    )
