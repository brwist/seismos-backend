from datetime import datetime
from app import db


class TimestampMixin():
    created_at = db.Column(db.DateTime, default=datetime.now, nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.now, nullable=False)
