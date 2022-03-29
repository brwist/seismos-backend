from sqlalchemy.orm import backref
from sqlalchemy.dialects.mysql import JSON, TINYINT
from app.models.mixin_models import TimestampMixin, ModelMixin, uuid_string
from app import db


class Well(TimestampMixin, ModelMixin, db.Model):

    __tablename__ = "well"

    id = db.Column(db.BigInteger, autoincrement=True, primary_key=True)
    well_uuid = db.Column(db.String(36), default=uuid_string, nullable=False)
    equipment_id = db.Column(db.Integer, nullable=False)
    pad_id = db.Column(db.Integer, nullable=False)
    well_name = db.Column(db.Text)
    well_api = db.Column(db.Text)
    formation = db.Column(db.String(255))
    num_stages = db.Column(db.Integer, default=0)
    total_planned_stage = db.Column(db.Integer)
    total_perfs = db.Column(db.Integer)
    total_clusters = db.Column(db.Integer)
    frac_system = db.Column(db.Text)
    fluid_system = db.Column(db.Text)
    well_start_time = db.Column(db.DateTime)
    well_end_time = db.Column(db.DateTime)
    bottom_hole_latitude = db.Column(db.Float)
    bottom_hole_longitude = db.Column(db.Float)
    surface_longitude = db.Column(db.Float)
    surface_latitude = db.Column(db.Float)
    lateral_length = db.Column(db.Float)
    lateral_length_unit = db.Column(db.Text)
    measured_depth = db.Column(db.Float)
    vertical_depth = db.Column(db.Float)
    vertical_depth_unit = db.Column(db.Text)
    estimated_surface_vol = db.Column(db.Float)
    estimated_bbls = db.Column(db.Float)
    estimated_gallons = db.Column(db.Float)
    casing_od = db.Column(db.Float)
    casing_wt = db.Column(db.Float)
    casing_id = db.Column(db.Float)
    casing_depth_md = db.Column(db.Float)
    casing_tol = db.Column(db.Float)
    liner1_od = db.Column(db.Float)
    liner1_wt = db.Column(db.Float)
    liner1_id = db.Column(db.Text)
    liner1_depth_md = db.Column(db.Float)
    liner1_tol = db.Column(db.Float)
    liner2_od = db.Column(db.Float)
    liner2_wt = db.Column(db.Float)
    liner2_id = db.Column(db.Text)
    liner2_depth_md = db.Column(db.Float)
    liner2_tol = db.Column(db.Float)
    measured_depth_unit = db.Column(db.Text)

    default_value = db.relationship(
        "DefaultVal",
        foreign_keys=[id],
        primaryjoin="Well.id == DefaultVal.well_id",
        cascade="all,delete",
    )

    default_advance_val = db.relationship(
        "DefaultAdvanceVal",
        foreign_keys=[id],
        primaryjoin="Well.id == DefaultAdvanceVal.well_id",
        cascade="all,delete",
    )

    default_param_val = db.relationship(
        "DefaultParamVal",
        foreign_keys=[id],
        primaryjoin="Well.id == DefaultParamVal.well_id",
        cascade="all,delete",
    )

    equipment = db.relationship(
        "Equipment",
        foreign_keys=[equipment_id],
        primaryjoin="Well.equipment_id == Equipment.id",
        cascade="all,delete",
    )

    stages = db.relationship(
        "Stage",
        foreign_keys=[id],
        primaryjoin="Well.id == Stage.well_id",
        uselist=True,
        backref=backref("well", uselist=False),
        cascade="all,delete",
    )

    daily_logs = db.relationship(
        "FieldNotes",
        foreign_keys=[id],
        primaryjoin="Well.id == FieldNotes.well_id",
        uselist=True,
        cascade="all,delete",
    )

    def get_logs(self):
        logs = []
        for log in self.daily_logs:
            logs.append(
                {
                    "date": int(log.comment_timestamp.timestamp() * 1000),
                    "description": log.comment_content,
                }
            )

        return logs


class FieldNotes(db.Model, ModelMixin, TimestampMixin):
    __tablename__ = "field_notes"

    id = db.Column(db.BigInteger, autoincrement=True, primary_key=True)
    well_id = db.Column(db.Integer, nullable=False)
    comment_timestamp = db.Column(db.DateTime)
    comment_content = db.Column(db.Text)
    comment_by = db.Column(db.Text)


class FileMetadata(db.Model, ModelMixin, TimestampMixin):
    __tablename__ = "file_metadata"

    id = db.Column(db.BigInteger, autoincrement=True, primary_key=True)
    well_id = db.Column(db.Integer, nullable=False)
    meta_data_json = db.Column(JSON)
    file_name = db.Column(db.Text)
    file_path = db.Column(db.Text)
    file_type = db.Column(db.Text)
    error = db.Column(db.Text)
    is_active = db.Column(TINYINT)
    loaded_by = db.Column(db.Text)
