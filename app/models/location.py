from app.models.mixin_models import TimestampMixin, ModelMixin
from app import db


class LocationInfo(TimestampMixin, ModelMixin, db.Model):

    __tablename__ = "location_info"

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    county_name_id = db.Column(db.Integer, nullable=False)
    basin_name_id = db.Column(db.Integer, nullable=False)
    state_id = db.Column(db.Integer, nullable=False)


class CountryName(TimestampMixin, ModelMixin, db.Model):

    __tablename__ = "county_name"

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    county_name = db.Column(db.Text)


class BasinName(TimestampMixin, ModelMixin, db.Model):

    __tablename__ = "basin_name"

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    basin_name = db.Column(db.Text, nullable=False)


class State(TimestampMixin, ModelMixin, db.Model):

    __tablename__ = "state"

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    value = db.Column(db.Text, nullable=False)
