from app.models.mixin_models import TimestampMixin, ModelMixin
from app import db


class Crew(TimestampMixin, ModelMixin, db.Model):

    __tablename__ = "crew"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    phone_number = db.Column(db.Text, nullable=False)
    role = db.Column(db.Enum('admin', 'manager', 'engineer'), nullable=False, default="N")
    manager_id = db.Column(db.Integer)


class ProjectCrew(TimestampMixin, ModelMixin, db.Model):

    __tablename__ = "project_crew"

    project_crew_id = db.Column(db.Integer, primary_key=True)
    project_id = db.Column(db.Integer, nullable=False)
    crew_id = db.Column(db.Integer, nullable=False)
