from app.models.mixin_models import TimestampMixin
from app import db


class Pad(TimestampMixin, db.Model):

    __tablename__ = "pad"

    id = db.Column(db.Integer, primary_key=True)
    pad_uuid = db.Column(db.String(36), nullable=False)
    project_id = db.Column(db.Integer, nullable=False)
    pad_name = db.Column(db.Text, nullable=False)
    number_of_wells = db.Column(db.Integer)
    well_spacing = db.Column(db.Float)
