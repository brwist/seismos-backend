from app.models.mixin_models import TimestampMixin, ModelMixin
from app import db


class Equipment(TimestampMixin, ModelMixin, db.Model):

    __tablename__ = "equipment"

    id = db.Column(db.Integer, primary_key=True)
    trailer_id = db.Column(db.Integer)
    powerpack_id = db.Column(db.Integer)
    source_id = db.Column(db.Integer)
    accumulator_id = db.Column(db.Integer)
    hydrophones_id = db.Column(db.Integer)
    hotspot_id = db.Column(db.Integer)
    computer_id = db.Column(db.Integer)
    transducer_id = db.Column(db.Integer)
