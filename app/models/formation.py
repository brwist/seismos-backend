from app.models.mixin_models import TimestampMixin
from app import db


class Formation(TimestampMixin, db.Model):

    __tablename__ = "formation"

    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.Integer, nullable=False)
