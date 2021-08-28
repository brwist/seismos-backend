from app.models.mixin_models import ModelMixin
from sqlalchemy.dialects.mysql import INTEGER
from app import db


class TrackingSheet(ModelMixin, db.Model):

    __tablename__ = "tracking_sheet"

    id = db.Column(INTEGER(unsigned=True), primary_key=True)
    well_id = db.Column(db.Integer, nullable=False)
    stage = db.Column(INTEGER(unsigned=True), nullable=False)
    stage_tracking_id = db.Column(INTEGER(unsigned=True), nullable=False)
    perforation_interval_information_id = db.Column(INTEGER(unsigned=True), nullable=False)
    stage_data_id = db.Column(INTEGER(unsigned=True), nullable=False)
    active_data_id = db.Column(INTEGER(unsigned=True), nullable=False)
    notes_id = db.Column(INTEGER(unsigned=True), nullable=False)
    approved = db.Column(db.Boolean, default=False)

    stage_tracking = db.relationship(
        "StageTracking",
        foreign_keys=[stage_tracking_id],
        primaryjoin="TrackingSheet.stage_tracking_id == StageTracking.id"
    )

    perforation_interval_information = db.relationship(
        "PerforationIntervalInformation",
        foreign_keys=[perforation_interval_information_id],
        primaryjoin="TrackingSheet.perforation_interval_information_id == PerforationIntervalInformation.id",
    )

    stage_data = db.relationship(
        "StageData",
        foreign_keys=[stage_data_id],
        primaryjoin="TrackingSheet.stage_data_id == StageData.id"
    )

    active_data = db.relationship(
        "ActiveData",
        foreign_keys=[active_data_id],
        primaryjoin="TrackingSheet.active_data_id == ActiveData.id"
    )

    notes = db.relationship(
        "Notes",
        foreign_keys=[notes_id],
        primaryjoin="TrackingSheet.notes_id == Notes.id"
    )

    def to_json(self):
        propant_data = []
        for pr_data in self.stage_data.propant_data:
            propant_data.append({
                "bulk_density": pr_data.bulk_density,
                "description": pr_data.description,
                "specific_gravity": pr_data.specific_gravity
            })

        stage_start_time = self.stage_data.stage_start_time.timestamp()
        stage_end_time = self.stage_data.stage_end_time.timestamp()

        return {
            "stage": self.stage,
            "stage_tracking": {
                "date": self.stage_tracking.date.timestamp() * 1000,
                "customer": self.stage_tracking.customer,
                "well": self.stage_tracking.well,
                "stage": self.stage_tracking.stage,
                "bht_f": self.stage_tracking.bht_f,
                "bht_psi": self.stage_tracking.bht_psi,
                "frac_design": self.stage_tracking.frac_design,
                "field_engineer": {
                    "days": self.stage_tracking.field_engineer.days,
                    "nights": self.stage_tracking.field_engineer.nights
                },

                "plug_type": self.stage_tracking.plug_type,
                "plug_seat_technique": self.stage_tracking.plug_seat_technique,
                "did_an_event_occur": self.stage_tracking.did_an_event_occur,
                "seismos_data_collection": self.stage_tracking.seismos_data_collection
            },

            "perforation_interval_information": {
                "top_perf": self.perforation_interval_information.top_perf,
                "bottom_perf": self.perforation_interval_information.bottom_perf,
                "plug_depth": self.perforation_interval_information.plug_depth,
                "n_clusters": self.perforation_interval_information.n_clusters,
                "perf_gun_description": self.perforation_interval_information.perf_gun_description,
                "perf_daiameter": self.perforation_interval_information.perf_daiameter,
                "spf": self.perforation_interval_information.spf,
                "pumped_diverter": self.perforation_interval_information.pumped_diverter,
                "diverter_type": self.perforation_interval_information.diverter_type,
                "acid": self.perforation_interval_information.acid,
                "displacement_volume": {
                    "top_perf": self.perforation_interval_information.displacement_volume.top_perf,
                    "bottom_perf": self.perforation_interval_information.displacement_volume.bottom_perf,
                    "plug": self.perforation_interval_information.displacement_volume.plug,
                }
            },

            "stage_data": {
                "stage_start_time": int(stage_start_time) * 1000,
                "stage_end_time": int(stage_end_time) * 1000,
                "opening_well": self.stage_data.opening_well,
                "isip": self.stage_data.isip,
                "fluid_parameters": {
                    "base_fluid_type": self.stage_data.fluid_parameters.base_fluid_type,
                    "base_fluid_density": self.stage_data.fluid_parameters.base_fluid_density,
                    "max_conc_density": self.stage_data.fluid_parameters.max_conc_density
                },

                "fluids_injected_into_formation": {
                    "last": {
                        "description": self.stage_data.fluids_injected_into_formation.last_description,
                        "bbls": self.stage_data.fluids_injected_into_formation.last_bbls,
                        "ppg": self.stage_data.fluids_injected_into_formation.last_ppg
                    },

                    "second_to_last": {
                        "description": self.stage_data.fluids_injected_into_formation.second_to_last_description,
                        "bbls": self.stage_data.fluids_injected_into_formation.second_to_last_bbls,
                        "ppg": self.stage_data.fluids_injected_into_formation.second_to_last_ppg
                    },

                    "third_to_last": {
                        "description": self.stage_data.fluids_injected_into_formation.third_to_last_description,
                        "bbls": self.stage_data.fluids_injected_into_formation.third_to_last_bbls,
                        "ppg": self.stage_data.fluids_injected_into_formation.third_to_last_ppg
                    }
                },
                "propant_data": propant_data,

                "pumping_summary": {
                    "max_prop_conc": {
                        "design": self.stage_data.pumping_summary.max_prop_conc_design,
                        "actual": self.stage_data.pumping_summary.max_prop_conc_actual
                    },

                    "total_pad_volume": {
                        "design": self.stage_data.pumping_summary.total_pad_volume_design,
                        "actual": self.stage_data.pumping_summary.total_pad_volume_actual
                    },
                    "total_clean_fluid_volume":  {
                        "design": self.stage_data.pumping_summary.total_clean_fluid_volume_design,
                        "actual": self.stage_data.pumping_summary.total_clean_fluid_volume_actual
                    },
                    "total_forty_seventy":  {
                        "design": self.stage_data.pumping_summary.total_forty_seventy_design,
                        "actual": self.stage_data.pumping_summary.total_forty_seventy_actual
                    },
                    "total_sand":  {
                        "design": self.stage_data.pumping_summary.total_sand_design,
                        "actual": self.stage_data.pumping_summary.total_sand_actual
                    },
                    "acid_volume":  {
                        "design": self.stage_data.pumping_summary.acid_volume_design,
                        "actual": self.stage_data.pumping_summary.acid_volume_actual
                    },
                    "flush_volume":  {
                        "design": self.stage_data.pumping_summary.flush_volume_design,
                        "actual": self.stage_data.pumping_summary.flush_volume_actual
                    },
                    "slurry_volume":  {
                        "design": self.stage_data.pumping_summary.slurry_volume_design,
                        "actual": self.stage_data.pumping_summary.slurry_volume_actual
                    }
                }
            },

            "active_data": {
                "pilsing_parameters": {
                    "wave_type": self.active_data.pilsing_parameters_wave_type,
                    "periods": self.active_data.pilsing_parameters_periods,
                    "freq": self.active_data.pilsing_parameters_freq,
                    "offset": self.active_data.pilsing_parameters_offset,
                    "amplitude": self.active_data.pilsing_parameters_amplitude
                },

                "pre_frac_pulses": {
                    "start_time": int(self.active_data.pre_frac_pulses_start_time.timestamp()) * 1000,
                    "end_time": int(self.active_data.pre_frac_pulses_end_time.timestamp()) * 1000,
                    "n_pulses": self.active_data.pre_frac_pulses_n_pulses
                },

                "post_frac_pulses": {
                    "start_time": int(self.active_data.post_frac_pulses_start_time.timestamp()) * 1000,
                    "end_time": int(self.active_data.post_frac_pulses_end_time.timestamp()) * 1000,
                    "n_pulses": self.active_data.post_frac_pulses_n_pulses
                }
            },

            "notes": {
                "pre_frac_pulse": self.notes.pre_frac_pulse,
                "post_frac_pulse": self.notes.post_frac_pulse,
                "other": self.notes.other
            }
        }


class StageTracking(ModelMixin, db.Model):

    __tablename__ = "stage_tracking"

    id = db.Column(INTEGER(unsigned=True), primary_key=True)
    date = db.Column(db.DateTime)
    customer = db.Column(db.String(255))
    well = db.Column(db.String(255))
    stage = db.Column(db.String(255))
    bht_f = db.Column(db.String(255))
    bht_psi = db.Column(db.String(255))
    frac_design = db.Column(db.String(255))
    field_engineer_id = db.Column(INTEGER(unsigned=True))
    plug_type = db.Column(db.String(255))
    plug_seat_technique = db.Column(db.String(255))
    did_an_event_occur = db.Column(db.String(255))
    seismos_data_collection = db.Column(db.String(255))

    field_engineer = db.relationship(
        "FieldEngineer",
        foreign_keys=[field_engineer_id],
        primaryjoin="StageTracking.field_engineer_id == FieldEngineer.id"
    )


class FieldEngineer(ModelMixin, db.Model):

    __tablename__ = "field_engineer"

    id = db.Column(INTEGER(unsigned=True), primary_key=True)
    days = db.Column(db.String(255))
    nights = db.Column(db.String(255))


class PerforationIntervalInformation(ModelMixin, db.Model):

    __tablename__ = "perforation_interval_information"

    id = db.Column(INTEGER(unsigned=True), primary_key=True)
    top_perf = db.Column(db.String(255))
    bottom_perf = db.Column(db.String(255))
    plug_depth = db.Column(db.String(255))
    n_clusters = db.Column(INTEGER(unsigned=True))
    perf_gun_description = db.Column(db.String(255))
    perf_daiameter = db.Column(db.String(255))
    spf = db.Column(db.String(255))
    pumped_diverter = db.Column(db.String(255))
    diverter_type = db.Column(db.String(255))
    acid = db.Column(db.String(255))
    displacement_volume_id = db.Column(INTEGER(unsigned=True))

    displacement_volume = db.relationship(
        "DisplacementVolume",
        foreign_keys=[displacement_volume_id],
        primaryjoin="PerforationIntervalInformation.displacement_volume_id == DisplacementVolume.id"
    )


class DisplacementVolume(ModelMixin, db.Model):

    __tablename__ = "displacement_volume"

    id = db.Column(INTEGER(unsigned=True), primary_key=True)
    top_perf = db.Column(db.String(255))
    bottom_perf = db.Column(db.String(255))
    plug = db.Column(db.String(255))


class StageData(ModelMixin, db.Model):

    __tablename__ = "stage_data"

    id = db.Column(INTEGER(unsigned=True), primary_key=True)
    stage_start_time = db.Column(db.DateTime)
    stage_end_time = db.Column(db.DateTime)
    opening_well = db.Column(db.String(255))
    isip = db.Column(db.String(255))
    fluid_parameters_id = db.Column(INTEGER(unsigned=True))
    fluids_injected_into_formation_id = db.Column(INTEGER(unsigned=True))
    pumping_summary_id = db.Column(INTEGER(unsigned=True))

    fluid_parameters = db.relationship(
        "FluidParameters",
        foreign_keys=[fluid_parameters_id],
        primaryjoin="StageData.fluid_parameters_id == FluidParameters.id"
    )

    fluids_injected_into_formation = db.relationship(
        "FluidsInjectedIntoFormation",
        foreign_keys=[fluids_injected_into_formation_id],
        primaryjoin="StageData.fluids_injected_into_formation_id == FluidsInjectedIntoFormation.id"
    )

    propant_data = db.relationship(
        "PropantData",
        foreign_keys=[id],
        primaryjoin="StageData.id == PropantData.stage_data_id",
        uselist=True,
        lazy=True,
    )

    pumping_summary = db.relationship(
        "PumpingSummary",
        foreign_keys=[pumping_summary_id],
        primaryjoin="StageData.pumping_summary_id == PumpingSummary.id"
    )


class FluidParameters(ModelMixin, db.Model):

    __tablename__ = "fluid_parameters"

    id = db.Column(INTEGER(unsigned=True), primary_key=True)
    base_fluid_type = db.Column(db.String(255))
    base_fluid_density = db.Column(db.String(255))
    max_conc_density = db.Column(db.String(255))


class FluidsInjectedIntoFormation(ModelMixin, db.Model):

    __tablename__ = "fluids_injected_into_formation"

    id = db.Column(INTEGER(unsigned=True), primary_key=True)
    last_description = db.Column(db.String(255))
    last_bbls = db.Column(db.String(255))
    last_ppg = db.Column(db.String(255))

    second_to_last_description = db.Column(db.String(255))
    second_to_last_bbls = db.Column(db.String(255))
    second_to_last_ppg = db.Column(db.String(255))

    third_to_last_description = db.Column(db.String(255))
    third_to_last_bbls = db.Column(db.String(255))
    third_to_last_ppg = db.Column(db.String(255))


class PropantData(ModelMixin, db.Model):

    __tablename__ = "propant_data"

    id = db.Column(INTEGER(unsigned=True), primary_key=True)
    stage_data_id = db.Column(INTEGER(unsigned=True))
    description = db.Column(db.String(255))
    specific_gravity = db.Column(db.String(255))
    bulk_density = db.Column(db.String(255))


class PumpingSummary(ModelMixin, db.Model):
    __tablename__ = "pumping_summary"

    id = db.Column(INTEGER(unsigned=True), primary_key=True)
    max_prop_conc_design = db.Column(db.String(255))
    max_prop_conc_actual = db.Column(db.String(255))

    total_pad_volume_design = db.Column(db.String(255))
    total_pad_volume_actual = db.Column(db.String(255))

    total_clean_fluid_volume_design = db.Column(db.String(255))
    total_clean_fluid_volume_actual = db.Column(db.String(255))

    total_forty_seventy_design = db.Column(db.String(255))
    total_forty_seventy_actual = db.Column(db.String(255))

    total_sand_design = db.Column(db.String(255))
    total_sand_actual = db.Column(db.String(255))

    acid_volume_design = db.Column(db.String(255))
    acid_volume_actual = db.Column(db.String(255))

    flush_volume_design = db.Column(db.String(255))
    flush_volume_actual = db.Column(db.String(255))

    slurry_volume_design = db.Column(db.String(255))
    slurry_volume_actual = db.Column(db.String(255))


class ActiveData(ModelMixin, db.Model):
    __tablename__ = "active_data"

    id = db.Column(INTEGER(unsigned=True), primary_key=True)
    pilsing_parameters_wave_type = db.Column(db.String(255))
    pilsing_parameters_periods = db.Column(db.String(255))
    pilsing_parameters_freq = db.Column(db.String(255))
    pilsing_parameters_offset = db.Column(db.String(255))
    pilsing_parameters_amplitude = db.Column(db.String(255))

    pre_frac_pulses_start_time = db.Column(db.DateTime)
    pre_frac_pulses_end_time = db.Column(db.DateTime)
    pre_frac_pulses_n_pulses = db.Column(INTEGER(unsigned=True))

    post_frac_pulses_start_time = db.Column(db.DateTime)
    post_frac_pulses_end_time = db.Column(db.DateTime)
    post_frac_pulses_n_pulses = db.Column(INTEGER(unsigned=True))


class Notes(ModelMixin, db.Model):
    __tablename__ = "notes"

    id = db.Column(INTEGER(unsigned=True), primary_key=True)
    pre_frac_pulse = db.Column(db.Text)
    post_frac_pulse = db.Column(db.Text)
    other = db.Column(db.Text)
