from app.models.mixin_models import TimestampMixin, ModelMixin
from app import db


class BacksidePressure(TimestampMixin, ModelMixin, db.Model):

    __tablename__ = "backside_pressure"

    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    stage_id = db.Column(db.Integer, nullable=False)
    value = db.Column(db.Float, nullable=False)
