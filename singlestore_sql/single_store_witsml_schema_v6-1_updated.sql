
DROP DATABASE IF EXISTS seismos;
CREATE DATABASE seismos;

USE seismos;
---SET GLOBAL default_table_type = 'columnstore';

DROP TABLE IF EXISTS seismos.`user`;
CREATE TABLE `user`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `email` char(255) NOT NULL,
  `password_hash` char(255) NOT NULL,
  `username` char(60) NOT NULL,

  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
  PRIMARY KEY (`id`)
);

--
-- Table structure for table `backside_pressure`
--

DROP TABLE IF EXISTS `backside_pressure`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `backside_pressure` (
  `id` bigint(11) NOT NULL AUTO_INCREMENT,
  `stage_id` int(11) NOT NULL,
  `value` float NOT NULL,
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `updated_at` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  UNIQUE KEY `PRIMARY` (`id`) USING HASH,
  KEY `stage_id` (`stage_id`) USING CLUSTERED COLUMNSTORE,
  SHARD KEY `__SHARDKEY` (`id`)
) AUTOSTATS_CARDINALITY_MODE=INCREMENTAL AUTOSTATS_HISTOGRAM_MODE=CREATE AUTOSTATS_SAMPLING=ON SQL_MODE='STRICT_ALL_TABLES';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `basin_name`
--

DROP TABLE IF EXISTS `basin_name`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `basin_name` (
  `id` bigint(11) NOT NULL AUTO_INCREMENT,
  `basin_name` text CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `updated_at` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  UNIQUE KEY `PRIMARY` (`id`) USING HASH,
  KEY `id` (`id`) USING CLUSTERED COLUMNSTORE,
  SHARD KEY `__SHARDKEY` (`id`)
) AUTOSTATS_CARDINALITY_MODE=INCREMENTAL AUTOSTATS_HISTOGRAM_MODE=CREATE AUTOSTATS_SAMPLING=ON SQL_MODE='STRICT_ALL_TABLES';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `chem_fluids`
--

DROP TABLE IF EXISTS `chem_fluids`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `chem_fluids` (
  `id` bigint(11) NOT NULL AUTO_INCREMENT,
  `stage_id` int(11) NOT NULL,
  `fluid_type_id` int(11) DEFAULT NULL,
  `chem_trade_name` text CHARACTER SET utf8 COLLATE utf8_general_ci,
  `chem_name` text CHARACTER SET utf8 COLLATE utf8_general_ci,
  `volume` float DEFAULT NULL,
  `volume_unit` text CHARACTER SET utf8 COLLATE utf8_general_ci,
  `volume_concentration` float DEFAULT NULL,
  `volume_concentration_unit` text CHARACTER SET utf8 COLLATE utf8_general_ci,
  `dry_total` float DEFAULT NULL,
  `dry_total_unit` text CHARACTER SET utf8 COLLATE utf8_general_ci,
  `dry_concentration` float DEFAULT NULL,
  `dry_concentration_unit` text CHARACTER SET utf8 COLLATE utf8_general_ci,
  `acid` float DEFAULT NULL,
  `acid_unit` text CHARACTER SET utf8 COLLATE utf8_general_ci,
  `clay_stabilizer` float DEFAULT NULL,
  `clay_stabilizer_unit` text CHARACTER SET utf8 COLLATE utf8_general_ci,
  `misc` text CHARACTER SET utf8 COLLATE utf8_general_ci,
  `bulk_modulus` float DEFAULT NULL,
  `base_fluid_density` VARCHAR(255) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `base_fluid_type` VARCHAR(255) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `max_conc_density` VARCHAR(255) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `bulk_modulus_unit` text CHARACTER SET utf8 COLLATE utf8_general_ci,
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `updated_at` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  UNIQUE KEY `PRIMARY` (`id`) USING HASH,
  KEY `stage_id` (`stage_id`) USING CLUSTERED COLUMNSTORE,
  SHARD KEY `__SHARDKEY` (`id`)
) AUTOSTATS_CARDINALITY_MODE=INCREMENTAL AUTOSTATS_HISTOGRAM_MODE=CREATE AUTOSTATS_SAMPLING=ON SQL_MODE='STRICT_ALL_TABLES';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `clean`
--

DROP TABLE IF EXISTS `clean`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `clean` (
  `id` bigint(11) NOT NULL AUTO_INCREMENT,
  `stage_id` int(11) NOT NULL,
  `total_clean_rate` float DEFAULT NULL,
  `total_clean_rate2` float DEFAULT NULL,
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `updated_at` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  UNIQUE KEY `PRIMARY` (`id`) USING HASH,
  KEY `stage_id` (`stage_id`) USING CLUSTERED COLUMNSTORE,
  SHARD KEY `__SHARDKEY` (`id`)
) AUTOSTATS_CARDINALITY_MODE=INCREMENTAL AUTOSTATS_HISTOGRAM_MODE=CREATE AUTOSTATS_SAMPLING=ON SQL_MODE='STRICT_ALL_TABLES';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `client`
--

DROP TABLE IF EXISTS `client`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `client` (
  `id` bigint(11) NOT NULL AUTO_INCREMENT,
  `client_uuid` char(36) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `client_name` text CHARACTER SET utf8 COLLATE utf8_general_ci,
  `customer_field_rep_id` text CHARACTER SET utf8 COLLATE utf8_general_ci,
  `project_id` int(11) DEFAULT NULL,
  `operator_name` text CHARACTER SET utf8 COLLATE utf8_general_ci,
  `service_company_name` text CHARACTER SET utf8 COLLATE utf8_general_ci,
  `wireline_company` text CHARACTER SET utf8 COLLATE utf8_general_ci,
  `other_comments` text CHARACTER SET utf8 COLLATE utf8_general_ci,
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `updated_at` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  UNIQUE KEY `PRIMARY` (`id`) USING HASH,
  KEY `client_uuid` (`client_uuid`) USING CLUSTERED COLUMNSTORE,
  SHARD KEY `__SHARDKEY` (`id`)
) AUTOSTATS_CARDINALITY_MODE=INCREMENTAL AUTOSTATS_HISTOGRAM_MODE=CREATE AUTOSTATS_SAMPLING=ON SQL_MODE='STRICT_ALL_TABLES';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `coil_tubing`
--

DROP TABLE IF EXISTS `coil_tubing`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `coil_tubing` (
  `id` bigint(11) NOT NULL AUTO_INCREMENT,
  `stage_id` int(11) NOT NULL,
  `pump_rate` float DEFAULT NULL,
  `pump_rate_unit` text CHARACTER SET utf8 COLLATE utf8_general_ci,
  `tubing_pressure` float DEFAULT NULL,
  `tubing_pressure_unit` text CHARACTER SET utf8 COLLATE utf8_general_ci,
  `depth` float DEFAULT NULL,
  `depth_unit` text CHARACTER SET utf8 COLLATE utf8_general_ci,
  `flowback_rate` float DEFAULT NULL,
  `flowback_unit` text CHARACTER SET utf8 COLLATE utf8_general_ci,
  `trip_in_out_rate` float DEFAULT NULL,
  `trip_in_out_rate_unit` text CHARACTER SET utf8 COLLATE utf8_general_ci,
  `weight_on_bit` float DEFAULT NULL,
  `weight_on_bit_unit` text CHARACTER SET utf8 COLLATE utf8_general_ci,
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `updated_at` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  UNIQUE KEY `PRIMARY` (`id`) USING HASH,
  KEY `stage_id` (`stage_id`) USING CLUSTERED COLUMNSTORE,
  SHARD KEY `__SHARDKEY` (`id`)
) AUTOSTATS_CARDINALITY_MODE=INCREMENTAL AUTOSTATS_HISTOGRAM_MODE=CREATE AUTOSTATS_SAMPLING=ON SQL_MODE='STRICT_ALL_TABLES';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `county_name`
--

DROP TABLE IF EXISTS `county_name`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `county_name` (
  `id` bigint(11) NOT NULL AUTO_INCREMENT,
  `county_name` text CHARACTER SET utf8 COLLATE utf8_general_ci,
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `updated_at` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  UNIQUE KEY `PRIMARY` (`id`) USING HASH,
  KEY `id` (`id`) USING CLUSTERED COLUMNSTORE,
  SHARD KEY `__SHARDKEY` (`id`)
) AUTOSTATS_CARDINALITY_MODE=INCREMENTAL AUTOSTATS_HISTOGRAM_MODE=CREATE AUTOSTATS_SAMPLING=ON SQL_MODE='STRICT_ALL_TABLES';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `crew`
--

DROP TABLE IF EXISTS `crew`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `crew` (
  `id` bigint(11) NOT NULL AUTO_INCREMENT,
  `name` text CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `phone_number` text CHARACTER SET utf8 COLLATE utf8_general_ci,
  `role` enum('admin','manager','engineer') CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `manager_id` int(11) DEFAULT NULL,
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `updated_at` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  UNIQUE KEY `PRIMARY` (`id`) USING HASH,
  KEY `id` (`id`) USING CLUSTERED COLUMNSTORE,
  SHARD KEY `__SHARDKEY` (`id`)
) AUTOSTATS_CARDINALITY_MODE=INCREMENTAL AUTOSTATS_HISTOGRAM_MODE=CREATE AUTOSTATS_SAMPLING=ON SQL_MODE='STRICT_ALL_TABLES';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `customer_field_rep`
--

DROP TABLE IF EXISTS `customer_field_rep`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `customer_field_rep` (
  `id` bigint(11) NOT NULL AUTO_INCREMENT,
  `name` text CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `customer_field_rep_num` int(11) DEFAULT NULL,
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `updated_at` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  UNIQUE KEY `PRIMARY` (`id`) USING HASH,
  KEY `id` (`id`) USING CLUSTERED COLUMNSTORE,
  SHARD KEY `__SHARDKEY` (`id`)
) AUTOSTATS_CARDINALITY_MODE=INCREMENTAL AUTOSTATS_HISTOGRAM_MODE=CREATE AUTOSTATS_SAMPLING=ON SQL_MODE='STRICT_ALL_TABLES';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `default_advance_val`
--

DROP TABLE IF EXISTS `default_advance_val`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `default_advance_val` (
  `id` bigint(11) NOT NULL AUTO_INCREMENT,
  `well_id` int(11) DEFAULT NULL,
  `model` varchar(40) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `response` varchar(40) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `source` varchar(40) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `viscosity` float DEFAULT NULL,
  `density` float DEFAULT NULL,
  `compresssibility` float DEFAULT NULL,
  `f_low_hz` float DEFAULT NULL,
  `f_high_hz` float DEFAULT NULL,
  `new_sample_rate` float DEFAULT NULL,
  `data_sample_rate` float DEFAULT NULL,
  `algorithm` varchar(40) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `grid_density` float DEFAULT NULL,
  `weighting` varchar(10) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `wlevexp` float DEFAULT NULL,
  `loop` varchar(10) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `method` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `tolerance` float DEFAULT NULL,
  `interation` int(11) DEFAULT NULL,
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `updated_at` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  UNIQUE KEY `PRIMARY` (`id`) USING HASH,
  KEY `well_id` (`well_id`) USING CLUSTERED COLUMNSTORE,
  SHARD KEY `__SHARDKEY` (`id`)
) AUTOSTATS_CARDINALITY_MODE=INCREMENTAL AUTOSTATS_HISTOGRAM_MODE=CREATE AUTOSTATS_SAMPLING=ON SQL_MODE='STRICT_ALL_TABLES';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `default_param_val`
--

DROP TABLE IF EXISTS `default_param_val`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `default_param_val` (
  `id` bigint(11) NOT NULL AUTO_INCREMENT,
  `well_id` int(11) DEFAULT NULL,
  `c1_min` float DEFAULT NULL,
  `c2_min` float DEFAULT NULL,
  `c1_max` float DEFAULT NULL,
  `c2_max` float DEFAULT NULL,
  `c3_min` float DEFAULT NULL,
  `c3_max` float DEFAULT NULL,
  `q_min` int(11) DEFAULT NULL,
  `q_max` int(11) DEFAULT NULL,
  `k_min` float DEFAULT NULL,
  `k_max` float DEFAULT NULL,
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `updated_at` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  UNIQUE KEY `PRIMARY` (`id`) USING HASH,
  KEY `well_id` (`well_id`) USING CLUSTERED COLUMNSTORE,
  SHARD KEY `__SHARDKEY` (`id`)
) AUTOSTATS_CARDINALITY_MODE=INCREMENTAL AUTOSTATS_HISTOGRAM_MODE=CREATE AUTOSTATS_SAMPLING=ON SQL_MODE='STRICT_ALL_TABLES';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `default_val`
--

DROP TABLE IF EXISTS `default_val`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `default_val` (
  `id` bigint(11) NOT NULL AUTO_INCREMENT,
  `well_id` int(11) DEFAULT NULL,
  `pres` float DEFAULT NULL,
  `young` float DEFAULT NULL,
  `overburden` float DEFAULT NULL,
  `poisson` float DEFAULT NULL,
  `eta_cp` int(11) DEFAULT NULL,
  `fuildt` int(11) DEFAULT NULL,
  `tect` float DEFAULT NULL,
  `fuild_density` float DEFAULT NULL,
  `diverter_time` float DEFAULT NULL,
  `met_res` float DEFAULT NULL,
  `ffkw_correction` int(11) DEFAULT NULL,
  `k_mpa` int(11) DEFAULT NULL,
  `nu_lim` int(11) DEFAULT NULL,
  `per_red` int(11) DEFAULT NULL,
  `start1` int(11) DEFAULT NULL,
  `beta_ss` float DEFAULT NULL,
  `st_lim` int(11) DEFAULT NULL,
  `biot` int(11) DEFAULT NULL,
  `shadow` int(11) DEFAULT NULL,
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `updated_at` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  UNIQUE KEY `PRIMARY` (`id`) USING HASH,
  KEY `well_id` (`well_id`) USING CLUSTERED COLUMNSTORE,
  SHARD KEY `__SHARDKEY` (`id`)
) AUTOSTATS_CARDINALITY_MODE=INCREMENTAL AUTOSTATS_HISTOGRAM_MODE=CREATE AUTOSTATS_SAMPLING=ON SQL_MODE='STRICT_ALL_TABLES';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `equipment`
--

DROP TABLE IF EXISTS `equipment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `equipment` (
  `id` bigint(11) NOT NULL AUTO_INCREMENT,
  `trailer_id` int(11) DEFAULT NULL,
  `powerpack_id` int(11) DEFAULT NULL,
  `source_id` int(11) DEFAULT NULL,
  `accumulator_id` int(11) DEFAULT NULL,
  `hydrophones_id` int(11) DEFAULT NULL,
  `transducer_id` int(11) DEFAULT NULL,
  `hotspot_id` int(11) DEFAULT NULL,
  `computer_id` int(11) DEFAULT NULL,
  `pressure_counter` double DEFAULT NULL,
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `updated_at` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  UNIQUE KEY `PRIMARY` (`id`) USING HASH,
  KEY `id` (`id`) USING CLUSTERED COLUMNSTORE,
  SHARD KEY `__SHARDKEY` (`id`)
) AUTOSTATS_CARDINALITY_MODE=INCREMENTAL AUTOSTATS_HISTOGRAM_MODE=CREATE AUTOSTATS_SAMPLING=ON SQL_MODE='STRICT_ALL_TABLES';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `ff_parameter_set`
--

DROP TABLE IF EXISTS `ff_parameter_set`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ff_parameter_set` (
  `id` int(11) NOT NULL,
  `username` text CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `date_created` datetime DEFAULT NULL,
  `shut_in_period_start` datetime DEFAULT NULL,
  `sample_rate` float DEFAULT NULL,
  `total_samples` float DEFAULT NULL,
  `tvd` float DEFAULT NULL,
  `viscosity` float DEFAULT NULL,
  `compressibility_mpa` float DEFAULT NULL,
  `poisson_ratio` float DEFAULT NULL,
  `youngs_modulus_mpa` float DEFAULT NULL,
  `volume_pumped` float DEFAULT NULL,
  `proppant_volume_pumped_bbl` float DEFAULT NULL,
  `average_injection_rate` float DEFAULT NULL,
  `tectonic_component` float DEFAULT NULL,
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `updated_at` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  UNIQUE KEY `PRIMARY` (`id`) USING HASH,
  KEY `id` (`id`) USING CLUSTERED COLUMNSTORE,
  SHARD KEY `__SHARDKEY` (`id`)
) AUTOSTATS_CARDINALITY_MODE=INCREMENTAL AUTOSTATS_HISTOGRAM_MODE=CREATE AUTOSTATS_SAMPLING=ON SQL_MODE='STRICT_ALL_TABLES';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `ff_processing_result`
--

DROP TABLE IF EXISTS `ff_processing_result`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ff_processing_result` (
  `id` int(11) NOT NULL,
  `timestamp` datetime DEFAULT NULL,
  `length` float DEFAULT NULL,
  `width` float DEFAULT NULL,
  `height` float DEFAULT NULL,
  `conductivity` float DEFAULT NULL,
  `minimum_stress` float DEFAULT NULL,
  `minimun_stress_gradient` float DEFAULT NULL,
  `net_pressure` float DEFAULT NULL,
  `fracture_pressure_gradient` float DEFAULT NULL,
  `reservoir_pressure` float DEFAULT NULL,
  `reservoir_pressure_gradient` float DEFAULT NULL,
  `pressure_match` float DEFAULT NULL,
  `fracture_efficiency` float DEFAULT NULL,
  `stress_shadow_pressure` float DEFAULT NULL,
  `calculated_poisson_ratio` float DEFAULT NULL,
  `stage_id` int(11) NOT NULL,
  `ff_parameter_id` int(11) NOT NULL,
  `nwb_region_size` float DEFAULT NULL,
  `nwb_compressibility` float DEFAULT NULL,
  `nwb_permeability` float DEFAULT NULL,
  `ff_version` text CHARACTER SET utf8 COLLATE utf8_general_ci,
  `unit` text CHARACTER SET utf8 COLLATE utf8_general_ci,
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `updated_at` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  UNIQUE KEY `PRIMARY` (`id`) USING HASH,
  KEY `id` (`id`) USING CLUSTERED COLUMNSTORE,
  SHARD KEY `__SHARDKEY` (`id`)
) AUTOSTATS_CARDINALITY_MODE=INCREMENTAL AUTOSTATS_HISTOGRAM_MODE=CREATE AUTOSTATS_SAMPLING=ON SQL_MODE='STRICT_ALL_TABLES';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `field_notes`
--

DROP TABLE IF EXISTS `field_notes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `field_notes` (
  `id` bigint(11) NOT NULL AUTO_INCREMENT,
  `well_id` int(11) NOT NULL,
  `comment_timestamp` datetime DEFAULT NULL,
  `comment_content` text CHARACTER SET utf8 COLLATE utf8_general_ci,
  `comment_by` text CHARACTER SET utf8 COLLATE utf8_general_ci,
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `updated_at` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  UNIQUE KEY `PRIMARY` (`id`) USING HASH,
  KEY `well_id` (`well_id`) USING CLUSTERED COLUMNSTORE,
  SHARD KEY `__SHARDKEY` (`id`)
) AUTOSTATS_CARDINALITY_MODE=INCREMENTAL AUTOSTATS_HISTOGRAM_MODE=CREATE AUTOSTATS_SAMPLING=ON SQL_MODE='STRICT_ALL_TABLES';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `fluid_type_lookup`
--

DROP TABLE IF EXISTS `fluid_type_lookup`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `fluid_type_lookup` (
  `id` bigint(11) NOT NULL AUTO_INCREMENT,
  `value` int(11) NOT NULL,
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `updated_at` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  UNIQUE KEY `PRIMARY` (`id`) USING HASH,
  KEY `id` (`id`) USING CLUSTERED COLUMNSTORE,
  SHARD KEY `__SHARDKEY` (`id`)
) AUTOSTATS_CARDINALITY_MODE=INCREMENTAL AUTOSTATS_HISTOGRAM_MODE=CREATE AUTOSTATS_SAMPLING=ON SQL_MODE='STRICT_ALL_TABLES';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `formation_top`
--

DROP TABLE IF EXISTS `formation_top`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `formation_top` (
  `id` bigint(11) NOT NULL AUTO_INCREMENT,
  `well_id` int(11) NOT NULL,
  `measured_depth` float DEFAULT NULL,
  `inclination` float DEFAULT NULL,
  `azimuth` float DEFAULT NULL,
  `X` float DEFAULT NULL,
  `Y` float DEFAULT NULL,
  `Z` float DEFAULT NULL,
  `target_upper` float DEFAULT NULL,
  `target_lower` float DEFAULT NULL,
  `l1_upper` float DEFAULT NULL,
  `l1_lower` float DEFAULT NULL,
  `l2_upper` float DEFAULT NULL,
  `l2_lower` float DEFAULT NULL,
  `l3_upper` float DEFAULT NULL,
  `l3_lower` float DEFAULT NULL,
  `l4_upper` float DEFAULT NULL,
  `l4_lower` float DEFAULT NULL,
  `l5_upper` float DEFAULT NULL,
  `l5_lower` float DEFAULT NULL,
  `l6_upper` float DEFAULT NULL,
  `l6_lower` float DEFAULT NULL,
  `l7_upper` float DEFAULT NULL,
  `l7_lower` float DEFAULT NULL,
  `l8_upper` float DEFAULT NULL,
  `l8_lower` float DEFAULT NULL,
  `l9_upper` float DEFAULT NULL,
  `l9_lower` float DEFAULT NULL,
  `l10_upper` float DEFAULT NULL,
  `l10_lower` float DEFAULT NULL,
  `additional` JSON COLLATE utf8_bin,
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `updated_at` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  UNIQUE KEY `PRIMARY` (`id`) USING HASH,
  KEY `well_id` (`well_id`) USING CLUSTERED COLUMNSTORE,
  SHARD KEY `__SHARDKEY` (`id`)
) AUTOSTATS_CARDINALITY_MODE=INCREMENTAL AUTOSTATS_HISTOGRAM_MODE=CREATE AUTOSTATS_SAMPLING=ON SQL_MODE='STRICT_ALL_TABLES';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `formation_top_reference`
--

DROP TABLE IF EXISTS `formation_top_reference`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `formation_top_reference` (
  `id` bigint(11) NOT NULL AUTO_INCREMENT,
  `formation_top_id` int(11) NOT NULL,
  `l1` text CHARACTER SET utf8 COLLATE utf8_general_ci,
  `l2` text CHARACTER SET utf8 COLLATE utf8_general_ci,
  `l3` text CHARACTER SET utf8 COLLATE utf8_general_ci,
  `l4` text CHARACTER SET utf8 COLLATE utf8_general_ci,
  `l5` text CHARACTER SET utf8 COLLATE utf8_general_ci,
  `l6` text CHARACTER SET utf8 COLLATE utf8_general_ci,
  `l7` text CHARACTER SET utf8 COLLATE utf8_general_ci,
  `l8` text CHARACTER SET utf8 COLLATE utf8_general_ci,
  `l9` text CHARACTER SET utf8 COLLATE utf8_general_ci,
  `l10` text CHARACTER SET utf8 COLLATE utf8_general_ci,
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `updated_at` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  UNIQUE KEY `PRIMARY` (`id`) USING HASH,
  KEY `id` (`id`) USING CLUSTERED COLUMNSTORE,
  SHARD KEY `__SHARDKEY` (`id`)
) AUTOSTATS_CARDINALITY_MODE=INCREMENTAL AUTOSTATS_HISTOGRAM_MODE=CREATE AUTOSTATS_SAMPLING=ON SQL_MODE='STRICT_ALL_TABLES';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `frac_design_lookup`
--

DROP TABLE IF EXISTS `frac_design_lookup`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `frac_design_lookup` (
  `id` bigint(11) NOT NULL AUTO_INCREMENT,
  `value` int(11) NOT NULL,
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `updated_at` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  UNIQUE KEY `PRIMARY` (`id`) USING HASH,
  KEY `id` (`id`) USING CLUSTERED COLUMNSTORE,
  SHARD KEY `__SHARDKEY` (`id`)
) AUTOSTATS_CARDINALITY_MODE=INCREMENTAL AUTOSTATS_HISTOGRAM_MODE=CREATE AUTOSTATS_SAMPLING=ON SQL_MODE='STRICT_ALL_TABLES';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `geophysical_properties`
--

DROP TABLE IF EXISTS `geophysical_properties`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `geophysical_properties` (
  `id` bigint(11) NOT NULL AUTO_INCREMENT,
  `well_id` int(11) NOT NULL,
  `measured_depth` float DEFAULT NULL,
  `young_modulus` float DEFAULT NULL,
  `poisson_ratio` float DEFAULT NULL,
  `min_stress` float DEFAULT NULL,
  `dynamic_horizontal_young_modulus` float DEFAULT NULL,
  `static_horizontal_young_modulus` float DEFAULT NULL,
  `static_vertical_young_modulus` float DEFAULT NULL,
  `horizontal_poisson_ratio` float DEFAULT NULL,
  `vertical_possion_ratio` float DEFAULT NULL,
  `pore_pressure` float DEFAULT NULL,
  `tensile_strength` float DEFAULT NULL,
  `vertical_stress_gradient` float DEFAULT NULL,
  `json_data` JSON COLLATE utf8_bin,
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `updated_at` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  UNIQUE KEY `PRIMARY` (`id`) USING HASH,
  KEY `well_id` (`well_id`) USING CLUSTERED COLUMNSTORE,
  SHARD KEY `__SHARDKEY` (`id`)
) AUTOSTATS_CARDINALITY_MODE=INCREMENTAL AUTOSTATS_HISTOGRAM_MODE=CREATE AUTOSTATS_SAMPLING=ON SQL_MODE='STRICT_ALL_TABLES';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `job_info`
--

DROP TABLE IF EXISTS `job_info`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `job_info` (
  `id` bigint(11) NOT NULL AUTO_INCREMENT,
  `job_id` text CHARACTER SET utf8 COLLATE utf8_general_ci,
  `job_name` text CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `afe_id` int(11) DEFAULT NULL,
  `job_start_date` datetime DEFAULT NULL,
  `job_end_date` datetime DEFAULT NULL,
  `job_type_id` int(11) DEFAULT NULL,
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `updated_at` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  UNIQUE KEY `PRIMARY` (`id`) USING HASH,
  KEY `id` (`id`) USING CLUSTERED COLUMNSTORE,
  SHARD KEY `__SHARDKEY` (`id`)
) AUTOSTATS_CARDINALITY_MODE=INCREMENTAL AUTOSTATS_HISTOGRAM_MODE=CREATE AUTOSTATS_SAMPLING=ON SQL_MODE='STRICT_ALL_TABLES';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `job_type`
--

DROP TABLE IF EXISTS `job_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `job_type` (
  `id` bigint(11) NOT NULL AUTO_INCREMENT,
  `value` text CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `updated_at` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  UNIQUE KEY `PRIMARY` (`id`) USING HASH,
  KEY `id` (`id`) USING CLUSTERED COLUMNSTORE,
  SHARD KEY `__SHARDKEY` (`id`)
) AUTOSTATS_CARDINALITY_MODE=INCREMENTAL AUTOSTATS_HISTOGRAM_MODE=CREATE AUTOSTATS_SAMPLING=ON SQL_MODE='STRICT_ALL_TABLES';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `location_info`
--

DROP TABLE IF EXISTS `location_info`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `location_info` (
  `id` bigint(11) NOT NULL AUTO_INCREMENT,
  `county_name_id` int(11) NOT NULL,
  `basin_name_id` int(11) NOT NULL,
  `state_id` int(11) NOT NULL,
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `updated_at` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  UNIQUE KEY `PRIMARY` (`id`,`county_name_id`,`basin_name_id`,`state_id`) USING HASH,
  KEY `id` (`id`) USING CLUSTERED COLUMNSTORE,
  SHARD KEY `__SHARDKEY` (`id`,`county_name_id`,`basin_name_id`,`state_id`)
) AUTOSTATS_CARDINALITY_MODE=INCREMENTAL AUTOSTATS_HISTOGRAM_MODE=CREATE AUTOSTATS_SAMPLING=ON SQL_MODE='STRICT_ALL_TABLES';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `mud_log`
--

DROP TABLE IF EXISTS `mud_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `mud_log` (
  `id` bigint(11) NOT NULL AUTO_INCREMENT,
  `well_id` int(11) NOT NULL,
  `measure_depth` float DEFAULT NULL,
  `siltstone` float DEFAULT NULL,
  `sand` float DEFAULT NULL,
  `coal` float DEFAULT NULL,
  `limestone` float DEFAULT NULL,
  `dolomite` float DEFAULT NULL,
  `salt` float DEFAULT NULL,
  `chert` float DEFAULT NULL,
  `chalk` float DEFAULT NULL,
  `anhydrite` float DEFAULT NULL,
  `shale` float DEFAULT NULL,
  `gamma_ray` float DEFAULT NULL,
  `clay` float DEFAULT NULL,
  `marl` float DEFAULT NULL,
  `rate_of_penetration` float DEFAULT NULL,
  `rpm` float DEFAULT NULL,
  `weight_on_bit` float DEFAULT NULL,
  `total_gas` float DEFAULT NULL,
  `methane` float DEFAULT NULL,
  `ethane` float DEFAULT NULL,
  `propane` float DEFAULT NULL,
  `isobutane` float DEFAULT NULL,
  `butane` float DEFAULT NULL,
  `isopentane` float DEFAULT NULL,
  `pentane` float DEFAULT NULL,
  `json_data` JSON COLLATE utf8_bin,
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `updated_at` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  UNIQUE KEY `PRIMARY` (`id`) USING HASH,
  KEY `well_id` (`well_id`) USING CLUSTERED COLUMNSTORE,
  SHARD KEY `__SHARDKEY` (`id`)
) AUTOSTATS_CARDINALITY_MODE=INCREMENTAL AUTOSTATS_HISTOGRAM_MODE=CREATE AUTOSTATS_SAMPLING=ON SQL_MODE='STRICT_ALL_TABLES';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `mwd_report`
--

DROP TABLE IF EXISTS `mwd_report`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `mwd_report` (
  `id` bigint(11) NOT NULL AUTO_INCREMENT,
  `well_id` int(11) NOT NULL,
  `measured_depth` float DEFAULT NULL,
  `gamma_ray` float DEFAULT NULL,
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `updated_at` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  UNIQUE KEY `PRIMARY` (`id`) USING HASH,
  KEY `well_id` (`well_id`) USING CLUSTERED COLUMNSTORE,
  SHARD KEY `__SHARDKEY` (`id`)
) AUTOSTATS_CARDINALITY_MODE=INCREMENTAL AUTOSTATS_HISTOGRAM_MODE=CREATE AUTOSTATS_SAMPLING=ON SQL_MODE='STRICT_ALL_TABLES';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `nf_parameter_set`
--

DROP TABLE IF EXISTS `nf_parameter_set`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `nf_parameter_set` (
  `id` int(11) NOT NULL,
  `creation_date` datetime DEFAULT NULL,
  `c1_lower_bound` float DEFAULT NULL,
  `c1_upper_bound` float DEFAULT NULL,
  `c2_lower_bound` float DEFAULT NULL,
  `c2_upper_bound` float DEFAULT NULL,
  `c3_lower_bound` float DEFAULT NULL,
  `c3_upper_bound` float DEFAULT NULL,
  `direct_sources_start` datetime DEFAULT NULL,
  `first_reflection_start` datetime DEFAULT NULL,
  `direct_source_num_samples` int(11) DEFAULT NULL,
  `first_reflection_num_samples` int(11) DEFAULT NULL,
  `source_duration` float DEFAULT NULL,
  `min_pulse_separation` float DEFAULT NULL,
  `compressbility` float DEFAULT NULL,
  `deconvolution_override` text CHARACTER SET utf8 COLLATE utf8_general_ci,
  `deconvolution_noise_level` float DEFAULT NULL,
  `nf_shot_finder_versaion` text CHARACTER SET utf8 COLLATE utf8_general_ci,
  `nf_inversion_version` text CHARACTER SET utf8 COLLATE utf8_general_ci,
  `shot_id` int(11) DEFAULT NULL,
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `updated_at` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  UNIQUE KEY `PRIMARY` (`id`) USING HASH,
  KEY `id` (`id`) USING CLUSTERED COLUMNSTORE,
  SHARD KEY `__SHARDKEY` (`id`)
) AUTOSTATS_CARDINALITY_MODE=INCREMENTAL AUTOSTATS_HISTOGRAM_MODE=CREATE AUTOSTATS_SAMPLING=ON SQL_MODE='STRICT_ALL_TABLES';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `nf_processing_result`
--

DROP TABLE IF EXISTS `nf_processing_result`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `nf_processing_result` (
  `id` bigint(11) NOT NULL AUTO_INCREMENT,
  `stage_id` int(11) NOT NULL,
  `timestamp` datetime DEFAULT NULL,
  `user_id` text CHARACTER SET utf8 COLLATE utf8_general_ci,
  `c0` float DEFAULT NULL,
  `c1` float DEFAULT NULL,
  `c2` float DEFAULT NULL,
  `c3` float DEFAULT NULL,
  `q0` float DEFAULT NULL,
  `q1` float DEFAULT NULL,
  `q2` float DEFAULT NULL,
  `q3` float DEFAULT NULL,
  `fit_error` float DEFAULT NULL,
  `nf_param_id` int(11) DEFAULT NULL,
  `connect_ops_risk` float DEFAULT NULL,
  `connect_efficiency` float DEFAULT NULL,
  `connect_condition` float DEFAULT NULL,
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `updated_at` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  UNIQUE KEY `PRIMARY` (`id`) USING HASH,
  KEY `stage_id` (`stage_id`) USING CLUSTERED COLUMNSTORE,
  SHARD KEY `__SHARDKEY` (`id`)
) AUTOSTATS_CARDINALITY_MODE=INCREMENTAL AUTOSTATS_HISTOGRAM_MODE=CREATE AUTOSTATS_SAMPLING=ON SQL_MODE='STRICT_ALL_TABLES';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `pad`
--

DROP TABLE IF EXISTS `pad`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `pad` (
  `id` bigint(11) NOT NULL AUTO_INCREMENT,
  `pad_uuid` char(36) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `project_id` int(11) NOT NULL,
  `pad_name` text CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `number_of_wells` int(11) DEFAULT NULL,
  `well_spacing` float DEFAULT NULL,
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `updated_at` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  UNIQUE KEY `PRIMARY` (`id`) USING HASH,
  KEY `pad_uuid` (`pad_uuid`) USING CLUSTERED COLUMNSTORE,
  SHARD KEY `__SHARDKEY` (`id`)
) AUTOSTATS_CARDINALITY_MODE=INCREMENTAL AUTOSTATS_HISTOGRAM_MODE=CREATE AUTOSTATS_SAMPLING=ON SQL_MODE='STRICT_ALL_TABLES';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `perforation`
--

DROP TABLE IF EXISTS `perforation`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `perforation` (
  `id` bigint(11) NOT NULL AUTO_INCREMENT,
  `stage_id` int(11) NOT NULL,
  `order_num` int(11) DEFAULT NULL,
  `ordinal` float DEFAULT NULL,
  `top_measured_depth` float DEFAULT NULL,
  `bottom_measured_depth` float DEFAULT NULL,
  `depth_unit` text CHARACTER SET utf8 COLLATE utf8_general_ci,
  `shot_number` int(11) DEFAULT NULL,
  `shot_density` float DEFAULT NULL,
  `shot_density_unit` text CHARACTER SET utf8 COLLATE utf8_general_ci,
  `shot_count` int(11) DEFAULT NULL,
  `phasing` text CHARACTER SET utf8 COLLATE utf8_general_ci,
  `conveyance_method` text CHARACTER SET utf8 COLLATE utf8_general_ci,
  `charge_type` text CHARACTER SET utf8 COLLATE utf8_general_ci,
  `charge_size` double DEFAULT NULL,
  `charge_size_unit` text CHARACTER SET utf8 COLLATE utf8_general_ci,
  `estimated_hole_diamter` float DEFAULT NULL,
  `estimated_hole_diameter_unit` text CHARACTER SET utf8 COLLATE utf8_general_ci,
  `perf_plug_num` int(11) DEFAULT NULL,
  `perf_start_time` datetime DEFAULT NULL,
  `perf_end_time` datetime DEFAULT NULL,
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `updated_at` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  UNIQUE KEY `PRIMARY` (`id`) USING HASH,
  KEY `stage_id` (`stage_id`) USING CLUSTERED COLUMNSTORE,
  SHARD KEY `__SHARDKEY` (`id`)
) AUTOSTATS_CARDINALITY_MODE=INCREMENTAL AUTOSTATS_HISTOGRAM_MODE=CREATE AUTOSTATS_SAMPLING=ON SQL_MODE='STRICT_ALL_TABLES';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `plug_depth_unit_lookup`
--

DROP TABLE IF EXISTS `plug_depth_unit_lookup`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `plug_depth_unit_lookup` (
  `id` bigint(11) NOT NULL AUTO_INCREMENT,
  `value` text CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `updated_at` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  UNIQUE KEY `PRIMARY` (`id`) USING HASH,
  KEY `id` (`id`) USING CLUSTERED COLUMNSTORE,
  SHARD KEY `__SHARDKEY` (`id`)
) AUTOSTATS_CARDINALITY_MODE=INCREMENTAL AUTOSTATS_HISTOGRAM_MODE=CREATE AUTOSTATS_SAMPLING=ON SQL_MODE='STRICT_ALL_TABLES';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `plug_name_lookup`
--

DROP TABLE IF EXISTS `plug_name_lookup`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `plug_name_lookup` (
  `id` bigint(11) NOT NULL AUTO_INCREMENT,
  `value` float NOT NULL,
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `updated_at` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  UNIQUE KEY `PRIMARY` (`id`) USING HASH,
  KEY `id` (`id`) USING CLUSTERED COLUMNSTORE,
  SHARD KEY `__SHARDKEY` (`id`)
) AUTOSTATS_CARDINALITY_MODE=INCREMENTAL AUTOSTATS_HISTOGRAM_MODE=CREATE AUTOSTATS_SAMPLING=ON SQL_MODE='STRICT_ALL_TABLES';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `post_frac`
--

DROP TABLE IF EXISTS `post_frac`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `post_frac` (
  `id` bigint(11) NOT NULL AUTO_INCREMENT,
  `stage_id` int(11) DEFAULT NULL,
  `post_start_time` datetime DEFAULT NULL,
  `post_end_time` datetime DEFAULT NULL,
  `post_frac_num_pulse` text CHARACTER SET utf8 COLLATE utf8_general_ci,
  `post_frac_pulse_notes` text CHARACTER SET utf8 COLLATE utf8_general_ci,
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `updated_at` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  UNIQUE KEY `PRIMARY` (`id`) USING HASH,
  KEY `stage_id` (`stage_id`) USING CLUSTERED COLUMNSTORE,
  SHARD KEY `__SHARDKEY` (`id`)
) AUTOSTATS_CARDINALITY_MODE=INCREMENTAL AUTOSTATS_HISTOGRAM_MODE=CREATE AUTOSTATS_SAMPLING=ON SQL_MODE='STRICT_ALL_TABLES';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `pre_frac`
--

DROP TABLE IF EXISTS `pre_frac`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `pre_frac` (
  `id` bigint(11) NOT NULL AUTO_INCREMENT,
  `stage_id` int(11) DEFAULT NULL,
  `pre_start_time` datetime DEFAULT NULL,
  `pre_end_time` datetime DEFAULT NULL,
  `pre_frac_num_pulse` text CHARACTER SET utf8 COLLATE utf8_general_ci,
  `pre_frac_pulse_notes` text CHARACTER SET utf8 COLLATE utf8_general_ci,
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `updated_at` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  UNIQUE KEY `PRIMARY` (`id`) USING HASH,
  KEY `stage_id` (`stage_id`) USING CLUSTERED COLUMNSTORE,
  SHARD KEY `__SHARDKEY` (`id`)
) AUTOSTATS_CARDINALITY_MODE=INCREMENTAL AUTOSTATS_HISTOGRAM_MODE=CREATE AUTOSTATS_SAMPLING=ON SQL_MODE='STRICT_ALL_TABLES';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `project`
--

DROP TABLE IF EXISTS `project`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `project` (
  `id` bigint(11) NOT NULL AUTO_INCREMENT,
  `project_uuid` char(36) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `project_name` text CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `client_id` int(11) NOT NULL,
  `equipment_id` int(11) DEFAULT NULL,
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `updated_at` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  UNIQUE KEY `PRIMARY` (`id`) USING HASH,
  KEY `project_uuid` (`project_uuid`) USING CLUSTERED COLUMNSTORE,
  SHARD KEY `__SHARDKEY` (`id`)
) AUTOSTATS_CARDINALITY_MODE=INCREMENTAL AUTOSTATS_HISTOGRAM_MODE=CREATE AUTOSTATS_SAMPLING=ON SQL_MODE='STRICT_ALL_TABLES';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `project_crew`
--

DROP TABLE IF EXISTS `project_crew`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `project_crew` (
  `project_crew_id` bigint(11) NOT NULL AUTO_INCREMENT,
  `project_id` int(11) NOT NULL,
  `crew_id` int(11) NOT NULL,
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `updated_at` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  UNIQUE KEY `PRIMARY` (`project_crew_id`) USING HASH,
  KEY `project_id` (`project_id`) USING CLUSTERED COLUMNSTORE,
  SHARD KEY `__SHARDKEY` (`project_crew_id`)
) AUTOSTATS_CARDINALITY_MODE=INCREMENTAL AUTOSTATS_HISTOGRAM_MODE=CREATE AUTOSTATS_SAMPLING=ON SQL_MODE='STRICT_ALL_TABLES';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `proppant`
--

DROP TABLE IF EXISTS `proppant`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `proppant` (
  `id` bigint(11) NOT NULL AUTO_INCREMENT,
  `stage_id` int(11) NOT NULL,
  `proppant_name_id` int(11) NOT NULL,
  `prop_mass` float DEFAULT NULL,
  `mass_unit` text CHARACTER SET utf8 COLLATE utf8_general_ci,
  `material` text CHARACTER SET utf8 COLLATE utf8_general_ci,
  `mesh_size` float DEFAULT NULL,
  `avg_concentration` float DEFAULT NULL,
  `avg_concentration_unit` text CHARACTER SET utf8 COLLATE utf8_general_ci,
  `max_concentration` float DEFAULT NULL,
  `max_concentration_unit` text CHARACTER SET utf8 COLLATE utf8_general_ci,
  `proppant_type_start_time` datetime DEFAULT NULL,
  `proppant_end_start_time` datetime DEFAULT NULL,
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `updated_at` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  UNIQUE KEY `PRIMARY` (`id`) USING HASH,
  KEY `stage_id` (`stage_id`) USING CLUSTERED COLUMNSTORE,
  SHARD KEY `__SHARDKEY` (`id`)
) AUTOSTATS_CARDINALITY_MODE=INCREMENTAL AUTOSTATS_HISTOGRAM_MODE=CREATE AUTOSTATS_SAMPLING=ON SQL_MODE='STRICT_ALL_TABLES';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `proppant_lookup`
--

DROP TABLE IF EXISTS `proppant_lookup`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `proppant_lookup` (
  `id` int(11) NOT NULL,
  `proppant_name` text CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `updated_at` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  UNIQUE KEY `PRIMARY` (`id`) USING HASH,
  KEY `id` (`id`) USING CLUSTERED COLUMNSTORE,
  SHARD KEY `__SHARDKEY` (`id`)
) AUTOSTATS_CARDINALITY_MODE=INCREMENTAL AUTOSTATS_HISTOGRAM_MODE=CREATE AUTOSTATS_SAMPLING=ON SQL_MODE='STRICT_ALL_TABLES';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `pumpdown`
--

DROP TABLE IF EXISTS `pumpdown`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `pumpdown` (
  `id` bigint(11) NOT NULL AUTO_INCREMENT,
  `stage_id` int(11) NOT NULL,
  `pressure` float DEFAULT NULL,
  `rate` float DEFAULT NULL,
  `total_pumdown_value` float DEFAULT NULL,
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `updated_at` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  UNIQUE KEY `PRIMARY` (`id`) USING HASH,
  KEY `stage_id` (`stage_id`) USING CLUSTERED COLUMNSTORE,
  SHARD KEY `__SHARDKEY` (`id`)
) AUTOSTATS_CARDINALITY_MODE=INCREMENTAL AUTOSTATS_HISTOGRAM_MODE=CREATE AUTOSTATS_SAMPLING=ON SQL_MODE='STRICT_ALL_TABLES';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `pumping_2hz`
--

DROP TABLE IF EXISTS `pumping_2hz`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `pumping_2hz` (
  `id` bigint(11) NOT NULL AUTO_INCREMENT,
  `stage_id` int(11) NOT NULL,
  `timestamp` datetime DEFAULT NULL,
  `treating_pressure` float DEFAULT NULL,
  `total_slurry_volume` float DEFAULT NULL,
  `total_clean_volume` float DEFAULT NULL,
  `slurry_rate` float DEFAULT NULL,
  `clean_rate` float DEFAULT NULL,
  `surface_prop_conc` float DEFAULT NULL,
  `bottom_prop_conc` float DEFAULT NULL,
  `bottom_pressure` float DEFAULT NULL,
  `net_pressure` float DEFAULT NULL,
  `backside_pressure` float DEFAULT NULL,
  `friction_reducer` float DEFAULT NULL,
  `gel` float DEFAULT NULL,
  `crosslink` float DEFAULT NULL,
  `additional_column` JSON COLLATE utf8_bin,
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `updated_at` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  UNIQUE KEY `PRIMARY` (`id`,`stage_id`) USING HASH,
  KEY `stage_id` (`stage_id`) USING CLUSTERED COLUMNSTORE,
  SHARD KEY `__SHARDKEY` (`id`,`stage_id`)
) AUTOSTATS_CARDINALITY_MODE=INCREMENTAL AUTOSTATS_HISTOGRAM_MODE=CREATE AUTOSTATS_SAMPLING=ON SQL_MODE='STRICT_ALL_TABLES';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `quality_control`
--

DROP TABLE IF EXISTS `quality_control`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `quality_control` (
  `id` bigint(11) NOT NULL AUTO_INCREMENT,
  `project_id` int(11) NOT NULL,
  `is_checked` tinyint(1) DEFAULT NULL,
  `checked_by` text CHARACTER SET utf8 COLLATE utf8_general_ci,
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `updated_at` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  UNIQUE KEY `PRIMARY` (`id`) USING HASH,
  KEY `project_id` (`project_id`) USING CLUSTERED COLUMNSTORE,
  SHARD KEY `__SHARDKEY` (`id`)
) AUTOSTATS_CARDINALITY_MODE=INCREMENTAL AUTOSTATS_HISTOGRAM_MODE=CREATE AUTOSTATS_SAMPLING=ON SQL_MODE='STRICT_ALL_TABLES';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `seismos_20hz`
--

DROP TABLE IF EXISTS `seismos_20hz`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `seismos_20hz` (
  `id` bigint(11) NOT NULL AUTO_INCREMENT,
  `stage_id` int(11) NOT NULL,
  `timestamp` datetime DEFAULT NULL,
  `ses_data_colllection_id` int(11) DEFAULT NULL,
  `ses_pressure_sensor` float NOT NULL,
  `ses_hydrophone_sensor_hi` float NOT NULL,
  `ses_hydrophone_sensor_low` float NOT NULL,
  `ses_pulse_trigger` float NOT NULL,
  `ses_wave_pulse_type` text CHARACTER SET utf8 COLLATE utf8_general_ci,
  `digital_signal_flag` int(11) DEFAULT NULL,
  `other_notes` text CHARACTER SET utf8 COLLATE utf8_general_ci,
  `num_reflections` int(11) DEFAULT NULL,
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `updated_at` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  UNIQUE KEY `PRIMARY` (`id`) USING HASH,
  KEY `stage_id` (`stage_id`) USING CLUSTERED COLUMNSTORE,
  SHARD KEY `__SHARDKEY` (`id`)
) AUTOSTATS_CARDINALITY_MODE=INCREMENTAL AUTOSTATS_HISTOGRAM_MODE=CREATE AUTOSTATS_SAMPLING=ON SQL_MODE='STRICT_ALL_TABLES';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `seismos_2hz_`
--

DROP TABLE IF EXISTS `seismos_2hz`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `seismos_2hz` (
  `id` bigint(11) NOT NULL AUTO_INCREMENT,
  `stage_id` int(11) NOT NULL,
  `timestamp` datetime DEFAULT NULL,
  `ses_data_colllection_id` int(11) DEFAULT NULL,
  `ses_pressure_sensor` float NOT NULL,
  `ses_hydrophone_sensor_hi` float NOT NULL,
  `ses_hydrophone_sensor_low` float NOT NULL,
  `ses_pulse_trigger` float NOT NULL,
  `ses_wave_pulse_type` text CHARACTER SET utf8 COLLATE utf8_general_ci,
  `digital_signal_flag` int(11) DEFAULT NULL,
  `other_notes` text CHARACTER SET utf8 COLLATE utf8_general_ci,
  `num_reflections` int(11) DEFAULT NULL,
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `updated_at` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  UNIQUE KEY `PRIMARY` (`id`) USING HASH,
  KEY `stage_id` (`stage_id`) USING CLUSTERED COLUMNSTORE,
  SHARD KEY `__SHARDKEY` (`id`)
) AUTOSTATS_CARDINALITY_MODE=INCREMENTAL AUTOSTATS_HISTOGRAM_MODE=CREATE AUTOSTATS_SAMPLING=ON SQL_MODE='STRICT_ALL_TABLES';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `slurry`
--

DROP TABLE IF EXISTS `slurry`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `slurry` (
  `id` bigint(11) NOT NULL AUTO_INCREMENT,
  `stage_id` int(11) NOT NULL,
  `total_slurry_rate` float DEFAULT NULL,
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `updated_at` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  UNIQUE KEY `PRIMARY` (`id`) USING HASH,
  KEY `stage_id` (`stage_id`) USING CLUSTERED COLUMNSTORE,
  SHARD KEY `__SHARDKEY` (`id`)
) AUTOSTATS_CARDINALITY_MODE=INCREMENTAL AUTOSTATS_HISTOGRAM_MODE=CREATE AUTOSTATS_SAMPLING=ON SQL_MODE='STRICT_ALL_TABLES';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `software`
--

DROP TABLE IF EXISTS `software`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `software` (
  `id` bigint(11) NOT NULL AUTO_INCREMENT,
  `project_id` int(11) DEFAULT NULL,
  `inpute_app_version` float DEFAULT NULL,
  `processing_version` float DEFAULT NULL,
  `db_version` float DEFAULT NULL,
  `mqtt_version` float DEFAULT NULL,
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `updated_at` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  UNIQUE KEY `PRIMARY` (`id`) USING HASH,
  KEY `project_id` (`project_id`) USING CLUSTERED COLUMNSTORE,
  SHARD KEY `__SHARDKEY` (`id`)
) AUTOSTATS_CARDINALITY_MODE=INCREMENTAL AUTOSTATS_HISTOGRAM_MODE=CREATE AUTOSTATS_SAMPLING=ON SQL_MODE='STRICT_ALL_TABLES';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `stage`
--

DROP TABLE IF EXISTS `stage`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `stage` (
  `id` bigint(11) NOT NULL AUTO_INCREMENT, 
  `stage_uuid` char(36) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `well_id` int(11) DEFAULT NULL,
  `stage_number` int(11) DEFAULT NULL,
  `number_of_cluster` int(11) DEFAULT NULL,
  `stage_start_time` datetime DEFAULT NULL,
  `stage_end_time` datetime DEFAULT NULL,
  `plug_depth` float DEFAULT NULL,
  `frac_design_id` int(11) DEFAULT NULL,
  `calc_net_pressure_result` float DEFAULT NULL,
  `observed_net_pressure` float DEFAULT NULL,
  `inline_density` float DEFAULT NULL,
  `blender_density` float DEFAULT NULL,
  `calc_bh_density` float DEFAULT NULL,
  `bottomhole_bhp` float DEFAULT NULL,
  `bottomhole_bht` float DEFAULT NULL,
  `frac_model_bhp` float DEFAULT NULL,
  `total_pumpdown_volume` float DEFAULT NULL,
  `poisson_ratio` float DEFAULT NULL,
  `pr_gradient` double DEFAULT NULL,
  `overburden_num` double DEFAULT NULL,
  `pumping_fluid_viscosity` float DEFAULT NULL,
  `pumping_fluid_density` float DEFAULT NULL,
  `pumping_fluid_type` text CHARACTER SET utf8 COLLATE utf8_general_ci,
  `tectonic_gradient` double DEFAULT NULL,
  `pore_pressure` float DEFAULT NULL,
  `sleeve_name` text CHARACTER SET utf8 COLLATE utf8_general_ci,
  `sleeve_ordinal` int(11) DEFAULT NULL,
  `sleeve_top_measured_depth` float DEFAULT NULL,
  `sleeve_bottom_measure_depth` float DEFAULT NULL,
  `sleeve_depth_unit` text CHARACTER SET utf8 COLLATE utf8_general_ci,
  `sleeve_port_size` float DEFAULT NULL,
  `sleeve_port_size_unit` text CHARACTER SET utf8 COLLATE utf8_general_ci,
  `sleeve_ball_size` float DEFAULT NULL,
  `sleeve_ball_size_unit` text CHARACTER SET utf8 COLLATE utf8_general_ci,
  `sleeve_seat_id` text CHARACTER SET utf8 COLLATE utf8_general_ci,
  `sleeve_manufacturer` text CHARACTER SET utf8 COLLATE utf8_general_ci,
  `sleeve_model` text CHARACTER SET utf8 COLLATE utf8_general_ci,
  `sleeve_toe_shift_pressure` int(11) DEFAULT NULL,
  `sleeve_toe_burst_pressure` int(11) DEFAULT NULL,
  `diverter_type` VARCHAR(255) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `plug_YN` VARCHAR(255) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `pumped_diverter` VARCHAR(255) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `spf` VARCHAR(255) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `stage_event` VARCHAR(255) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `plug_seat_technique` VARCHAR(255) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `designed_acid_vol` float DEFAULT NULL,
  `designed_flush_vol` float DEFAULT NULL,
    
  `designed_max_prop_conc` float DEFAULT NULL,
  `designed_total_clean_fluid_vol` float DEFAULT NULL,
  `designed_pad_vol` float DEFAULT NULL,
  `designed_propant` float DEFAULT NULL,
  `days` text CHARACTER SET utf8 COLLATE utf8_general_ci,
  `nights` text CHARACTER SET utf8 COLLATE utf8_general_ci,
  `frac_design_id` text CHARACTER SET utf8 COLLATE utf8_general_ci,
  `plug_type` text CHARACTER SET utf8 COLLATE utf8_general_ci,

  `additional` JSON COLLATE utf8_bin,
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `updated_at` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  UNIQUE KEY `PRIMARY` (`id`) USING HASH,
  KEY `stage_uuid` (`stage_uuid`) USING CLUSTERED COLUMNSTORE,
  SHARD KEY `__SHARDKEY` (`id`)
) AUTOSTATS_CARDINALITY_MODE=INCREMENTAL AUTOSTATS_HISTOGRAM_MODE=CREATE AUTOSTATS_SAMPLING=ON SQL_MODE='STRICT_ALL_TABLES';
/*!40101 SET character_set_client = @saved_cs_client */;


DROP TABLE IF EXISTS `active_data`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `active_data` (
  `id` bigint(11) NOT NULL AUTO_INCREMENT,
  `stage_id` int(11) DEFAULT NULL,
  `post_start_time` datetime DEFAULT NULL,
  `post_end_time` datetime DEFAULT NULL,
  `post_frac_num_pulse` text CHARACTER SET utf8 COLLATE utf8_general_ci,
  `post_frac_pulse_notes` text CHARACTER SET utf8 COLLATE utf8_general_ci,
  `pre_start_time` datetime DEFAULT NULL,
  `pre_end_time` datetime DEFAULT NULL,
  `pre_frac_num_pulse` text CHARACTER SET utf8 COLLATE utf8_general_ci,
  `pre_frac_pulse_notes` text CHARACTER SET utf8 COLLATE utf8_general_ci,
  `seismos_data_collection` text CHARACTER SET utf8 COLLATE utf8_general_ci,
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `updated_at` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  UNIQUE KEY `PRIMARY` (`id`) USING HASH,
  KEY `stage_id` (`stage_id`) USING CLUSTERED COLUMNSTORE,
  SHARD KEY `__SHARDKEY` (`id`)
) AUTOSTATS_CARDINALITY_MODE=INCREMENTAL AUTOSTATS_HISTOGRAM_MODE=CREATE AUTOSTATS_SAMPLING=ON SQL_MODE='STRICT_ALL_TABLES';
/*!40101 SET character_set_client = @saved_cs_client */;



--
-- Table structure for table `stage_avg`
--

DROP TABLE IF EXISTS `stage_avg`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `stage_avg` (
  `id` bigint(11) NOT NULL AUTO_INCREMENT,
  `stage_id` int(11) NOT NULL,
  `breakdown_pressure` float DEFAULT NULL,
  `isip` float DEFAULT NULL,
  `frac_gradient` float DEFAULT NULL,
  `diverter` float DEFAULT NULL,
  `acid` float DEFAULT NULL,
  `open_well_pressure` float DEFAULT NULL,
  `isip_5min` float DEFAULT NULL,
  `isip_10min` float DEFAULT NULL,
  `isip_15min` float DEFAULT NULL,
  `time_to_max_rate` float DEFAULT NULL,
  `avg_pressure` float DEFAULT NULL,
  `max_pressure` float DEFAULT NULL,
  `slickwater_volume` float DEFAULT NULL,
  `total_slurry` float DEFAULT NULL,
  `total_clean` float DEFAULT NULL,
  `avg_rate` float DEFAULT NULL,
  `max_rate` float DEFAULT NULL,
  `100_mesh` float DEFAULT NULL,
  `30_50_mesh` float DEFAULT NULL,
  `40_70_mesh` float DEFAULT NULL,
  `20_40_mesh` float DEFAULT NULL,
  `micro_prop` float DEFAULT NULL,
  `friction_reducer` float DEFAULT NULL,
  `gel` float DEFAULT NULL,
  `crosslink` float DEFAULT NULL,
  `flush_volume` float DEFAULT NULL,
  `additional` JSON COLLATE utf8_bin,

  `flush_volume` float DEFAULT NULL,
  `max_prop_conc` float DEFAULT NULL,
  `pad_vol` float DEFAULT NULL,  
  `propant` float DEFAULT NULL,

  `created_at` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `updated_at` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  UNIQUE KEY `PRIMARY` (`id`) USING HASH,
  KEY `stage_id` (`stage_id`) USING CLUSTERED COLUMNSTORE,
  SHARD KEY `__SHARDKEY` (`id`)
) AUTOSTATS_CARDINALITY_MODE=INCREMENTAL AUTOSTATS_HISTOGRAM_MODE=CREATE AUTOSTATS_SAMPLING=ON SQL_MODE='STRICT_ALL_TABLES';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `state`
--

DROP TABLE IF EXISTS `state`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `state` (
  `id` bigint(11) NOT NULL AUTO_INCREMENT,
  `value` text CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `updated_at` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  UNIQUE KEY `PRIMARY` (`id`) USING HASH,
  KEY `id` (`id`) USING CLUSTERED COLUMNSTORE,
  SHARD KEY `__SHARDKEY` (`id`)
) AUTOSTATS_CARDINALITY_MODE=INCREMENTAL AUTOSTATS_HISTOGRAM_MODE=CREATE AUTOSTATS_SAMPLING=ON SQL_MODE='STRICT_ALL_TABLES';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `survey_report`
--

DROP TABLE IF EXISTS `survey_report`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `survey_report` (
  `id` int(11) NOT NULL,
  `well_id` int(11) NOT NULL,
  `measured_depth` float DEFAULT NULL,
  `inclination` float DEFAULT NULL,
  `azimuth` float DEFAULT NULL,
  `tvd` float DEFAULT NULL,
  `ns` float DEFAULT NULL,
  `ew` float DEFAULT NULL,
  `vs` float DEFAULT NULL,
  `dls` float DEFAULT NULL,
  `closure_direction` float DEFAULT NULL,
  `dogleg_severity` float DEFAULT NULL,
  `additional` JSON COLLATE utf8_bin,
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `updated_at` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  UNIQUE KEY `PRIMARY` (`id`) USING HASH,
  KEY `well_id` (`well_id`) USING CLUSTERED COLUMNSTORE,
  SHARD KEY `__SHARDKEY` (`id`)
) AUTOSTATS_CARDINALITY_MODE=INCREMENTAL AUTOSTATS_HISTOGRAM_MODE=CREATE AUTOSTATS_SAMPLING=ON SQL_MODE='STRICT_ALL_TABLES';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `treating_pressure`
--

DROP TABLE IF EXISTS `treating_pressure`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `treating_pressure` (
  `id` bigint(11) NOT NULL AUTO_INCREMENT,
  `stage_id` int(11) NOT NULL,
  `wellhead_pressure` float DEFAULT NULL,
  `treating_pressure` float DEFAULT NULL,
  `annulus_pressure` float DEFAULT NULL,
  `calc_hydrostatic_pressure` float DEFAULT NULL,
  `calc_bhp` float DEFAULT NULL,
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `updated_at` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  UNIQUE KEY `PRIMARY` (`id`) USING HASH,
  KEY `stage_id` (`stage_id`) USING CLUSTERED COLUMNSTORE,
  SHARD KEY `__SHARDKEY` (`id`)
) AUTOSTATS_CARDINALITY_MODE=INCREMENTAL AUTOSTATS_HISTOGRAM_MODE=CREATE AUTOSTATS_SAMPLING=ON SQL_MODE='STRICT_ALL_TABLES';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `well`
--

DROP TABLE IF EXISTS `well`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `well` (
  `id` bigint(11) NOT NULL AUTO_INCREMENT,
  `well_uuid` char(36) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `pad_id` int(11) NOT NULL,
  `well_name` text CHARACTER SET utf8 COLLATE utf8_general_ci,
  `well_api` text CHARACTER SET utf8 COLLATE utf8_general_ci,
  `formation_id` int(11) DEFAULT NULL,
  `num_stages` int(11) DEFAULT NULL,
  `total_planned_stage` int(11) DEFAULT NULL,
  `total_perfs` int(11) DEFAULT NULL,
  `total_clusters` int(11) DEFAULT NULL,
  `frac_system` text CHARACTER SET utf8 COLLATE utf8_general_ci,
  `fluid_system` text CHARACTER SET utf8 COLLATE utf8_general_ci,
  `well_start_time` datetime DEFAULT NULL,
  `well_end_time` datetime DEFAULT NULL,
  `bottom_hole_latitude` float DEFAULT NULL,
  `bottom_hole_longitude` float DEFAULT NULL,
  `surface_longitude` float DEFAULT NULL,
  `surface_latitude` float DEFAULT NULL,
  `lateral_length` float DEFAULT NULL,
  `lateral_length_unit` text CHARACTER SET utf8 COLLATE utf8_general_ci,
  `measured_depth` float DEFAULT NULL,
  `vertical_depth` float DEFAULT NULL,
  `vertical_depth_unit` text CHARACTER SET utf8 COLLATE utf8_general_ci,
  `estimated_surface_vol` float DEFAULT NULL,
  `estimated_bbls` float DEFAULT NULL,
  `estimated_gallons` float DEFAULT NULL,
  `casing_od` float DEFAULT NULL,
  `casing_wt` float DEFAULT NULL,
  `casing_id` float DEFAULT NULL,
  `casing_depth_md` float DEFAULT NULL,
  `casing_tol` float DEFAULT NULL,
  `liner1_od` float DEFAULT NULL,
  `liner1_wt` float DEFAULT NULL,
  `liner1_id` float DEFAULT NULL,
  `liner1_depth_md` float DEFAULT NULL,
  `liner1_tol` float DEFAULT NULL,
  `liner2_od` float DEFAULT NULL,
  `liner2_wt` float DEFAULT NULL,
  `liner2_id` float DEFAULT NULL,
  `liner2_depth_md` float DEFAULT NULL,
  `liner2_tol` float DEFAULT NULL,
  `measured_depth_unit` text CHARACTER SET utf8 COLLATE utf8_general_ci,
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `updated_at` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  UNIQUE KEY `PRIMARY` (`id`) USING HASH,
  KEY `well_uuid` (`well_uuid`) USING CLUSTERED COLUMNSTORE,
  SHARD KEY `__SHARDKEY` (`id`)
) AUTOSTATS_CARDINALITY_MODE=INCREMENTAL AUTOSTATS_HISTOGRAM_MODE=CREATE AUTOSTATS_SAMPLING=ON SQL_MODE='STRICT_ALL_TABLES';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `wireline`
--

DROP TABLE IF EXISTS `wireline`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `wireline` (
  `id` bigint(11) NOT NULL AUTO_INCREMENT,
  `stage_id` int(11) NOT NULL,
  `ccl` float DEFAULT NULL,
  `current` float DEFAULT NULL,
  `line_speed` float DEFAULT NULL,
  `line_tension` float DEFAULT NULL,
  `trigger_perfs` datetime DEFAULT NULL,
  `weight` float DEFAULT NULL,
  `measured_depth` float DEFAULT NULL,
  `voltage` float DEFAULT NULL,
  `timestamp` datetime DEFAULT NULL,
  `elapsed_time` datetime DEFAULT NULL,
  `additional` JSON COLLATE utf8_bin,
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `updated_at` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  UNIQUE KEY `PRIMARY` (`id`) USING HASH,
  KEY `stage_id` (`stage_id`) USING CLUSTERED COLUMNSTORE,
  SHARD KEY `__SHARDKEY` (`id`)
) AUTOSTATS_CARDINALITY_MODE=INCREMENTAL AUTOSTATS_HISTOGRAM_MODE=CREATE AUTOSTATS_SAMPLING=ON SQL_MODE='STRICT_ALL_TABLES';
/*!40101 SET character_set_client = @saved_cs_client */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;





CREATE TABLE `result_processed` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  well_id int(11) NOT NULL,
  `stage_id` int(11) NOT NULL,
  `approved_at` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `updated_at` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  UNIQUE KEY `PRIMARY` (`id`) USING HASH,
  KEY `stage_id` (`stage_id`) USING CLUSTERED COLUMNSTORE,
  SHARD KEY `__SHARDKEY` (`id`)
) AUTOSTATS_CARDINALITY_MODE=INCREMENTAL AUTOSTATS_HISTOGRAM_MODE=CREATE AUTOSTATS_SAMPLING=ON SQL_MODE='STRICT_ALL_TABLES';




CREATE TABLE well_metadata ( 
	id                   int(11) NOT NULL AUTO_INCREMENT,
	well_id              int(11) NOT NULL,
	meta_data_json       json  NOT NULL    ,
	created_at           datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
	updated_at           datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  UNIQUE KEY `PRIMARY` (`id`) USING HASH,
  KEY `well_id` (`well_id`) USING CLUSTERED COLUMNSTORE,
  SHARD KEY `__SHARDKEY` (`id`)
 ) AUTOSTATS_CARDINALITY_MODE=INCREMENTAL AUTOSTATS_HISTOGRAM_MODE=CREATE AUTOSTATS_SAMPLING=ON SQL_MODE='STRICT_ALL_TABLES';

CREATE TABLE well_metadata_data ( 
	id                   int  NOT NULL    PRIMARY KEY,
	well_metadata_id     int  NOT NULL    ,
	depth                float DEFAULT NULL,
	latitude             float DEFAULT NULL,
	created_at           datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
	updated_at           datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,   
    UNIQUE KEY `PRIMARY` (`id`) USING HASH,
  KEY `well_metadata_id` (`well_metadata_id`) USING CLUSTERED COLUMNSTORE,
  SHARD KEY `__SHARDKEY` (`id`) 
) AUTOSTATS_CARDINALITY_MODE=INCREMENTAL AUTOSTATS_HISTOGRAM_MODE=CREATE AUTOSTATS_SAMPLING=ON SQL_MODE='STRICT_ALL_TABLES';

