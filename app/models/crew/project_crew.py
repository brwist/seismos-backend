from app.models.mixin_models import TimestampMixin, ModelMixin
from app import db


class ProjectCrew(TimestampMixin, ModelMixin, db.Model):

    __tablename__ = "project_crew"

    project_crew_id = db.Column(db.BigInteger, primary_key=True)
    project_id = db.Column(db.BigInteger, nullable=False)
    crew_id = db.Column(db.Integer, nullable=False)

    crew = db.relationship(
        "Crew",
        foreign_keys=[crew_id],
        primaryjoin="ProjectCrew.crew_id == Crew.id"
    )
