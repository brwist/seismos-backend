from app.models.mixin_models import TimestampMixin, ModelMixin
from app import db


class JobType(TimestampMixin, ModelMixin, db.Model):

    __tablename__ = "job_type"

    id = db.Column(db.BigInteger, primary_key=True, nullable=False)
    value = db.Column(db.Text)
