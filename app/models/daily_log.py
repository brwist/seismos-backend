from app.models.mixin_models import ModelMixin
from app import db


class DailyLog(ModelMixin, db.Model):

    __tablename__ = "daily_log"

    id = db.Column(db.Integer, primary_key=True)
    well_id = db.Column(db.Integer, nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    description = db.Column(db.String(255), nullable=False)
