from sqlalchemy.orm import backref
from app.models.mixin_models import TimestampMixin, ModelMixin
from app import db


class Pad(TimestampMixin, ModelMixin, db.Model):

    __tablename__ = "pad"

    id = db.Column(db.Integer, primary_key=True)
    pad_uuid = db.Column(db.String(36), nullable=False)
    project_id = db.Column(db.BigInteger, nullable=False)
    pad_name = db.Column(db.Text, nullable=False)
    number_of_wells = db.Column(db.Integer)
    well_spacing = db.Column(db.Float)

    wells = db.relationship(
        "Well",
        foreign_keys=[id],
        primaryjoin="Pad.id == Well.pad_id",
        uselist=True,
        backref=backref('pad', uselist=False),
        lazy=True,
    )
