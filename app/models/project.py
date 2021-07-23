from app.models.mixin_models import TimestampMixin, ModelMixin
from app import db


class Project(TimestampMixin, ModelMixin, db.Model):

    __tablename__ = "project"

    id = db.Column(db.Integer, primary_key=True)
    project_uuid = db.Column(db.String(36), nullable=False)
    project_name = db.Column(db.Text, nullable=False)  # TODO make it string with fix max width
    client_id = db.Column(db.Integer, nullable=False)
    equipment_id = db.Column(db.Integer)

    equipment = db.relationship(
        'Equipment',
        foreign_keys=[equipment_id],
        primaryjoin='Project.equipment_id == Equipment.id'
    )
