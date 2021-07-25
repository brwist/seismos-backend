DROP DATABASE IF EXISTS seismos;
CREATE DATABASE seismos;

USE seismos;

SET GLOBAL default_table_type = 'columnstore';

DROP TABLE IF EXISTS seismos.`backside_pressure`;
CREATE TABLE seismos.`backside_pressure`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `stage_id` int NOT NULL,
  `value` float NOT NULL,
  `created_at` datetime NOT NULL,
  `updated_at` datetime NOT NULL,
  PRIMARY KEY (`id`)
);

DROP TABLE IF EXISTS seismos.`basin_name`;
CREATE TABLE seismos.`basin_name`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `basin_name` text NOT NULL,
  `created_at` datetime NOT NULL,
  `updated_at` datetime NOT NULL,
  PRIMARY KEY (`id`)
);

DROP TABLE IF EXISTS seismos.`chem_fluids`;
CREATE TABLE seismos.`chem_fluids`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `stage_id` int NOT NULL,
  `fluid_type_id` int NULL,
  `chem_trade_name` text NULL,
  `chem_name` text NULL,
  `volume` float NULL,
  `volume_unit` text NULL,
  `volume_concentration` float NULL,
  `volume_concentration_unit` text NULL,
  `dry_total` float NULL,
  `dry_total_unit` text NULL,
  `dry_concentration` float NULL,
  `dry_concentration_unit` text NULL,
  `acid` float NULL,
  `acid_unit` text NULL,
  `clay_stabilizer` float NULL,
  `clay_stabilizer_unit` text NULL,
  `misc` text NULL,
  `bulk_modulus` float NULL,
  `bulk_modulus_unit` text NULL,
  `created_at` datetime NOT NULL,
  `updated_at` datetime NOT NULL,
  PRIMARY KEY (`id`)
);

DROP TABLE IF EXISTS seismos.`clean`;
CREATE TABLE seismos.`clean`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `stage_id` int NOT NULL,
  `total_clean_rate` float NULL,
  `total_clean_rate2` float NULL,
  `created_at` datetime NOT NULL,
  `updated_at` datetime NOT NULL,
  PRIMARY KEY (`id`)
);

DROP TABLE IF EXISTS seismos.`client`;
CREATE TABLE seismos.`client`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `client_uuid` char(36) NOT NULL,
  `client_name` text NULL,
  `customer_field_rep_id` text NULL,
  `project_id` int NULL,
  `operator_name` text NULL,
  `service_company_name` text NULL,
  `wireline_company` text NULL,
  `other_comments` text(200) NULL,
  `password` char(50) NULL,
  `title` char(50) NULL,
  `created_at` datetime NOT NULL,
  `updated_at` datetime NOT NULL,
  PRIMARY KEY (`id`)
);

DROP TABLE IF EXISTS seismos.`coil_tubing`;
CREATE TABLE seismos.`coil_tubing`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `stage_id` int NOT NULL,
  `pump_rate` float NULL,
  `pump_rate_unit` text NULL,
  `tubing_pressure` float NULL,
  `tubing_pressure_unit` text NULL,
  `depth` float NULL,
  `depth_unit` text NULL,
  `flowback_rate` float NULL,
  `flowback_unit` text NULL,
  `trip_in_out_rate` float NULL,
  `trip_in_out_rate_unit` text NULL,
  `weight_on_bit` float NULL DEFAULT NULL,
  `weight_on_bit_unit` text NULL,
  `created_at` datetime NOT NULL,
  `updated_at` datetime NOT NULL,
  PRIMARY KEY (`id`)
);

DROP TABLE IF EXISTS seismos.`county_name`;
CREATE TABLE seismos.`county_name`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `county_name` text NULL,
  `created_at` datetime NOT NULL,
  `updated_at` datetime NOT NULL,
  PRIMARY KEY (`id`)
);

DROP TABLE IF EXISTS seismos.`crew`;
CREATE TABLE seismos.`crew`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` text NOT NULL,
  `phone_number` text NULL,
  `role` enum('admin', 'manager', 'engineer') NULL,
  `manager_id` int NULL,
  `created_at` datetime NOT NULL,
  `updated_at` datetime NOT NULL,
  PRIMARY KEY (`id`)
);

DROP TABLE IF EXISTS seismos.`customer_field_rep`;
CREATE TABLE seismos.`customer_field_rep`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` text NOT NULL,
  `customer_field_rep_num` int NULL,
  `created_at` datetime NOT NULL,
  `updated_at` datetime NOT NULL,
  PRIMARY KEY (`id`)
);

DROP TABLE IF EXISTS seismos.`equipment`;
CREATE TABLE `equipment`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `trailer_id` int NULL,
  `powerpack_id` int NULL,
  `source_id` int NULL,
  `accumulator_id` int NULL,
  `hydrophones_id` int NULL,
  `transducer_id` int NULL,
  `hotspot_id` int NULL,
  `computer_id` int NULL,
  `created_at` datetime NOT NULL,
  `updated_at` datetime NOT NULL,
  PRIMARY KEY (`id`)
);

DROP TABLE IF EXISTS seismos.`ff_parameter_set`;
CREATE TABLE `ff_parameter_set`  (
  `id` int NOT NULL,
  `username` text NOT NULL,
  `date_created` datetime NULL,
  `shut_in_period_start` datetime NULL,
  `sample_rate` float NULL,
  `total_samples` float NULL,
  `tvd` float NULL,
  `viscosity` float NULL,
  `compressibility_mpa` float NULL,
  `poisson_ratio` float NULL,
  `youngs_modulus_mpa` float NULL,
  `volume_pumped` float NULL,
  `proppant_volume_pumped_bbl` float NULL,
  `average_injection_rate` float NULL,
  `tectonic_component` float NULL,
  `created_at` datetime NULL,
  `updated_at` datetime NULL,
  PRIMARY KEY (`id`)
);

DROP TABLE IF EXISTS seismos.`ff_processing_result`;
CREATE TABLE `ff_processing_result`  (
  `id` int NOT NULL,
  `timestamp` datetime NULL,
  `length` float NULL,
  `width` float NULL,
  `height` float NULL,
  `conductivity` float NULL,
  `minimum_stress` float NULL,
  `minimun_stress_gradient` float NULL,
  `net_pressure` float NULL,
  `fracture_pressure_gradient` float NULL,
  `reservoir_pressure` float NULL,
  `reservoir_pressure_gradient` float NULL,
  `pressure_match` float NULL,
  `fracture_efficiency` float NULL,
  `stress_shadow_pressure` float NULL,
  `calculated_poisson_ratio` float NULL,
  `stage_id` int NOT NULL,
  `ff_parameter_id` int NOT NULL,
  `nwb_region_size` float NULL,
  `nwb_compressibility` float NULL,
  `nwb_permeability` float NULL,
  `ff_version` text NULL,
  `created_at` datetime NULL,
  `updated_at` datetime NULL,
  PRIMARY KEY (`id`)
);

DROP TABLE IF EXISTS seismos.`field_notes`;
CREATE TABLE `field_notes`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `well_id` int NOT NULL,
  `comment_timestamp` datetime NULL,
  `comment_content` text NULL,
  `comment_by` text NULL,
  `created_at` datetime NOT NULL,
  `updated_at` datetime NOT NULL,
  PRIMARY KEY (`id`)
);

DROP TABLE IF EXISTS seismos.`fluid_type_lookup`;
CREATE TABLE `fluid_type_lookup`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `value` int NOT NULL,
  `created_at` datetime NOT NULL,
  `updated_at` datetime NOT NULL,
  PRIMARY KEY (`id`)
);

DROP TABLE IF EXISTS seismos.`formation`;
CREATE TABLE `formation`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `value` TEXT NOT NULL,
  `created_at` datetime NOT NULL,
  `updated_at` datetime NOT NULL,
  PRIMARY KEY (`id`)
);

DROP TABLE IF EXISTS seismos.`formation_top`;
CREATE TABLE `formation_top`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `well_id` int NOT NULL,
  `measured_depth` float NULL,
  `inclination` float NULL,
  `azimuth` float NULL,
  `X` float NULL,
  `Y` float NULL,
  `Z` float NULL,
  `target_upper` float NULL,
  `target_lower` float NULL,
  `l1_upper` float NULL,
  `l1_lower` float NULL,
  `l2_upper` float NULL,
  `l2_lower` float NULL,
  `l3_upper` float NULL,
  `l3_lower` float NULL,
  `l4_upper` float NULL,
  `l4_lower` float NULL,
  `l5_upper` float NULL,
  `l5_lower` float NULL,
  `l6_upper` float NULL,
  `l6_lower` float NULL,
  `l7_upper` float NULL,
  `l7_lower` float NULL,
  `l8_upper` float NULL,
  `l8_lower` float NULL,
  `l9_upper` float NULL,
  `l9_lower` float NULL,
  `l10_upper` float NULL,
  `l10_lower` float NULL,
  `json_data` json NULL,
  `created_at` datetime NULL,
  `updated_at` datetime NULL,
  PRIMARY KEY (`id`)
);

DROP TABLE IF EXISTS seismos.`formation_top_reference`;
CREATE TABLE `formation_top_reference`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `formation_top_id` int NOT NULL,
  `l1` text NULL,
  `l2` text NULL,
  `l3` text NULL,
  `l4` text NULL,
  `l5` text NULL,
  `l6` text NULL,
  `l7` text NULL,
  `l8` text NULL,
  `l9` text NULL,
  `l10` text NULL,
  `created_at` datetime NULL,
  `updated_at` datetime NULL,
  PRIMARY KEY (`id`)
);

DROP TABLE IF EXISTS seismos.`frac_design_lookup`;
CREATE TABLE `frac_design_lookup`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `value` int NOT NULL,
  `created_at` datetime NOT NULL,
  `updated_at` datetime NOT NULL,
  PRIMARY KEY (`id`)
);

DROP TABLE IF EXISTS seismos.`geophysical_properties`;
CREATE TABLE `geophysical_properties`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `well_id` int NOT NULL,
  `measured_depth` float NULL,
  `young_modulus` float NULL,
  `poisson_ratio` float NULL,
  `min_stress` float NULL,
  `dynamic_horizontal_young_modulus` float NULL,
  `static_horizontal_young_modulus` float NULL,
  `static_vertical_young_modulus` float NULL,
  `horizontal_poisson_ratio` float NULL,
  `vertical_possion_ratio` float NULL,
  `pore_pressure` float NULL,
  `tensile_strength` float NULL,
  `vertical_stress_gradient` float NULL,
  `json_data` json NULL,
  `created_at` datetime NULL,
  `updated_at` datetime NULL,
  PRIMARY KEY (`id`)
);

DROP TABLE IF EXISTS seismos.`job_info`;
CREATE TABLE `job_info`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `job_id` text,
  `job_name` text NOT NULL,
  `afe_id` int NULL,
  `job_start_date` datetime NULL,
  `job_end_date` datetime NULL,
  `job_type_id` int NULL,
  `project_id` INT,
  `created_at` datetime NOT NULL,
  `updated_at` datetime NOT NULL,
  PRIMARY KEY (`id`)
);




DROP TABLE IF EXISTS seismos.`job_type`;
CREATE TABLE `job_type`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `value` text NOT NULL,
  `created_at` datetime NOT NULL,
  `updated_at` datetime NOT NULL,
  PRIMARY KEY (`id`)
);

DROP TABLE IF EXISTS seismos.`location_info`;
CREATE TABLE `location_info`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `county_name_id` int NOT NULL,
  `basin_name_id` int NOT NULL,
  `state_id` int NOT NULL,
  `job_info_id` int,
  `created_at` datetime NOT NULL,
  `updated_at` datetime NOT NULL,
  PRIMARY KEY (`id`)
);

DROP TABLE IF EXISTS seismos.`mud_log`;
CREATE TABLE `mud_log`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `well_id` int NOT NULL,
  `measure_depth` float NULL,
  `siltstone` float NULL,
  `sand` float NULL,
  `coal` float NULL,
  `limestone` float NULL,
  `dolomite` float NULL,
  `salt` float NULL,
  `chert` float NULL,
  `chalk` float NULL,
  `anhydrite` float NULL,
  `shale` float NULL,
  `gamma_ray` float NULL,
  `clay` float NULL,
  `marl` float NULL,
  `rate_of_penetration` float NULL,
  `rpm` float NULL,
  `weight_on_bit` float NULL,
  `total_gas` float NULL,
  `methane` float NULL,
  `ethane` float NULL,
  `propane` float NULL,
  `isobutane` float NULL,
  `butane` float NULL,
  `isopentane` float NULL,
  `pentane` float NULL,
  `json_data` json NULL,
  `created_at` datetime NULL,
  `updated_at` datetime NULL,
  PRIMARY KEY (`id`)
);

DROP TABLE IF EXISTS seismos.`mwd_report`;
CREATE TABLE `mwd_report`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `well_id` int NOT NULL,
  `measured_depth` float NULL,
  `gamma_ray` float NULL,
  `created_at` datetime NULL,
  `updated_at` datetime NULL,
  PRIMARY KEY (`id`)
);

DROP TABLE IF EXISTS seismos.`nf_parameter_set`;
CREATE TABLE `nf_parameter_set`  (
  `id` int NOT NULL,
  `creation_date` datetime NULL,
  `c1_lower_bound` float NULL,
  `c1_upper_bound` float NULL,
  `c2_lower_bound` float NULL,
  `c2_upper_bound` float NULL,
  `c3_lower_bound` float NULL,
  `c3_upper_bound` float NULL,
  `direct_sources_start` datetime NULL,
  `first_reflection_start` datetime NULL,
  `direct_source_num_samples` int NULL,
  `first_reflection_num_samples` int NULL,
  `source_duration` float NULL,
  `min_pulse_separation` float NULL,
  `compressbility` float NULL,
  `deconvolution_override` text NULL,
  `deconvolution_noise_level` float NULL,
  `nf_shot_finder_versaion` text NULL,
  `nf_inversion_version` text NULL,
  `shot_id` int NULL,
  `created_at` datetime NULL,
  `updated_at` datetime NULL,
  PRIMARY KEY (`id`)
);

DROP TABLE IF EXISTS seismos.`nf_processing_result`;
CREATE TABLE `nf_processing_result`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `stage_id` int NOT NULL,
  `timestamp` datetime NULL,
  `user_id` text NULL,
  `c0` float NULL,
  `c1` float NULL,
  `c2` float NULL,
  `c3` float NULL,
  `q0` float NULL,
  `q1` float NULL,
  `q2` float NULL,
  `q3` float NULL,
  `fit_error` float NULL,
  `nf_param_id` int NULL,
  `created_at` datetime NULL,
  `updated_at` datetime NULL,
  PRIMARY KEY (`id`)
);

DROP TABLE IF EXISTS seismos.`pad`;
CREATE TABLE `pad`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `pad_uuid` char(36) NOT NULL,
  `project_id` int NOT NULL,
  `pad_name` text NOT NULL,
  `number_of_wells` int NULL,
  `well_spacing` float NULL,
  `created_at` datetime NOT NULL,
  `updated_at` datetime NOT NULL,
  PRIMARY KEY (`id`)
);

DROP TABLE IF EXISTS seismos.`perforation`;
CREATE TABLE `perforation`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `stage_id` int NOT NULL,
  `order_num` int NULL,
  `ordinal` text NULL,
  `top_measured_depth` text NULL,
  `bottom_measured_depth` text NULL,
  `depth_unit` text NULL,
  `shot_number` int NULL,
  `shot_density` text NULL,
  `shot_density_unit` text NULL,
  `shot_count` text NULL,
  `phasing` text NULL,
  `conveyance_method` text NULL,
  `charge_type` text NULL,
  `charge_size` double NULL,
  `charge_size_unit` text NULL,
  `estimated_hole_diamter` text NULL,
  `estimated_hole_diameter_unit` text NULL,
  `created_at` datetime NOT NULL,
  `updated_at` datetime NOT NULL,
  PRIMARY KEY (`id`)
);

DROP TABLE IF EXISTS seismos.`plug_depth_unit_lookup`;
CREATE TABLE `plug_depth_unit_lookup`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `value` text NOT NULL,
  `created_at` datetime NOT NULL,
  `updated_at` datetime NOT NULL,
  PRIMARY KEY (`id`)
);

DROP TABLE IF EXISTS seismos.`plug_name_lookup`;
CREATE TABLE `plug_name_lookup`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `value` float NOT NULL,
  `created_at` datetime NOT NULL,
  `updated_at` datetime NOT NULL,
  PRIMARY KEY (`id`)
);

DROP TABLE IF EXISTS seismos.`project`;
CREATE TABLE `project`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `project_uuid` char(36) NOT NULL,
  `project_name` text NOT NULL,
  `client_id` int NOT NULL,
  `equipment_id` int NULL,
  `created_at` datetime NOT NULL,
  `updated_at` datetime NOT NULL,
  PRIMARY KEY (`id`)
);


DROP TABLE IF EXISTS seismos.`project_crew`;
CREATE TABLE `project_crew`  (
  `project_crew_id` int NOT NULL AUTO_INCREMENT,
  `project_id` int NOT NULL,
  `crew_id` int NOT NULL,
  `created_at` datetime NOT NULL,
  `updated_at` datetime NOT NULL,
  PRIMARY KEY (`project_crew_id`)
);

DROP TABLE IF EXISTS seismos.`proppant`;
CREATE TABLE `proppant`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `stage_id` int NOT NULL,
  `proppant_name_id` int NOT NULL,
  `prop_mass` float NULL,
  `mass_unit` text NULL,
  `material` text NULL,
  `mesh_size` float NULL,
  `avg_concentration` float NULL,
  `avg_concentration_unit` text NULL,
  `max_concentration` float NULL,
  `max_concentration_unit` text NULL,
  `proppant_type_start_time` datetime NULL,
  `proppant_end_start_time` datetime NULL,
  `created_at` datetime NOT NULL,
  `updated_at` datetime NOT NULL,
  PRIMARY KEY (`id`)
);

DROP TABLE IF EXISTS seismos.`proppant_lookup`;
CREATE TABLE `proppant_lookup`  (
  `id` int NOT NULL,
  `proppant_name` text NOT NULL,
  `created_at` datetime NOT NULL,
  `updated_at` datetime NOT NULL,
  PRIMARY KEY (`id`)
);

DROP TABLE IF EXISTS seismos.`pumpdown`;
CREATE TABLE `pumpdown`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `stage_id` int NOT NULL,
  `pressure` float NULL,
  `rate` float NULL,
  `total_pumdown_value` float NULL,
  `created_at` datetime NOT NULL,
  `updated_at` datetime NOT NULL,
  PRIMARY KEY (`id`)
);

DROP TABLE IF EXISTS seismos.`pumping`;
CREATE TABLE `pumping`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `stage_id` int NOT NULL,
  `total_slurry_volume` float NULL,
  `total_clean_volume` float NULL,
  `treating_pressure` float NULL,
  `clean_rate` float NULL,
  `slurry_rate` float NULL,
  `surface_prop_conc` float NULL,
  `bottom_prop_conc` float NULL,
  `100_mesh` float NULL,
  `30_50_mesh` float NULL,
  `40_70_mesh` float NULL,
  `20_40_mesh` float NULL,
  `micro_prop` float NULL,
  `bottom_pressure` float NULL,
  `net_pressure` float NULL,
  `backside_pressure` float NULL,
  `friction_reducer` float NULL,
  `gel` float NULL,
  `crosslink` float NULL,
  `created_at` datetime NULL,
  `updated_at` datetime NULL,
  PRIMARY KEY (`id`)
);

DROP TABLE IF EXISTS seismos.`quality_control`;
CREATE TABLE `quality_control`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `project_id` int NOT NULL,
  `is_checked` bool NULL,
  `checked_by` text NULL,
  `created_at` datetime NOT NULL,
  `updated_at` datetime NOT NULL,
  PRIMARY KEY (`id`)
);

DROP TABLE IF EXISTS seismos.`slurry`;
CREATE TABLE `slurry`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `stage_id` int NOT NULL,
  `total_slurry_rate` float NULL,
  `total_slurry_rate2` float NULL,
  `created_at` datetime NOT NULL,
  `updated_at` datetime NOT NULL,
  PRIMARY KEY (`id`)
);

DROP TABLE IF EXISTS seismos.`software`;
CREATE TABLE `software`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `project_id` int NULL,
  `inpute_app_version` float NULL,
  `processing_version` float NULL,
  `db_version` float NULL,
  `created_at` datetime NOT NULL,
  `updated_at` datetime NOT NULL,
  PRIMARY KEY (`id`)
);

DROP TABLE IF EXISTS seismos.`stage`;
CREATE TABLE `stage`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `stage_uuid` char(36) NOT NULL,
  `well_id` int NULL,
  `stage_number` integer NULL,
  `number_of_cluster` integer NULL,
  `stage_start_time` datetime NULL,
  `stage_end_time` datetime NULL,
  `plug_depth` float NULL,
  `frac_design_id` integer NULL,
  `calc_net_pressure_result` float NULL,
  `observed_net_pressure` float NULL,
  `inline_density` float NULL,
  `blender_density` float NULL,
  `calc_bh_density` float NULL,
  `bottomhole_bhp` float NULL,
  `bottomhole_bht` float NULL,
  `frac_model_bhp` float NULL,
  `total_pumpdown_volume` float NULL,
  `formation_poisson_ratio` float NULL,
  `formation_prgradient` double NULL,
  `formation_overburden_num` double NULL,
  `formation_pumping_fluid_viscosity` float NULL,
  `formation_fluid_density` float NULL,
  `formation_fluid_type` integer NULL,
  `formation_tectonic_gradient` double NULL,
  `formation_pore_pressure` float NULL,
  `connect_ops_risk` float NULL,
  `connect_efficiency` float NULL,
  `connect_condition` float NULL,
  `ses_data_colllection_id` integer NULL,
  `ses_pressure_sensor` float NULL,
  `ses_hydrophone_sensor_hi` float NULL,
  `ses_hydrophone_sensor_low` float NULL,
  `ses_pulse_trigger` datetime NULL,
  `ses_wave_pulse_type` integer NULL,
  `ses_pre_frac_pulse_notes` text NULL,
  `ses_pre_frac_num_pulses` integer NULL,
  `ses_pre_frac_start_time` datetime NULL,
  `ses_pre_frac_end_time` datetime NULL,
  `post_frac_start_time` datetime NULL,
  `post_frac_end_time` datetime NULL,
  `post_frac_num_pulses` integer NULL,
  `digital_signal_flag` integer NULL,
  `pressure_counter` double NULL,
  `post_frac_pulse_notes` text NULL,
  `other_notes` text NULL,
  `num_reflections` integer NULL,
  `plug_name` integer NULL,
  `plug_ordinal` integer NULL,
  `plug_top_measured_depth` float NULL,
  `plug_type` integer NULL,
  `plug_depth_unit_id` integer NULL,
  `plug_diameter` float NULL,
  `plug_diameter_unit` text NULL,
  `plug_manufacturer` text NULL,
  `plug_model` integer NULL,
  `sleeve_name` text NULL,
  `sleeve_ordinal` integer NULL,
  `sleeve_top_measured_depth` float NULL,
  `sleeve_bottom_measure_depth` float NULL,
  `sleeve_depth_unit` text NULL,
  `sleeve_port_size` float NULL,
  `sleeve_port_size_unit` text NULL,
  `sleeve_ball_size` float NULL,
  `sleeve_ball_size_unit` text NULL,
  `sleeve_seat_id` text NULL,
  `sleeve_manufacturer` text NULL,
  `sleeve_model` text NULL,
  `sleeve_toe_shift_pressure` integer NULL,
  `sleeve_toe_burst_pressure` integer NULL,
  `created_at` datetime,
  `updated_at` datetime,
  PRIMARY KEY(`id`)
);

DROP TABLE IF EXISTS seismos.`state`;
CREATE TABLE `state`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `value` text NOT NULL,
  `created_at` datetime NOT NULL,
  `updated_at` datetime NOT NULL,
  PRIMARY KEY (`id`)
);

DROP TABLE IF EXISTS seismos.`survey_report`;
CREATE TABLE `survey_report`  (
  `id` int NOT NULL,
  `well_id` int NOT NULL,
  `measured_depth` float NULL,
  `inclination` float NULL,
  `azimuth` float NULL,
  `tvd` float NULL,
  `ns` float NULL,
  `ew` float NULL,
  `vs` float NULL,
  `dls` float NULL,
  `closure_direction` float NULL,
  `dogleg_severity` float NULL,
  `json_data` json NULL,
  `created_at` datetime NULL,
  `updated_at` datetime NULL,
  PRIMARY KEY (`id`)
);

DROP TABLE IF EXISTS seismos.`treating_pressure`;
CREATE TABLE `treating_pressure`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `stage_id` int NOT NULL,
  `wellhead_pressure` float NULL,
  `treating_pressure` float NULL,
  `annulus_pressure` float NULL,
  `calc_hydrostatic_pressure` float NULL,
  `calc_bhp` float NULL,
  `created_at` datetime NOT NULL,
  `updated_at` datetime NOT NULL,
  PRIMARY KEY (`id`)
);

DROP TABLE IF EXISTS seismos.`well`;
CREATE TABLE `well`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `well_uuid` char(36) NOT NULL,
  `pad_id` int NOT NULL,
  `well_name` text NULL,
  `well_api` text NULL,
  `formation_id` int NULL,
  `num_stages` integer NULL,
  `total_planned_stage` integer NULL,
  `total_perfs` integer NULL,
  `total_clusters` integer NULL,
  `frac_system` text NULL,
  `fluid_system` text NULL,
  `well_start_time` datetime NULL,
  `well_end_time` datetime NULL,
  `bottom_hole_latitude` float NULL,
  `bottom_hole_longitude` float NULL,
  `surface_longitude` float NULL,
  `surface_latitude` float NULL,
  `lateral_length` float NULL,
  `lateral_length_unit` text NULL,
  `measured_depth` float NULL,
  `vertical_depth` float NULL,
  `vertical_depth_unit` text NULL,
  `lat` text NULL,
  `easting` text NULL,
  `northing` text NULL,
  `estimated_surface_vol` float NULL,
  `estimated_bbls` float NULL,
  `estimated_gallons` float NULL,
  `casing_od` float NULL,
  `casing_wt` float NULL,
  `casing_id` float NULL,
  `casing_depth_md` float NULL,
  `casing_tol` float NULL,
  `liner1_od` float NULL,
  `liner1_wt` float NULL,
  `liner1_id` float NULL,
  `liner1_depth_md` float NULL,
  `liner1_tol` float NULL,
  `liner2_od` float NULL,
  `liner2_wt` float NULL,
  `liner2_id` float NULL,
  `liner2_depth_md` float NULL,
  `liner2_tol` float NULL,
  `measured_depth_unit` text NULL,
  `created_at` datetime NOT NULL,
  `updated_at` datetime NOT NULL,
  PRIMARY KEY (`id`)
);

DROP TABLE IF EXISTS seismos.`wireline`;
CREATE TABLE `wireline`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `stage_id` int NOT NULL,
  `ccl` float NULL,
  `current` float NULL,
  `line_speed` float NULL,
  `line_tension` float NULL,
  `trigger_perfs` datetime NULL,
  `weight` float NULL,
  `depth` float NULL,
  `voltage` float NULL,
  `timestamp` datetime NULL,
  `elapsed_time` datetime NULL,
  `created_at` datetime NOT NULL,
  `updated_at` datetime NOT NULL,
  PRIMARY KEY (`id`)
);

DROP TABLE IF EXISTS seismos.`user`;
CREATE TABLE `user`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `email` char(255) NOT NULL,
  `password_hash` char(255) NOT NULL,
  `username` char(60) NOT NULL,

  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
  PRIMARY KEY (`id`)
);

DROP TABLE IF EXISTS seismos.`user_project`;
CREATE TABLE `user_project`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `project_id` int NOT NULL,

  PRIMARY KEY (`id`)
);
