from app.models.mixin_models import TimestampMixin, ModelMixin
from app import db


class FluidTypeLookup(TimestampMixin, ModelMixin, db.Model):

    __tablename__ = "fluid_type_lookup"

    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    value = db.Column(db.Integer, nullable=False)


class FracDesignLookup(TimestampMixin, ModelMixin, db.Model):

    __tablename__ = "frac_design_lookup"

    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    value = db.Column(db.Integer, nullable=False)


class PlugDepthUnitLookup(TimestampMixin, ModelMixin, db.Model):

    __tablename__ = "plug_depth_unit_lookup"

    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    value = db.Column(db.Text, nullable=False)


class PlugNameLookup(TimestampMixin, ModelMixin, db.Model):

    __tablename__ = "plug_name_lookup"

    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    value = db.Column(db.Float, nullable=False)


class ProppantLookup(TimestampMixin, ModelMixin, db.Model):

    __tablename__ = "proppant_lookup"

    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    proppant_name = db.Column(db.Float, nullable=False)


# class DaqSensor(TimestampMixin, ModelMixin, db.Model):

#     __tablename__ = "DaqSensor"

#     Id = db.Column(db.Integer)
#     Name = db.Column(db.Text)


# class DaqSample(TimestampMixin, ModelMixin, db.Model):

#     __tablename__ = "DaqSample"

#     SensorId = db.Column(db.Integer)
#     Value = db.Column(db.Float)
#     SampleTimeUtc = db.Column(db.DateTime)
