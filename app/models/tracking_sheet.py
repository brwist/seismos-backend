from datetime import datetime
from sqlalchemy.dialects.mysql import TINYINT
from app.models.mixin_models import ModelMixin, TimestampMixin, JsonModelMixin
from app import db


class ChemFluids(ModelMixin, db.Model, TimestampMixin, JsonModelMixin):
    __tablename__ = "chem_fluids"

    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    stage_id = db.Column(db.Integer)
    fluid_type_name = db.Column(db.Integer)
    chem_trade_name = db.Column(db.Text)
    chem_name = db.Column(db.Text)
    volume = db.Column(db.Float)
    volume_unit = db.Column(db.Text)
    volume_concentration = db.Column(db.Float)
    volume_concentration_unit = db.Column(db.Text)
    dry_total = db.Column(db.Float)
    dry_total_unit = db.Column(db.Text)
    dry_concentration = db.Column(db.Float)
    dry_concentration_unit = db.Column(db.Text)
    acid = db.Column(db.Float)
    acid_unit = db.Column(db.Text)
    clay_stabilizer = db.Column(db.Float)
    clay_stabilizer_unit = db.Column(db.Text)
    misc = db.Column(db.Text)
    bulk_modulus = db.Column(db.Float)
    bulk_modulus_unit = db.Column(db.Text)
    base_fluid_density = db.Column(db.Float)
    base_fluid_type = db.Column(db.String(255))
    max_conc_density = db.Column(db.Float)
    design_acid_vol = db.Column(db.Integer)

    formation_fuild_injection = db.relation(
        "FormationFuildInjection",
        foreign_keys=[id],
        primaryjoin="ChemFluids.id == FormationFuildInjection.chem_fluid_id",
        uselist=True,
        cascade="all,delete",
    )

    json_fields = (
        "fluid_type_name", "chem_trade_name", "chem_name",
        "volume", "volume_unit", "volume_concentration",
        "volume_concentration_unit", "dry_total", "dry_total_unit",
        "dry_concentration", "dry_concentration_unit", "acid",
        "acid_unit", "clay_stabilizer", "clay_stabilizer_unit",
        "misc", "bulk_modulus", "bulk_modulus_unit",
        "base_fluid_density", "base_fluid_type", "max_conc_density",
        "design_acid_vol"
    )

    json_list_fields = ("formation_fuild_injection",)

    def to_json(self, remove_none=False):
        res = super().to_json(remove_none)
        for list_field in self.json_list_fields:
            res[list_field] = []
            list_value = getattr(self, list_field)
            for value in list_value:
                res[list_field].append(value.to_json())
        return res


# FluidsItem
class FormationFuildInjection(ModelMixin, db.Model, JsonModelMixin):
    __tablename__ = "formation_fuild_injection"

    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    chem_fluid_id = db.Column(db.Integer, nullable=False)
    bbls = db.Column(db.Integer)
    ppg = db.Column(db.Float)
    description = db.Column(db.String(50))

    json_fields = ("bbls", "ppg", "description")


class Perforation(ModelMixin, db.Model, TimestampMixin, JsonModelMixin):
    __tablename__ = "perforation"

    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    stage_id = db.Column(db.Integer)
    order_num = db.Column(db.Integer)
    ordinal = db.Column(db.Float)
    top_measured_depth = db.Column(db.Float)
    bottom_measured_depth = db.Column(db.Float)
    depth_unit = db.Column(db.Text)
    shot_number = db.Column(db.Integer)
    shot_density = db.Column(db.Float)
    shot_density_unit = db.Column(db.Text)
    shot_count = db.Column(db.Integer)
    phasing = db.Column(db.Text)
    conveyance_method = db.Column(db.Text)
    charge_type = db.Column(db.Text)
    charge_size = db.Column(db.Float)
    charge_size_unit = db.Column(db.Text)
    estimated_hole_diameter = db.Column(db.Float)
    estimated_hole_diameter_unit = db.Column(db.Text)
    perf_plug_num = db.Column(db.Integer)
    perf_start_time = db.Column(db.DateTime)
    perf_end_time = db.Column(db.DateTime)
    bottom_perf = db.Column(db.Float)
    perf_gun_description = db.Column(db.String(255))

    json_fields = (
        "order_num", "ordinal", "top_measured_depth",
        "bottom_measured_depth", "depth_unit", "shot_number",
        "shot_density", "shot_density_unit", "shot_count",
        "phasing", "conveyance_method", "charge_type",
        "charge_size", "charge_size_unit", "estimated_hole_diameter",
        "estimated_hole_diameter_unit", "perf_plug_num", "perf_start_time",
        "perf_end_time", "bottom_perf", "perf_gun_description",
    )


class Proppant(ModelMixin, db.Model, TimestampMixin, JsonModelMixin):
    __tablename__ = "proppant"

    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    stage_id = db.Column(db.Integer)
    proppant_name = db.Column(db.String(35))
    prop_mass = db.Column(db.Float)
    mass_unit = db.Column(db.String(10))
    material = db.Column(db.String(25))
    mesh_size = db.Column(db.Float)
    avg_concentration = db.Column(db.Float)
    avg_concentration_unit = db.Column(db.String(10))
    max_concentration = db.Column(db.Float)
    max_concentration_unit = db.Column(db.String(10))

    bulk_density = db.Column(db.Integer)
    specific_gravity = db.Column(db.Float)
    actual_lbs = db.Column(db.Float)
    designed_lbs = db.Column(db.Float)
    total_pumped_lbs = db.Column(db.Float)
    proppant_type_start_time = db.Column(db.DateTime)
    proppant_end_start_time = db.Column(db.DateTime)

    json_fields = (
        "proppant_name", "prop_mass", "mass_unit",
        "material", "mesh_size", "avg_concentration",
        "avg_concentration_unit", "max_concentration", "max_concentration_unit",
        "bulk_density", "specific_gravity", "actual_lbs",
        "designed_lbs", "total_pumped_lbs"
    )

    datetime_fields = (
        "proppant_type_start_time",
        "proppant_end_start_time"
    )

    def to_json(self):
        data = super().to_json()
        for field in self.datetime_fields:
            timestamp = getattr(self, field)
            if timestamp:
                data[field] = timestamp.timestamp()

        return data


class ActiveData(ModelMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    stage_id = db.Column(db.Integer, nullable=False)
    amplitude = db.Column(db.Integer, nullable=False, default=0)
    frequency = db.Column(db.Float, nullable=False, default=0)
    offset = db.Column(db.Integer, nullable=False, default=0)
    period = db.Column(db.Integer, nullable=False, default=0)
    wave_type = db.Column(db.String(50))
    post_frac_start_time = db.Column(db.Integer)
    post_frac_end_time = db.Column(db.Integer)
    pre_frac_start_time = db.Column(db.Integer)
    pre_frac_end_time = db.Column(db.Integer)
    pre_frac_num_pulse = db.Column(db.Integer)
    post_frac_num_pulse = db.Column(db.Integer)
    pre_frac_pulse_note = db.Column(db.String(255))
    post_frac_pulse_note = db.Column(db.String(255))
    additional_note = db.Column(db.String(255))
