from datetime import datetime
from app import db


class TimestampMixin():
    created_at = db.Column(db.DateTime, default=datetime.now, nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.now, nullable=False)


class ModelMixin(object):

    def save(self):
        # Save this model to the database.
        db.session.add(self)
        db.session.commit()
        return self

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self, dict_data):
        for key, value in dict_data.items():
            setattr(self, key, value)
        self.save()


class JsonModelMixin(object):

    def to_json(self):
        result = {}

        for field in self.json_fields:
            result[field] = getattr(self, field)

        return result
