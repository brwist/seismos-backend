-- SET GLOBAL default_table_type = 'columnstore';

DROP DATABASE IF EXISTS seismos;
CREATE DATABASE seismos;
USE seismos;

-- DROP DATABASE IF EXISTS seismos_franck_test;
-- CREATE DATABASE seismos_franck_test;
-- USE seismos_franck_test;

--
-- Table structure for table backside_pressure
--

DROP TABLE IF EXISTS backside_pressure;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE backside_pressure (
  id bigint NOT NULL AUTO_INCREMENT,
  stage_id int NOT NULL,
  value float NOT NULL,
  created_at datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  updated_at datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  UNIQUE KEY `PRIMARY` (id) USING HASH,
  KEY stage_id (stage_id) USING CLUSTERED COLUMNSTORE,
  SHARD KEY idx_SHARDKEY (id)
) AUTOSTATS_CARDINALITY_MODE=INCREMENTAL AUTOSTATS_HISTOGRAM_MODE=CREATE AUTOSTATS_SAMPLING=ON SQL_MODE='STRICT_ALL_TABLES';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table basin_name
--

DROP TABLE IF EXISTS basin_name;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE basin_name (
  id bigint NOT NULL AUTO_INCREMENT,
  basin_name text CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  created_at datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  updated_at datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  UNIQUE KEY `PRIMARY` (id) USING HASH,
  KEY id (id) USING CLUSTERED COLUMNSTORE,
  SHARD KEY idx_SHARDKEY (id)
) AUTOSTATS_CARDINALITY_MODE=INCREMENTAL AUTOSTATS_HISTOGRAM_MODE=CREATE AUTOSTATS_SAMPLING=ON SQL_MODE='STRICT_ALL_TABLES';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table chem_fluids
--

DROP TABLE IF EXISTS chem_fluids;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE chem_fluids (
  id bigint NOT NULL AUTO_INCREMENT,
  stage_id int NOT NULL,
  `fluid_type_name` varchar(50) NULL,
  `chem_trade_name` varchar(50) NULL,
  `chem_name` varchar(50) NULL,
  `volume` float NULL,
  `volume_unit` varchar(10) NULL,
  `volume_concentration` float NULL,
  `volume_concentration_unit` varchar(10) NULL,
  `dry_total` float NULL,
  `dry_total_unit` varchar(10) NULL,
  `dry_concentration` float NULL,
  `dry_concentration_unit` varchar(10) NULL,
  `acid` float NULL,
  `acid_unit` varchar(10) NULL,
  `design_acid_vol` int NULL,
  `clay_stabilizer` float NULL,
  `clay_stabilizer_unit` varchar(10) NULL,
  `misc` varchar(10) NULL,
  `bulk_modulus` float NULL,
  `bulk_modulus_unit` varchar(10) NULL,
  `base_fluid_density` float NULL,
  `base_fluid_type` varchar(35) NULL,
  `max_conc_density` float NULL,
  created_at datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  updated_at datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  UNIQUE KEY `PRIMARY` (id) USING HASH,
  KEY stage_id (stage_id) USING CLUSTERED COLUMNSTORE,
  SHARD KEY idx_SHARDKEY (id)
) AUTOSTATS_CARDINALITY_MODE=INCREMENTAL AUTOSTATS_HISTOGRAM_MODE=CREATE AUTOSTATS_SAMPLING=ON SQL_MODE='STRICT_ALL_TABLES';
/*!40101 SET character_set_client = @saved_cs_client */;


--
-- Table structure for table formation_fuild_injection
--
DROP TABLE IF EXISTS formation_fluid_injection;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE formation_fluid_injection (
  id bigint NOT NULL AUTO_INCREMENT,
  chem_fluid_id int NOT NULL,
  `description` varchar(50) NULL,
  `bbls` int NULL,
  `ppg` float NULL,
  created_at datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  updated_at datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  UNIQUE KEY `PRIMARY` (id) USING HASH,
  KEY chem_fluid_id (chem_fluid_id) USING CLUSTERED COLUMNSTORE,
  SHARD KEY idx_SHARDKEY (id)
) AUTOSTATS_CARDINALITY_MODE=INCREMENTAL AUTOSTATS_HISTOGRAM_MODE=CREATE AUTOSTATS_SAMPLING=ON SQL_MODE='STRICT_ALL_TABLES';



DROP TABLE IF EXISTS clean;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE clean (
  id bigint NOT NULL AUTO_INCREMENT,
  stage_id int NOT NULL,
  total_clean_rate float DEFAULT NULL,
  total_clean_rate2 float DEFAULT NULL,
  created_at datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  updated_at datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  UNIQUE KEY `PRIMARY` (id) USING HASH,
  KEY stage_id (stage_id) USING CLUSTERED COLUMNSTORE,
  SHARD KEY idx_SHARDKEY (id)
) AUTOSTATS_CARDINALITY_MODE=INCREMENTAL AUTOSTATS_HISTOGRAM_MODE=CREATE AUTOSTATS_SAMPLING=ON SQL_MODE='STRICT_ALL_TABLES';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table client
--

DROP TABLE IF EXISTS client;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE client (
  id bigint NOT NULL AUTO_INCREMENT,
  client_uuid char(36) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  client_name text CHARACTER SET utf8 COLLATE utf8_general_ci,
  customer_field_rep_id text CHARACTER SET utf8 COLLATE utf8_general_ci,
  project_id int DEFAULT NULL,
  operator_name text CHARACTER SET utf8 COLLATE utf8_general_ci,
  service_company_name text CHARACTER SET utf8 COLLATE utf8_general_ci,
  wireline_company text CHARACTER SET utf8 COLLATE utf8_general_ci,
  other_comments text CHARACTER SET utf8 COLLATE utf8_general_ci,
  created_at datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  updated_at datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  UNIQUE KEY `PRIMARY` (id) USING HASH,
  KEY client_uuid (client_uuid) USING CLUSTERED COLUMNSTORE,
  SHARD KEY idx_SHARDKEY (id)
) AUTOSTATS_CARDINALITY_MODE=INCREMENTAL AUTOSTATS_HISTOGRAM_MODE=CREATE AUTOSTATS_SAMPLING=ON SQL_MODE='STRICT_ALL_TABLES';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table coil_tubing
--

DROP TABLE IF EXISTS coil_tubing;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE coil_tubing (
  id bigint NOT NULL AUTO_INCREMENT,
  stage_id int NOT NULL,
  `timestamp` decimal(13,3) Null,
  pump_rate float DEFAULT NULL,
  pump_rate_unit text CHARACTER SET utf8 COLLATE utf8_general_ci,
  tubing_pressure float DEFAULT NULL,
  tubing_pressure_unit text CHARACTER SET utf8 COLLATE utf8_general_ci,
  depth float DEFAULT NULL,
  depth_unit text CHARACTER SET utf8 COLLATE utf8_general_ci,
  flowback_rate float DEFAULT NULL,
  flowback_unit text CHARACTER SET utf8 COLLATE utf8_general_ci,
  trip_in_out_rate float DEFAULT NULL,
  trip_in_out_rate_unit text CHARACTER SET utf8 COLLATE utf8_general_ci,
  weight_on_bit float DEFAULT NULL,
  weight_on_bit_unit text CHARACTER SET utf8 COLLATE utf8_general_ci,
  created_at datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  updated_at datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  UNIQUE KEY `PRIMARY` (id) USING HASH,
  KEY stage_id (stage_id) USING CLUSTERED COLUMNSTORE,
  SHARD KEY idx_SHARDKEY (id)
) AUTOSTATS_CARDINALITY_MODE=INCREMENTAL AUTOSTATS_HISTOGRAM_MODE=CREATE AUTOSTATS_SAMPLING=ON SQL_MODE='STRICT_ALL_TABLES';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table county_name
--

DROP TABLE IF EXISTS county_name;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE county_name (
  id bigint NOT NULL AUTO_INCREMENT,
  county_name text CHARACTER SET utf8 COLLATE utf8_general_ci,
  created_at datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  updated_at datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  UNIQUE KEY `PRIMARY` (id) USING HASH,
  KEY id (id) USING CLUSTERED COLUMNSTORE,
  SHARD KEY idx_SHARDKEY (id)
) AUTOSTATS_CARDINALITY_MODE=INCREMENTAL AUTOSTATS_HISTOGRAM_MODE=CREATE AUTOSTATS_SAMPLING=ON SQL_MODE='STRICT_ALL_TABLES';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table crew
--

DROP TABLE IF EXISTS crew;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE crew (
  id bigint NOT NULL AUTO_INCREMENT,
  name text CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
shift text CHARACTER SET utf8 COLLATE utf8_general_ci,
  role enum('admin','manager','engineer') CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  manager_id int DEFAULT NULL,
  created_at datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  updated_at datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  UNIQUE KEY `PRIMARY` (id) USING HASH,
  KEY id (id) USING CLUSTERED COLUMNSTORE,
  SHARD KEY idx_SHARDKEY (id)
) AUTOSTATS_CARDINALITY_MODE=INCREMENTAL AUTOSTATS_HISTOGRAM_MODE=CREATE AUTOSTATS_SAMPLING=ON SQL_MODE='STRICT_ALL_TABLES';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table customer_field_rep
--

DROP TABLE IF EXISTS customer_field_rep;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE customer_field_rep (
  id bigint NOT NULL AUTO_INCREMENT,
  name text CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  email varchar(100)  NULL,
  customer_field_rep_num int DEFAULT NULL,
  created_at datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  updated_at datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  UNIQUE KEY `PRIMARY` (id) USING HASH,
  KEY id (id) USING CLUSTERED COLUMNSTORE,
  SHARD KEY idx_SHARDKEY (id)
) AUTOSTATS_CARDINALITY_MODE=INCREMENTAL AUTOSTATS_HISTOGRAM_MODE=CREATE AUTOSTATS_SAMPLING=ON SQL_MODE='STRICT_ALL_TABLES';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table default_advance_val
--

DROP TABLE IF EXISTS default_advance_val;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE default_advance_val (
  id bigint NOT NULL AUTO_INCREMENT,
  well_id int DEFAULT NULL,
  model varchar(40) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  response varchar(40) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  source varchar(40) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  layer int DEFAULT NULL,
  viscosity float DEFAULT NULL,
  density float DEFAULT NULL,
  compressibility float DEFAULT NULL,
  f_low_hz float DEFAULT NULL,
  f_high_hz float DEFAULT NULL,
  new_sample_rate float DEFAULT NULL,
  data_sample_rate float DEFAULT NULL,
  `algorithm` varchar(40) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  total_width float DEFAULT NULL,
  grid_density float DEFAULT NULL,
  weighting varchar(10) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  wlevexp float DEFAULT NULL,
  `loop` varchar(10) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  method varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  tolerance float DEFAULT NULL,
  iteration int DEFAULT NULL,
  created_at datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  updated_at datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  UNIQUE KEY `PRIMARY` (id) USING HASH,
  KEY well_id (well_id) USING CLUSTERED COLUMNSTORE,
  SHARD KEY idx_SHARDKEY (id)
) AUTOSTATS_CARDINALITY_MODE=INCREMENTAL AUTOSTATS_HISTOGRAM_MODE=CREATE AUTOSTATS_SAMPLING=ON SQL_MODE='STRICT_ALL_TABLES';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table default_param_val
--

DROP TABLE IF EXISTS default_param_val;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE default_param_val (
  id bigint NOT NULL AUTO_INCREMENT,
  well_id int DEFAULT NULL,
  c1_min float DEFAULT NULL,
  c2_min float DEFAULT NULL,
  c1_max float DEFAULT NULL,
  c2_max float DEFAULT NULL,
  c3_min float DEFAULT NULL,
  c3_max float DEFAULT NULL,
  q_min int DEFAULT NULL,
  q_max int DEFAULT NULL,
  k_min float DEFAULT NULL,
  k_max float DEFAULT NULL,
  w_min float DEFAULT NULL,
  w_max float DEFAULT NULL,
  created_at datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  updated_at datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  UNIQUE KEY `PRIMARY` (id) USING HASH,
  KEY well_id (well_id) USING CLUSTERED COLUMNSTORE,
  SHARD KEY idx_SHARDKEY (id)
) AUTOSTATS_CARDINALITY_MODE=INCREMENTAL AUTOSTATS_HISTOGRAM_MODE=CREATE AUTOSTATS_SAMPLING=ON SQL_MODE='STRICT_ALL_TABLES';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table default_val
--

DROP TABLE IF EXISTS default_val;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE default_val (
  id bigint NOT NULL AUTO_INCREMENT,
  well_id int DEFAULT NULL,
  pres float DEFAULT NULL,
  young float DEFAULT NULL,
  overburden float DEFAULT NULL,
  poisson float DEFAULT NULL,
  eta_cp int DEFAULT NULL,
  fluidt int DEFAULT NULL,
  tect float DEFAULT NULL,
  fluid_density float DEFAULT NULL,
  diverter_time float DEFAULT NULL,
  met_res float DEFAULT NULL,
  ffkw_correction int DEFAULT NULL,
  k_mpa int DEFAULT NULL,
  nu_lim int DEFAULT NULL,
  per_red int DEFAULT NULL,
  start1 int DEFAULT NULL,
  beta_ss float DEFAULT NULL,
  st_lim int DEFAULT NULL,
  biot int DEFAULT NULL,
  shadow int DEFAULT NULL,
fit_end_point Varchar(30) DEFAULT NULL,
NG float DEFAULT NULL,
breaker_YN Char(1)  DEFAULT NULL,
poisson_method int  DEFAULT NULL,
plotraw_YN Char(1)  DEFAULT NULL,
use_wns_YN Char(1)  DEFAULT NULL,
fit_iteration int  DEFAULT NULL,
start2 float DEFAULT NULL,
stage_ques float DEFAULT NULL,
poisson_var_YN Char(1)  DEFAULT NULL,
stress_shadow_YN Char(1)  DEFAULT NULL,
skip_losses_YN Char(1)  DEFAULT NULL,
use_wncuts_YN Char(1)  DEFAULT NULL,
wns int DEFAULT NULL,
visc_var float,
ac_type int,
ac_vol float,
ac_per float,
rc_type int,
created_at datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
updated_at datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
UNIQUE KEY `PRIMARY` (id) USING HASH,
KEY well_id (well_id) USING CLUSTERED COLUMNSTORE,
SHARD KEY idx_SHARDKEY (id)
) AUTOSTATS_CARDINALITY_MODE=INCREMENTAL AUTOSTATS_HISTOGRAM_MODE=CREATE AUTOSTATS_SAMPLING=ON SQL_MODE='STRICT_ALL_TABLES';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table equipment
--

DROP TABLE IF EXISTS equipment;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE equipment (
  id bigint NOT NULL AUTO_INCREMENT,
  trailer_id int DEFAULT NULL,
  powerpack_id int DEFAULT NULL,
  source_id int DEFAULT NULL,
  accumulator_id int DEFAULT NULL,
  hydrophones_id int DEFAULT NULL,
  transducer_id int DEFAULT NULL,
  hotspot_id int DEFAULT NULL,
  computer_id int DEFAULT NULL,
  pressure_counter double DEFAULT NULL,
  created_at datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  updated_at datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  UNIQUE KEY `PRIMARY` (id) USING HASH,
  KEY id (id) USING CLUSTERED COLUMNSTORE,
  SHARD KEY idx_SHARDKEY (id)
) AUTOSTATS_CARDINALITY_MODE=INCREMENTAL AUTOSTATS_HISTOGRAM_MODE=CREATE AUTOSTATS_SAMPLING=ON SQL_MODE='STRICT_ALL_TABLES';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table ff_parameter_set
--

DROP TABLE IF EXISTS ff_parameter_set;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE ff_parameter_set (
  id int NOT NULL,
  username text CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  date_created datetime DEFAULT NULL,
  shut_in_period_start datetime DEFAULT NULL,
  sample_rate float DEFAULT NULL,
  total_samples float DEFAULT NULL,
  tvd float DEFAULT NULL,
  viscosity float DEFAULT NULL,
  compressibility_mpa float DEFAULT NULL,
  poisson_ratio float DEFAULT NULL,
  youngs_modulus_mpa float DEFAULT NULL,
  volume_pumped float DEFAULT NULL,
  proppant_volume_pumped_bbl float DEFAULT NULL,
  average_injection_rate float DEFAULT NULL,
  tectonic_component float DEFAULT NULL,
  created_at datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  updated_at datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  UNIQUE KEY `PRIMARY` (id) USING HASH,
  KEY id (id) USING CLUSTERED COLUMNSTORE,
  SHARD KEY idx_SHARDKEY (id)
) AUTOSTATS_CARDINALITY_MODE=INCREMENTAL AUTOSTATS_HISTOGRAM_MODE=CREATE AUTOSTATS_SAMPLING=ON SQL_MODE='STRICT_ALL_TABLES';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table ff_processing_result
--

DROP TABLE IF EXISTS ff_processing_result;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE ff_processing_result (
  id int NOT NULL,
  stage_id int NOT NULL,
  ff_parameter_id int NOT NULL,
  timestamp datetime DEFAULT NULL,
  length float DEFAULT NULL,
  width float DEFAULT NULL,
  height float DEFAULT NULL,
  conductivity float DEFAULT NULL,
  minimum_stress float DEFAULT NULL,
  minimun_stress_gradient float DEFAULT NULL,
  net_pressure float DEFAULT NULL,
  fracture_pressure_gradient float DEFAULT NULL,
  reservoir_pressure float DEFAULT NULL,
  reservoir_pressure_gradient float DEFAULT NULL,
  pressure_match float DEFAULT NULL,
  fracture_efficiency float DEFAULT NULL,
  stress_shadow_pressure float DEFAULT NULL,
  calculated_poisson_ratio float DEFAULT NULL,
  nwb_region_size float DEFAULT NULL,
  nwb_compressibility float DEFAULT NULL,
  nwb_permeability float DEFAULT NULL,
  ff_version text CHARACTER SET utf8 COLLATE utf8_general_ci,
  unit text CHARACTER SET utf8 COLLATE utf8_general_ci,
  created_at datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  updated_at datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  UNIQUE KEY `PRIMARY` (id) USING HASH,
  KEY id (id) USING CLUSTERED COLUMNSTORE,
  SHARD KEY idx_SHARDKEY (id)
) AUTOSTATS_CARDINALITY_MODE=INCREMENTAL AUTOSTATS_HISTOGRAM_MODE=CREATE AUTOSTATS_SAMPLING=ON SQL_MODE='STRICT_ALL_TABLES';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table field_notes
--

DROP TABLE IF EXISTS field_notes;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE field_notes (
  id bigint NOT NULL AUTO_INCREMENT,
  well_id int NOT NULL,
  comment_timestamp datetime DEFAULT NULL,
  comment_content text CHARACTER SET utf8 COLLATE utf8_general_ci,
  comment_by text CHARACTER SET utf8 COLLATE utf8_general_ci,
  created_at datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  updated_at datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  UNIQUE KEY `PRIMARY` (id) USING HASH,
  KEY well_id (well_id) USING CLUSTERED COLUMNSTORE,
  SHARD KEY idx_SHARDKEY (id)
) AUTOSTATS_CARDINALITY_MODE=INCREMENTAL AUTOSTATS_HISTOGRAM_MODE=CREATE AUTOSTATS_SAMPLING=ON SQL_MODE='STRICT_ALL_TABLES';
/*!40101 SET character_set_client = @saved_cs_client */;



-- Table structure for table fluid_type_lookup
--
DROP TABLE IF EXISTS fluid_type_lookup;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE fluid_type_lookup (
  id bigint NOT NULL AUTO_INCREMENT,
  value int NOT NULL,
  created_at datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  updated_at datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  UNIQUE KEY `PRIMARY` (id) USING HASH,
  KEY id (id) USING CLUSTERED COLUMNSTORE,
  SHARD KEY idx_SHARDKEY (id)
) AUTOSTATS_CARDINALITY_MODE=INCREMENTAL AUTOSTATS_HISTOGRAM_MODE=CREATE AUTOSTATS_SAMPLING=ON SQL_MODE='STRICT_ALL_TABLES';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table formation_top
--

DROP TABLE IF EXISTS formation_top;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE formation_top (
  id bigint NOT NULL AUTO_INCREMENT,
  well_id int NOT NULL,
  measured_depth float DEFAULT NULL,
  inclination float DEFAULT NULL,
  azimuth float DEFAULT NULL,
  X float DEFAULT NULL,
  Y float DEFAULT NULL,
  Z float DEFAULT NULL,
  target_upper float DEFAULT NULL,
  target_lower float DEFAULT NULL,
  l1_upper float DEFAULT NULL,
  l1_lower float DEFAULT NULL,
  l2_upper float DEFAULT NULL,
  l2_lower float DEFAULT NULL,
  l3_upper float DEFAULT NULL,
  l3_lower float DEFAULT NULL,
  l4_upper float DEFAULT NULL,
  l4_lower float DEFAULT NULL,
  l5_upper float DEFAULT NULL,
  l5_lower float DEFAULT NULL,
  l6_upper float DEFAULT NULL,
  l6_lower float DEFAULT NULL,
  l7_upper float DEFAULT NULL,
  l7_lower float DEFAULT NULL,
  l8_upper float DEFAULT NULL,
  l8_lower float DEFAULT NULL,
  l9_upper float DEFAULT NULL,
  l9_lower float DEFAULT NULL,
  l10_upper float DEFAULT NULL,
  l10_lower float DEFAULT NULL,
  additional JSON COLLATE utf8_bin,
  created_at datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  updated_at datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  UNIQUE KEY `PRIMARY` (id) USING HASH,
  KEY well_id (well_id) USING CLUSTERED COLUMNSTORE,
  SHARD KEY idx_SHARDKEY (id)
) AUTOSTATS_CARDINALITY_MODE=INCREMENTAL AUTOSTATS_HISTOGRAM_MODE=CREATE AUTOSTATS_SAMPLING=ON SQL_MODE='STRICT_ALL_TABLES';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table formation_top_reference
--

DROP TABLE IF EXISTS formation_top_reference;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE formation_top_reference (
  id bigint NOT NULL AUTO_INCREMENT,
  formation_top_id int NOT NULL,
  l1 text CHARACTER SET utf8 COLLATE utf8_general_ci,
  l2 text CHARACTER SET utf8 COLLATE utf8_general_ci,
  l3 text CHARACTER SET utf8 COLLATE utf8_general_ci,
  l4 text CHARACTER SET utf8 COLLATE utf8_general_ci,
  l5 text CHARACTER SET utf8 COLLATE utf8_general_ci,
  l6 text CHARACTER SET utf8 COLLATE utf8_general_ci,
  l7 text CHARACTER SET utf8 COLLATE utf8_general_ci,
  l8 text CHARACTER SET utf8 COLLATE utf8_general_ci,
  l9 text CHARACTER SET utf8 COLLATE utf8_general_ci,
  l10 text CHARACTER SET utf8 COLLATE utf8_general_ci,
  created_at datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  updated_at datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  UNIQUE KEY `PRIMARY` (id) USING HASH,
  KEY id (id) USING CLUSTERED COLUMNSTORE,
  SHARD KEY idx_SHARDKEY (id)
) AUTOSTATS_CARDINALITY_MODE=INCREMENTAL AUTOSTATS_HISTOGRAM_MODE=CREATE AUTOSTATS_SAMPLING=ON SQL_MODE='STRICT_ALL_TABLES';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table frac_design_lookup
--

DROP TABLE IF EXISTS frac_design_lookup;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE frac_design_lookup (
  id bigint NOT NULL AUTO_INCREMENT,
  value int NOT NULL,
  created_at datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  updated_at datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  UNIQUE KEY `PRIMARY` (id) USING HASH,
  KEY id (id) USING CLUSTERED COLUMNSTORE,
  SHARD KEY idx_SHARDKEY (id)
) AUTOSTATS_CARDINALITY_MODE=INCREMENTAL AUTOSTATS_HISTOGRAM_MODE=CREATE AUTOSTATS_SAMPLING=ON SQL_MODE='STRICT_ALL_TABLES';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table geophysical_properties
--

DROP TABLE IF EXISTS geophysical_properties;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE geophysical_properties (
  id bigint NOT NULL AUTO_INCREMENT,
  file_metadata_id int NOT NULL,
  measured_depth float DEFAULT NULL,
  young_modulus float DEFAULT NULL,
  poisson_ratio float DEFAULT NULL,
  min_stress float DEFAULT NULL,
  dynamic_horizontal_young_modulus float DEFAULT NULL,
  static_horizontal_young_modulus float DEFAULT NULL,
  static_vertical_young_modulus float DEFAULT NULL,
  horizontal_poisson_ratio float DEFAULT NULL,
  vertical_possion_ratio float DEFAULT NULL,
  pore_pressure float DEFAULT NULL,
  tensile_strength float DEFAULT NULL,
  vertical_stress_gradient float DEFAULT NULL,
  json_data JSON COLLATE utf8_bin,
  created_at datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  updated_at datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  UNIQUE KEY `PRIMARY` (id) USING HASH,
  KEY well_id (file_metadata_id) USING CLUSTERED COLUMNSTORE,
  SHARD KEY idx_SHARDKEY (id)
) AUTOSTATS_CARDINALITY_MODE=INCREMENTAL AUTOSTATS_HISTOGRAM_MODE=CREATE AUTOSTATS_SAMPLING=ON SQL_MODE='STRICT_ALL_TABLES';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table job_info
--

DROP TABLE IF EXISTS job_info;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE job_info (
  id bigint NOT NULL AUTO_INCREMENT,
  job_id int not null,
  project_id int not null,
  job_name text CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  afe_id int DEFAULT NULL,
  job_start_date datetime DEFAULT NULL,
  job_end_date datetime DEFAULT NULL,
  job_type_id int DEFAULT NULL,
  created_at datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  updated_at datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  UNIQUE KEY `PRIMARY` (id) USING HASH,
  KEY id (id) USING CLUSTERED COLUMNSTORE,
  SHARD KEY idx_SHARDKEY (id)
) AUTOSTATS_CARDINALITY_MODE=INCREMENTAL AUTOSTATS_HISTOGRAM_MODE=CREATE AUTOSTATS_SAMPLING=ON SQL_MODE='STRICT_ALL_TABLES';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table job_type
--

DROP TABLE IF EXISTS job_type;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE job_type (
  id bigint NOT NULL AUTO_INCREMENT,
  value text CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  created_at datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  updated_at datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  UNIQUE KEY `PRIMARY` (id) USING HASH,
  KEY id (id) USING CLUSTERED COLUMNSTORE,
  SHARD KEY idx_SHARDKEY (id)
) AUTOSTATS_CARDINALITY_MODE=INCREMENTAL AUTOSTATS_HISTOGRAM_MODE=CREATE AUTOSTATS_SAMPLING=ON SQL_MODE='STRICT_ALL_TABLES';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table location_info
--

DROP TABLE IF EXISTS location_info;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE location_info (
  id bigint NOT NULL AUTO_INCREMENT,
  county_name_id int NOT NULL,
  job_info_id int NOT NULL,
  basin_name_id int NOT NULL,
  state_id int NOT NULL,
  created_at datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  updated_at datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  UNIQUE KEY `PRIMARY` (id,county_name_id,basin_name_id,state_id) USING HASH,
  KEY id (id) USING CLUSTERED COLUMNSTORE,
  SHARD KEY idx_SHARDKEY (id,county_name_id,basin_name_id,state_id)
) AUTOSTATS_CARDINALITY_MODE=INCREMENTAL AUTOSTATS_HISTOGRAM_MODE=CREATE AUTOSTATS_SAMPLING=ON SQL_MODE='STRICT_ALL_TABLES';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table mud_log
--

DROP TABLE IF EXISTS mud_log;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE mud_log (
  id bigint NOT NULL AUTO_INCREMENT,
  file_metadata_id int NOT NULL,
  measure_depth float DEFAULT NULL,
  siltstone float DEFAULT NULL,
  sand float DEFAULT NULL,
  coal float DEFAULT NULL,
  limestone float DEFAULT NULL,
  dolomite float DEFAULT NULL,
  salt float DEFAULT NULL,
  chert float DEFAULT NULL,
  chalk float DEFAULT NULL,
  anhydrite float DEFAULT NULL,
  shale float DEFAULT NULL,
  gamma_ray float DEFAULT NULL,
  clay float DEFAULT NULL,
  
  marl float DEFAULT NULL,
  rate_of_penetration float DEFAULT NULL,
  rpm float DEFAULT NULL,
  weight_on_bit float DEFAULT NULL,
  total_gas float DEFAULT NULL,
  methane float DEFAULT NULL,
  ethane float DEFAULT NULL,
  propane float DEFAULT NULL,
  isobutane float DEFAULT NULL,
  butane float DEFAULT NULL,
  isopentane float DEFAULT NULL,
  pentane float DEFAULT NULL,
  json_data JSON COLLATE utf8_bin,
  created_at datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  updated_at datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  UNIQUE KEY `PRIMARY` (id) USING HASH,
  KEY well_id (file_metadata_id) USING CLUSTERED COLUMNSTORE,
  SHARD KEY idx_SHARDKEY (id)
) AUTOSTATS_CARDINALITY_MODE=INCREMENTAL AUTOSTATS_HISTOGRAM_MODE=CREATE AUTOSTATS_SAMPLING=ON SQL_MODE='STRICT_ALL_TABLES';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table mwd_report
--

DROP TABLE IF EXISTS mwd_report;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE mwd_report (
  id bigint NOT NULL AUTO_INCREMENT,
  file_metadata_id int NOT NULL,
  measured_depth float DEFAULT NULL,
  gamma_ray float DEFAULT NULL,
  created_at datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  updated_at datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  UNIQUE KEY `PRIMARY` (id) USING HASH,
  KEY well_id (file_metadata_id) USING CLUSTERED COLUMNSTORE,
  SHARD KEY idx_SHARDKEY (id)
) AUTOSTATS_CARDINALITY_MODE=INCREMENTAL AUTOSTATS_HISTOGRAM_MODE=CREATE AUTOSTATS_SAMPLING=ON SQL_MODE='STRICT_ALL_TABLES';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table nf_parameter_set
--

DROP TABLE IF EXISTS nf_parameter_set;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE nf_parameter_set (
  id int NOT NULL,
  crew_id int NOT NULL,
  daq_sensor_id int NOT NULL,
    parameter_type varchar(10) NOT NULL,
  t_0 DATETIME(6) NULL,
pulsetrain_duration float null,
clock_offset float null,
hp_channel_id int null,
p_channel_id int null, 
n_pulses int, 
inv_method int, 
pop_size int, 
noise_level float,
deconv_layer int, 
c1_min int, 
c1_max int, 
c2_min int, 
c2_max int, 
c3_min int, 
c3_max int, 
q1_min float , 
q1_max float, 
q2_min float,
q2_max float ,
q3_min float,
q3_max float,
k_min float,
k_max float,
w_min float,
w_max float,
w_inch float, 
mu_cp float,
rho_kgm3 float,
b_1_psi float,
 additional json NULL,
  created_at datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  updated_at datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  UNIQUE KEY `PRIMARY` (id) USING HASH,
  KEY id (id) USING CLUSTERED COLUMNSTORE,
  SHARD KEY idx_SHARDKEY (id)
) AUTOSTATS_CARDINALITY_MODE=INCREMENTAL AUTOSTATS_HISTOGRAM_MODE=CREATE AUTOSTATS_SAMPLING=ON SQL_MODE='STRICT_ALL_TABLES';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table nf_processing_result
--

DROP TABLE IF EXISTS nf_processing_result;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE nf_processing_result (
  id bigint NOT NULL AUTO_INCREMENT,
  stage_id int NOT NULL,
nf_param_id int DEFAULT NULL,
  timestamp datetime DEFAULT NULL,
  user_id text CHARACTER SET utf8 COLLATE utf8_general_ci,
  c0 float DEFAULT NULL,
  c1 float DEFAULT NULL,
  c2 float DEFAULT NULL,
  c3 float DEFAULT NULL,
  q0 float DEFAULT NULL,
  q1 float DEFAULT NULL,
  q2 float DEFAULT NULL,
  q3 float DEFAULT NULL,
  fit_error float DEFAULT NULL,
  connect_ops_risk float DEFAULT NULL,
  connect_efficiency float DEFAULT NULL,
  connect_condition float DEFAULT NULL,
  created_at datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  updated_at datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  UNIQUE KEY `PRIMARY` (id) USING HASH,
  KEY stage_id (stage_id) USING CLUSTERED COLUMNSTORE,
  SHARD KEY idx_SHARDKEY (id)
) AUTOSTATS_CARDINALITY_MODE=INCREMENTAL AUTOSTATS_HISTOGRAM_MODE=CREATE AUTOSTATS_SAMPLING=ON SQL_MODE='STRICT_ALL_TABLES';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table pad
--

DROP TABLE IF EXISTS pad;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE pad (
  id bigint NOT NULL AUTO_INCREMENT,
  pad_uuid char(36) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  project_id int NOT NULL,
  pad_name text CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  number_of_wells int DEFAULT NULL,
  well_spacing float DEFAULT NULL,
  created_at datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  updated_at datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  UNIQUE KEY `PRIMARY` (id) USING HASH,
  KEY pad_uuid (pad_uuid) USING CLUSTERED COLUMNSTORE,
  SHARD KEY idx_SHARDKEY (id)
) AUTOSTATS_CARDINALITY_MODE=INCREMENTAL AUTOSTATS_HISTOGRAM_MODE=CREATE AUTOSTATS_SAMPLING=ON SQL_MODE='STRICT_ALL_TABLES';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table perforation
--

DROP TABLE IF EXISTS perforation;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE perforation (
   id int NOT NULL AUTO_INCREMENT,
  stage_id int NOT NULL,
  `order_num` int NULL,
  `ordinal` float NULL,
  `top_measured_depth` float NULL,
  `bottom_measured_depth` float NULL,
  `depth_unit` varchar(10) NULL,
  `shot_number` int NULL,
  `shot_density` float NULL,
  `shot_density_unit` varchar(10) NULL,
  `shot_count` integer NULL,
  `phasing` int NULL,
  `conveyance_method` varchar(20) NULL,
  `charge_type` varchar(20) NULL,
  `charge_size` double NULL,
  `charge_size_unit` varchar(10) NULL,
  `estimated_hole_diameter` float NULL,
  `estimated_hole_diameter_unit` varchar(10) NULL,
  `perf_plug_num` int NULL,
  `perf_start_time` datetime NULL,
  `perf_end_time` datetime NULL,
  `bottom_perf` double(255, 0) NULL,
  `perf_gun_description` varchar(255) NULL,
  created_at datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  updated_at datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  UNIQUE KEY `PRIMARY` (id) USING HASH,
  KEY stage_id (stage_id) USING CLUSTERED COLUMNSTORE,
  SHARD KEY idx_SHARDKEY (id)
) AUTOSTATS_CARDINALITY_MODE=INCREMENTAL AUTOSTATS_HISTOGRAM_MODE=CREATE AUTOSTATS_SAMPLING=ON SQL_MODE='STRICT_ALL_TABLES';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table plug_depth_unit_lookup
--

DROP TABLE IF EXISTS plug_depth_unit_lookup;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE plug_depth_unit_lookup (
  id bigint NOT NULL AUTO_INCREMENT,
  value text CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  created_at datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  updated_at datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  UNIQUE KEY `PRIMARY` (id) USING HASH,
  KEY id (id) USING CLUSTERED COLUMNSTORE,
  SHARD KEY idx_SHARDKEY (id)
) AUTOSTATS_CARDINALITY_MODE=INCREMENTAL AUTOSTATS_HISTOGRAM_MODE=CREATE AUTOSTATS_SAMPLING=ON SQL_MODE='STRICT_ALL_TABLES';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table plug_name_lookup
--

DROP TABLE IF EXISTS plug_name_lookup;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE plug_name_lookup (
  id bigint NOT NULL AUTO_INCREMENT,
  value float NOT NULL,
  created_at datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  updated_at datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  UNIQUE KEY `PRIMARY` (id) USING HASH,
  KEY id (id) USING CLUSTERED COLUMNSTORE,
  SHARD KEY idx_SHARDKEY (id)
) AUTOSTATS_CARDINALITY_MODE=INCREMENTAL AUTOSTATS_HISTOGRAM_MODE=CREATE AUTOSTATS_SAMPLING=ON SQL_MODE='STRICT_ALL_TABLES';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table post_frac
--

DROP TABLE IF EXISTS post_frac;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE post_frac (
  id bigint NOT NULL AUTO_INCREMENT,
  stage_id int DEFAULT NULL,
  post_start_time datetime DEFAULT NULL,
  post_end_time datetime DEFAULT NULL,
  post_frac_num_pulse text CHARACTER SET utf8 COLLATE utf8_general_ci,
  post_frac_pulse_notes text CHARACTER SET utf8 COLLATE utf8_general_ci,
  created_at datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  updated_at datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  UNIQUE KEY `PRIMARY` (id) USING HASH,
  KEY stage_id (stage_id) USING CLUSTERED COLUMNSTORE,
  SHARD KEY idx_SHARDKEY (id)
) AUTOSTATS_CARDINALITY_MODE=INCREMENTAL AUTOSTATS_HISTOGRAM_MODE=CREATE AUTOSTATS_SAMPLING=ON SQL_MODE='STRICT_ALL_TABLES';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table pre_frac
--

DROP TABLE IF EXISTS pre_frac;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE pre_frac (
  id bigint NOT NULL AUTO_INCREMENT,
  stage_id int DEFAULT NULL,
  pre_start_time datetime DEFAULT NULL,
  pre_end_time datetime DEFAULT NULL,
  pre_frac_num_pulse text CHARACTER SET utf8 COLLATE utf8_general_ci,
  pre_frac_pulse_notes text CHARACTER SET utf8 COLLATE utf8_general_ci,
  created_at datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  updated_at datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  UNIQUE KEY `PRIMARY` (id) USING HASH,
  KEY stage_id (stage_id) USING CLUSTERED COLUMNSTORE,
  SHARD KEY idx_SHARDKEY (id)
) AUTOSTATS_CARDINALITY_MODE=INCREMENTAL AUTOSTATS_HISTOGRAM_MODE=CREATE AUTOSTATS_SAMPLING=ON SQL_MODE='STRICT_ALL_TABLES';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table project
--

DROP TABLE IF EXISTS project;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE project (
  id bigint NOT NULL AUTO_INCREMENT,
  project_uuid char(36) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  user_id int not null,
  project_name text CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  client_id int NOT NULL,
  -- equipment_id int DEFAULT NULL,
  created_at datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  updated_at datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  UNIQUE KEY `PRIMARY` (id) USING HASH,
  KEY project_uuid (project_uuid) USING CLUSTERED COLUMNSTORE,
  SHARD KEY idx_SHARDKEY (id)
) AUTOSTATS_CARDINALITY_MODE=INCREMENTAL AUTOSTATS_HISTOGRAM_MODE=CREATE AUTOSTATS_SAMPLING=ON SQL_MODE='STRICT_ALL_TABLES';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table project_crew
--

DROP TABLE IF EXISTS project_crew;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE project_crew (
  project_crew_id bigint NOT NULL AUTO_INCREMENT,
  project_id int NOT NULL,
  crew_id int NOT NULL,
  created_at datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  updated_at datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  UNIQUE KEY `PRIMARY` (project_crew_id) USING HASH,
  KEY project_id (project_id) USING CLUSTERED COLUMNSTORE,
  SHARD KEY idx_SHARDKEY (project_crew_id)
) AUTOSTATS_CARDINALITY_MODE=INCREMENTAL AUTOSTATS_HISTOGRAM_MODE=CREATE AUTOSTATS_SAMPLING=ON SQL_MODE='STRICT_ALL_TABLES';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table proppant
--

DROP TABLE IF EXISTS proppant;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE proppant (
  id bigint NOT NULL AUTO_INCREMENT,
  stage_id int NOT NULL,
  `proppant_name` varchar(35) NOT NULL,
  `prop_mass` float NULL,
  `mass_unit` varchar(10) NULL,
  `material` varchar(25) NULL,
  `mesh_size` float NULL,
  `avg_concentration` float NULL,
  `avg_concentration_unit` varchar(10) NULL,
  `max_concentration` float NULL,
  `proppant_type_start_time` datetime NULL,
  `proppant_end_start_time` datetime NULL,
  `max_concentration_unit` varchar(10) NULL,
  `bulk_density` int NULL,
  `specific_gravity` float NULL,
  `actual_lbs` float NULL,
  `designed_lbs` float NULL,
  total_pumped_lbs float NULL,
  `total_proppant_volume` float NULL,
  created_at datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  updated_at datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  UNIQUE KEY `PRIMARY` (id) USING HASH,
  KEY stage_id (stage_id) USING CLUSTERED COLUMNSTORE,
  SHARD KEY idx_SHARDKEY (id)
) AUTOSTATS_CARDINALITY_MODE=INCREMENTAL AUTOSTATS_HISTOGRAM_MODE=CREATE AUTOSTATS_SAMPLING=ON SQL_MODE='STRICT_ALL_TABLES';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table proppant_lookup
--

DROP TABLE IF EXISTS proppant_lookup;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE proppant_lookup (
  id int NOT NULL,
  proppant_name text CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  created_at datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  updated_at datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  UNIQUE KEY `PRIMARY` (id) USING HASH,
  KEY id (id) USING CLUSTERED COLUMNSTORE,
  SHARD KEY idx_SHARDKEY (id)
) AUTOSTATS_CARDINALITY_MODE=INCREMENTAL AUTOSTATS_HISTOGRAM_MODE=CREATE AUTOSTATS_SAMPLING=ON SQL_MODE='STRICT_ALL_TABLES';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table pumpdown
--

DROP TABLE IF EXISTS pumpdown;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE pumpdown (
  id bigint NOT NULL AUTO_INCREMENT,
  stage_id int NOT NULL,
  `timestamp` decimal(13,3) Null,
  pressure float DEFAULT NULL,
  rate float DEFAULT NULL,
  total_pumdown_value float DEFAULT NULL,
  created_at datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  updated_at datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  UNIQUE KEY `PRIMARY` (id) USING HASH,
  KEY stage_id (stage_id) USING CLUSTERED COLUMNSTORE,
  SHARD KEY idx_SHARDKEY (id)
) AUTOSTATS_CARDINALITY_MODE=INCREMENTAL AUTOSTATS_HISTOGRAM_MODE=CREATE AUTOSTATS_SAMPLING=ON SQL_MODE='STRICT_ALL_TABLES';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table pumping
--

DROP TABLE IF EXISTS pumping;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE pumping (
  id bigint NOT NULL AUTO_INCREMENT,
  stage_id int NOT NULL,
  `timestamp` decimal(13,3) Null,
  treating_pressure float DEFAULT NULL,
  total_slurry_volume float DEFAULT NULL,
  total_clean_volume float DEFAULT NULL,
  slurry_rate float DEFAULT NULL,
  clean_rate float DEFAULT NULL,
  surface_prop_conc float DEFAULT NULL,
  bottom_prop_conc float DEFAULT NULL,
  bottom_pressure float DEFAULT NULL,
  net_pressure float DEFAULT NULL,
  backside_pressure float DEFAULT NULL,
  friction_reducer float DEFAULT NULL,
  gel float DEFAULT NULL,
  crosslink float DEFAULT NULL,
  additional_column JSON COLLATE utf8_bin,
  created_at datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  updated_at datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  UNIQUE KEY `PRIMARY` (id,stage_id) USING HASH,
  KEY stage_id (stage_id) USING CLUSTERED COLUMNSTORE,
  SHARD KEY idx_SHARDKEY (id,stage_id)
) AUTOSTATS_CARDINALITY_MODE=INCREMENTAL AUTOSTATS_HISTOGRAM_MODE=CREATE AUTOSTATS_SAMPLING=ON SQL_MODE='STRICT_ALL_TABLES';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table quality_control
--

DROP TABLE IF EXISTS quality_control;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE quality_control (
  id bigint NOT NULL AUTO_INCREMENT,
  project_id int NOT NULL,
  is_checked tinyint(1) DEFAULT NULL,
  checked_by text CHARACTER SET utf8 COLLATE utf8_general_ci,
  created_at datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  updated_at datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  UNIQUE KEY `PRIMARY` (id) USING HASH,
  KEY project_id (project_id) USING CLUSTERED COLUMNSTORE,
  SHARD KEY idx_SHARDKEY (id)
) AUTOSTATS_CARDINALITY_MODE=INCREMENTAL AUTOSTATS_HISTOGRAM_MODE=CREATE AUTOSTATS_SAMPLING=ON SQL_MODE='STRICT_ALL_TABLES';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table sensor_20hz_data
--

-- DROP TABLE IF EXISTS sensor_20hz_data;
-- /*!40101 SET @saved_cs_client     = @@character_set_client */;
-- /*!50503 SET character_set_client = utf8mb4 */;
-- CREATE TABLE sensor_20hz_data (
--   id bigint NOT NULL AUTO_INCREMENT,
--   stage_id int NOT NULL,
--   timestamp datetime DEFAULT NULL,
--   ses_data_colllection_id int DEFAULT NULL,
--   ses_pressure_sensor float NOT NULL,
--   ses_hydrophone_sensor_hi float NOT NULL,
--   ses_hydrophone_sensor_low float NOT NULL,
--   ses_pulse_trigger float NOT NULL,
--   ses_wave_pulse_type text CHARACTER SET utf8 COLLATE utf8_general_ci,
--   digital_signal_flag int DEFAULT NULL,
--   other_notes text CHARACTER SET utf8 COLLATE utf8_general_ci,
--   num_reflections int DEFAULT NULL,
--   created_at datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
--   updated_at datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
--   UNIQUE KEY `PRIMARY` (id) USING HASH,
--   KEY stage_id (stage_id) USING CLUSTERED COLUMNSTORE,
--   SHARD KEY idx_SHARDKEY (id)
-- ) AUTOSTATS_CARDINALITY_MODE=INCREMENTAL AUTOSTATS_HISTOGRAM_MODE=CREATE AUTOSTATS_SAMPLING=ON SQL_MODE='STRICT_ALL_TABLES';
-- /*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table sensor_2hz_data
--

-- DROP TABLE IF EXISTS sensor_2hz_data;
-- /*!40101 SET @saved_cs_client     = @@character_set_client */;
-- /*!50503 SET character_set_client = utf8mb4 */;
-- CREATE TABLE sensor_2hz_data (
--   id bigint NOT NULL AUTO_INCREMENT,
--   stage_id int NOT NULL,
--   timestamp datetime DEFAULT NULL,
--   ses_data_colllection_id int DEFAULT NULL,
--   ses_pressure_sensor float NOT NULL,
--   ses_hydrophone_sensor_hi float NOT NULL,
--   ses_hydrophone_sensor_low float NOT NULL,
--   ses_pulse_trigger float NOT NULL,
--   ses_wave_pulse_type text CHARACTER SET utf8 COLLATE utf8_general_ci,
--   digital_signal_flag int DEFAULT NULL,
--   other_notes text CHARACTER SET utf8 COLLATE utf8_general_ci,
--   num_reflections int DEFAULT NULL,
--   created_at datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
--   updated_at datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
--   UNIQUE KEY `PRIMARY` (id) USING HASH,
--   KEY stage_id (stage_id) USING CLUSTERED COLUMNSTORE,
--   SHARD KEY idx_SHARDKEY (id)
-- ) AUTOSTATS_CARDINALITY_MODE=INCREMENTAL AUTOSTATS_HISTOGRAM_MODE=CREATE AUTOSTATS_SAMPLING=ON SQL_MODE='STRICT_ALL_TABLES';
-- /*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table slurry
--

DROP TABLE IF EXISTS slurry;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE slurry (
  id bigint NOT NULL AUTO_INCREMENT,
  stage_id int NOT NULL,
  total_slurry_rate float DEFAULT NULL,
  created_at datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  updated_at datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  UNIQUE KEY `PRIMARY` (id) USING HASH,
  KEY stage_id (stage_id) USING CLUSTERED COLUMNSTORE,
  SHARD KEY idx_SHARDKEY (id)
) AUTOSTATS_CARDINALITY_MODE=INCREMENTAL AUTOSTATS_HISTOGRAM_MODE=CREATE AUTOSTATS_SAMPLING=ON SQL_MODE='STRICT_ALL_TABLES';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table software
--

DROP TABLE IF EXISTS software;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE software (
  id bigint NOT NULL AUTO_INCREMENT,
  project_id int DEFAULT NULL,
  inpute_app_version float DEFAULT NULL,
  processing_version float DEFAULT NULL,
  db_version float DEFAULT NULL,
  mqtt_version float DEFAULT NULL,
  created_at datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  updated_at datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  UNIQUE KEY `PRIMARY` (id) USING HASH,
  KEY project_id (project_id) USING CLUSTERED COLUMNSTORE,
  SHARD KEY idx_SHARDKEY (id)
) AUTOSTATS_CARDINALITY_MODE=INCREMENTAL AUTOSTATS_HISTOGRAM_MODE=CREATE AUTOSTATS_SAMPLING=ON SQL_MODE='STRICT_ALL_TABLES';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table stage
--

DROP TABLE IF EXISTS stage;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE stage (
  id bigint NOT NULL AUTO_INCREMENT,
  stage_uuid char(36) NOT NULL,
   `well_id` integer NOT NULL,
   is_approved tinyint not null default 0,
  `stage_number` integer NOT NULL,
  `number_of_cluster` integer NOT NULL DEFAULT 0,
  `stage_start_time` datetime NULL,
  `stage_end_time` datetime NULL,
  `frac_design` varchar(35) NULL,
designed_acid_vol float ,
  designed_proppant float ,
  `calc_net_pressure_result` float NULL,
  `observed_net_pressure` float NULL,
  `inline_density` float NULL,
  `blender_density` float NULL,
  `calc_bh_density` float NULL,
  `bottomhole_bhp` float NULL,
  `bottomhole_bht` float NULL,
  `frac_model_bhp` float NULL,
  `total_pumpdown_volume` float NULL,
top_perf_Displacement_volume float NULL,
bottom_perf_Displacement_volume float NULL,
  `plug_name` varchar(50) NULL,
  `plug_depth` int NULL,
  `plug_ordinal` integer NULL,
  `plug_type` varchar(35) NULL,
  `plug_depth_unit` varchar(20) NULL,
  `plug_diameter` float NULL,
  `plug_diameter_unit` varchar(10) NULL,
  `plug_manufacturer` varchar(25) NULL,
  `plug_model` integer NULL,
  `plug_displacement_volume` float NULL,
  `poisson_ratio` float NULL,
  `pr_gradient` double NULL,
  `overburden_num` double NULL,
  `pumping_fluid_viscosity` float NULL,
  `pumping_fluid_density` float NULL,
  `pumping_fluid_type` varchar(35) NULL,
  `tectonic_gradient` double NULL,
  `pore_pressure` float NULL,
  `sleeve_name` varchar(100) NULL,
  `sleeve_ordinal` integer NULL,
  `sleeve_top_measured_depth` float NULL,
  `sleeve_bottom_measured_depth` float NULL,
  `sleeve_depth_unit` varchar(20) NULL,
  `sleeve_port_size` float NULL,
  `sleeve_port_size_unit` varchar(20) NULL,
  `sleeve_ball_size` float NULL,
  `sleeve_ball_size_unit` varchar(20) NULL,
  `sleeve_seat_id` integer NULL,
  `sleeve_manufacturer` varchar(100) NULL,
  `sleeve_model` varchar(100) NULL,
  `sleeve_toe_shift_pressure` float NULL,
  `sleeve_toe_burst_pressure` float NULL,
  `is_acid` varchar(55) NULL,
  `diverter_type` varchar(45) NULL,
  `pumped_diverter` varchar(50) NULL,
  `spf` int NULL,
  `designed_max_prop` float NULL,
  `designed_pad_vol` int NULL,
  `designed_total_clean_fluid_vol` int NULL,
  `designed_flush_vol` int NULL,
  `designed_slurry_vol` int NULL,
  `plug_seat_technique` varchar(50) NULL,
  `stage_event` varchar(50) NULL,
  `data_collection` varchar(255) NULL,
  `additional` json NULL,
  `stage_tvd` float NULL,
  created_at datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  updated_at datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  UNIQUE KEY `PRIMARY` (id) USING HASH,
  KEY stage_uuid (stage_uuid) USING CLUSTERED COLUMNSTORE,
  SHARD KEY idx_SHARDKEY (id)
) AUTOSTATS_CARDINALITY_MODE=INCREMENTAL AUTOSTATS_HISTOGRAM_MODE=CREATE AUTOSTATS_SAMPLING=ON SQL_MODE='STRICT_ALL_TABLES';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table stage_avg
--

DROP TABLE IF EXISTS stage_avg;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE stage_avg (
  id bigint NOT NULL AUTO_INCREMENT,
  stage_id int NOT NULL,
  breakdown_pressure float NULL,
  frac_gradient float NULL,
  diverter float NULL,
  acid float NULL,
  open_well_pressure float NULL,
  isip int NULL,
  isip_5min float NULL,
  isip_10min float NULL,
  isip_15min float NULL,
  time_to_max_rate float NULL,
  100_mesh float NULL,
  40_70_mesh float NULL,
  30_50_mesh float NULL,
  20_40_mesh float NULL,
  micro_prop float NULL,
  avg_rate float NULL,
  avg_pressure float NULL,
  max_rate float NULL,
  max_pressure float NULL,
  slickwater_volume float NULL,
  total_slurry int NULL,
  total_clean float NULL,
  friction_reducer float NULL,
  gel float NULL,
  crosslink float NULL,
  opening_well int NULL,
  total_proppant_lbs float NULL,
  flush_volume int NULL,
  max_prop_conc float NULL,
  pad_vol int NULL,
  additional json NULL,
  created_at datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  updated_at datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  UNIQUE KEY `PRIMARY` (id) USING HASH,
  KEY stage_id (stage_id) USING CLUSTERED COLUMNSTORE,
  SHARD KEY idx_SHARDKEY (id)
) AUTOSTATS_CARDINALITY_MODE=INCREMENTAL AUTOSTATS_HISTOGRAM_MODE=CREATE AUTOSTATS_SAMPLING=ON SQL_MODE='STRICT_ALL_TABLES';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table state
--

DROP TABLE IF EXISTS state;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE state (
  id bigint NOT NULL AUTO_INCREMENT,
  value text CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  created_at datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  updated_at datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  UNIQUE KEY `PRIMARY` (id) USING HASH,
  KEY id (id) USING CLUSTERED COLUMNSTORE,
  SHARD KEY idx_SHARDKEY (id)
) AUTOSTATS_CARDINALITY_MODE=INCREMENTAL AUTOSTATS_HISTOGRAM_MODE=CREATE AUTOSTATS_SAMPLING=ON SQL_MODE='STRICT_ALL_TABLES';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table survey_report
--

DROP TABLE IF EXISTS survey_report;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE survey_report (
  id int NOT NULL,
  file_metadata_id int NOT NULL,
  measured_depth float DEFAULT NULL,
  inclination float DEFAULT NULL,
  azimuth float DEFAULT NULL,
  tvd float DEFAULT NULL,
  ns float DEFAULT NULL,
  ew float DEFAULT NULL,
  vs float DEFAULT NULL,
  dls float DEFAULT NULL,
  closure_direction float DEFAULT NULL,
  dogleg_severity float DEFAULT NULL,
  additional JSON COLLATE utf8_bin,
  created_at datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  updated_at datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  UNIQUE KEY `PRIMARY` (id) USING HASH,
  KEY well_id (file_metadata_id) USING CLUSTERED COLUMNSTORE,
  SHARD KEY idx_SHARDKEY (id)
) AUTOSTATS_CARDINALITY_MODE=INCREMENTAL AUTOSTATS_HISTOGRAM_MODE=CREATE AUTOSTATS_SAMPLING=ON SQL_MODE='STRICT_ALL_TABLES';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table treating_pressure
--

DROP TABLE IF EXISTS treating_pressure;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE treating_pressure (
  id bigint NOT NULL AUTO_INCREMENT,
  stage_id int NOT NULL,
  wellhead_pressure float DEFAULT NULL,
  treating_pressure float DEFAULT NULL,
  annulus_pressure float DEFAULT NULL,
  calc_hydrostatic_pressure float DEFAULT NULL,
  calc_bhp float DEFAULT NULL,
  created_at datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  updated_at datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  UNIQUE KEY `PRIMARY` (id) USING HASH,
  KEY stage_id (stage_id) USING CLUSTERED COLUMNSTORE,
  SHARD KEY idx_SHARDKEY (id)
) AUTOSTATS_CARDINALITY_MODE=INCREMENTAL AUTOSTATS_HISTOGRAM_MODE=CREATE AUTOSTATS_SAMPLING=ON SQL_MODE='STRICT_ALL_TABLES';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table well
--

DROP TABLE IF EXISTS well;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE well (
  id bigint NOT NULL AUTO_INCREMENT,
  well_uuid char(36) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  equipment_id  int NOT NULL,
  pad_id int NOT NULL,
  well_name text CHARACTER SET utf8 COLLATE utf8_general_ci,
  well_api text CHARACTER SET utf8 COLLATE utf8_general_ci,
  formation varchar(255),
  num_stages int DEFAULT NULL,
  number_section int DEFAULT NULL,
  total_planned_stage int DEFAULT NULL,
  total_perfs int DEFAULT NULL,
  total_clusters int DEFAULT NULL,
  frac_system text CHARACTER SET utf8 COLLATE utf8_general_ci,
  fluid_system text CHARACTER SET utf8 COLLATE utf8_general_ci,
  well_start_time datetime DEFAULT NULL,
  well_end_time datetime DEFAULT NULL,
  bottom_hole_latitude float DEFAULT NULL,
  bottom_hole_longitude float DEFAULT NULL,
  surface_longitude float DEFAULT NULL,
  surface_latitude float DEFAULT NULL,
  lateral_length float DEFAULT NULL,
  lateral_length_unit text CHARACTER SET utf8 COLLATE utf8_general_ci,
  measured_depth float DEFAULT NULL,
  vertical_depth float DEFAULT NULL,
  vertical_depth_unit text CHARACTER SET utf8 COLLATE utf8_general_ci,
  estimated_surface_vol float DEFAULT NULL,
  estimated_bbls float DEFAULT NULL,
  estimated_gallons float DEFAULT NULL,
  casing_od float DEFAULT NULL,
  casing_wt float DEFAULT NULL,
  casing_id float DEFAULT NULL,
  casing_depth_md float DEFAULT NULL,
  casing_tol float DEFAULT NULL,
  liner1_od float DEFAULT NULL,
  liner1_wt float DEFAULT NULL,
  liner1_id float DEFAULT NULL,
  liner1_depth_md float DEFAULT NULL,
  liner1_tol float DEFAULT NULL,
  liner2_od float DEFAULT NULL,
  liner2_wt float DEFAULT NULL,
  liner2_id float DEFAULT NULL,
  liner2_depth_md float DEFAULT NULL,
  liner2_tol float DEFAULT NULL,
  measured_depth_unit text CHARACTER SET utf8 COLLATE utf8_general_ci,
  created_at datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  updated_at datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  UNIQUE KEY `PRIMARY` (id) USING HASH,
  KEY well_uuid (well_uuid) USING CLUSTERED COLUMNSTORE,
  SHARD KEY idx_SHARDKEY (id)
) AUTOSTATS_CARDINALITY_MODE=INCREMENTAL AUTOSTATS_HISTOGRAM_MODE=CREATE AUTOSTATS_SAMPLING=ON SQL_MODE='STRICT_ALL_TABLES';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table wireline
--

DROP TABLE IF EXISTS wireline;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE wireline (
  id bigint NOT NULL AUTO_INCREMENT,
  stage_id int NOT NULL,
  ccl float DEFAULT NULL,
  current float DEFAULT NULL,
  line_speed float DEFAULT NULL,
  line_tension float DEFAULT NULL,
  trigger_perfs datetime DEFAULT NULL,
  weight float DEFAULT NULL,
  measured_depth float DEFAULT NULL,
  voltage float DEFAULT NULL,
  `timestamp` decimal(13,3) Null,
  elapsed_time datetime DEFAULT NULL,
  additional JSON COLLATE utf8_bin,
  created_at datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  updated_at datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  UNIQUE KEY `PRIMARY` (id) USING HASH,
  KEY stage_id (stage_id) USING CLUSTERED COLUMNSTORE,
  SHARD KEY idx_SHARDKEY (id)
) AUTOSTATS_CARDINALITY_MODE=INCREMENTAL AUTOSTATS_HISTOGRAM_MODE=CREATE AUTOSTATS_SAMPLING=ON SQL_MODE='STRICT_ALL_TABLES';
/*!40101 SET character_set_client = @saved_cs_client */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;



DROP TABLE IF EXISTS result_processed;

CREATE TABLE result_processed (
  id int NOT NULL AUTO_INCREMENT,
  well_id int NOT NULL,
  stage_id int NOT NULL,
  approved_at datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  updated_at datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  UNIQUE KEY `PRIMARY` (id) USING HASH,
  KEY stage_id (stage_id) USING CLUSTERED COLUMNSTORE,
  SHARD KEY idx_SHARDKEY (id)
) AUTOSTATS_CARDINALITY_MODE=INCREMENTAL AUTOSTATS_HISTOGRAM_MODE=CREATE AUTOSTATS_SAMPLING=ON SQL_MODE='STRICT_ALL_TABLES';


DROP TABLE IF EXISTS file_metadata;
CREATE TABLE file_metadata ( 
	id                   int NOT NULL AUTO_INCREMENT,
	well_id              int NOT NULL,
	meta_data_json       json  NOT NULL    ,
  file_name varchar(100),
  file_path varchar(100),
  file_type varchar(35),
  error varchar(255),
  is_active tinyint,
  loaded_by varchar(100),
	created_at datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
	updated_at datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  UNIQUE KEY `PRIMARY` (id) USING HASH,
  KEY well_id (well_id) USING CLUSTERED COLUMNSTORE,
  SHARD KEY idx_SHARDKEY (id)
 ) AUTOSTATS_CARDINALITY_MODE=INCREMENTAL AUTOSTATS_HISTOGRAM_MODE=CREATE AUTOSTATS_SAMPLING=ON SQL_MODE='STRICT_ALL_TABLES';

 
DROP TABLE IF EXISTS active_data;

CREATE TABLE active_data  (
  id int NOT NULL AUTO_INCREMENT,
  stage_id int NOT NULL,
  amplitude int NULL,
  frequency float NULL,
  offset int NULL,
  period tinyint NULL,
  wave_type varchar(50) NULL,
  post_frac_start_time int NULL,
  post_frac_end_time integer NULL,
  pre_frac_start_time int NULL,
  pre_frac_end_time int NULL,
  pre_frac_num_pulse int NULL,
  post_frac_num_pulse int NULL,
  pre_frac_pulse_note varchar(255) NULL,
  post_frac_pulse_note varchar(255) NULL,
  additional_note varchar(255) NULL,
  UNIQUE KEY `PRIMARY` (id) USING HASH,
  KEY stage_id (stage_id) USING CLUSTERED COLUMNSTORE,
  SHARD KEY idx_SHARDKEY (id)
)  AUTOSTATS_CARDINALITY_MODE=INCREMENTAL AUTOSTATS_HISTOGRAM_MODE=CREATE AUTOSTATS_SAMPLING=ON SQL_MODE='STRICT_ALL_TABLES';


DROP TABLE IF EXISTS DaqSensor ;

CREATE TABLE IF NOT EXISTS DaqSensor
(
  Id INT NOT NULL,
  Name VARCHAR(32),  
  UNIQUE KEY `PRIMARY` (id) USING HASH,
  SHARD KEY idx_SHARDKEY (id)
);

DROP TABLE IF EXISTS DaqSample ;

CREATE TABLE IF NOT EXISTS DaqSample
(
  SampleTimeUtc DATETIME(6) NOT NULL,
  SensorId INT NOT NULL,
  Value Float NOT NULL,
  SHARD KEY idx_SHARDKEY (),
  KEY idx_cluster_key (SampleTimeUtc, SensorId) USING CLUSTERED COLUMNSTORE
);
 

DROP TABLE IF EXISTS single_pulse_parameter ;

CREATE TABLE single_pulse_parameter  (
  id bigint UNSIGNED NOT NULL AUTO_INCREMENT,
  stage_id int NOT NULL,
  crew_id int NOT NULL,
  pulse_ordinal int NULL DEFAULT NULL,
  t_trigger DATETIME(6) NULL DEFAULT NULL,
  t_send float NULL DEFAULT NULL,
  t_ref_0 DATETIME(6) NULL DEFAULT NULL,
  t_ref_1 float NULL DEFAULT NULL,
	created_at datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
	updated_at datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
UNIQUE KEY `PRIMARY` (id) USING HASH,
  KEY stage_id (stage_id) USING CLUSTERED COLUMNSTORE,
  SHARD KEY idx_SHARDKEY (id)
)  AUTOSTATS_CARDINALITY_MODE=INCREMENTAL AUTOSTATS_HISTOGRAM_MODE=CREATE AUTOSTATS_SAMPLING=ON SQL_MODE='STRICT_ALL_TABLES';



DROP TABLE IF EXISTS single_pulse_nf_result;

CREATE TABLE single_pulse_nf_result  (
 id bigint UNSIGNED NOT NULL AUTO_INCREMENT,
  stage_id int NOT NULL,
  single_pulse_param_id int NOT NULL,
  crew_id int NOT NULL,
  nf_parameter_set_id int NOT NULL,
  pulse_ordinal int NOT NULL DEFAULT 1,
  inv_ver float NULL DEFAULT NULL,
  reprocessed int NULL DEFAULT NULL,
  reprocessed_t datetime NULL DEFAULT NULL,
  t_0 DATETIME(6) NULL DEFAULT NULL,
  t_end float NULL DEFAULT NULL,
  nfci float NULL DEFAULT NULL,
  w_inch float NULL DEFAULT NULL,
  polarity float NULL DEFAULT NULL,
  fit_error float NULL DEFAULT NULL,
  runtime_s float NULL DEFAULT NULL,
  k_d float NULL DEFAULT NULL,
  q1 float NULL DEFAULT NULL,
  q2 float NULL DEFAULT NULL,
  q3 float NULL DEFAULT NULL,
  c1 float NULL DEFAULT NULL,
  c2 float NULL DEFAULT NULL,
  c3 float NULL DEFAULT NULL,
  tof1 float NULL DEFAULT NULL,
  tof2 float NULL DEFAULT NULL,
  tof3 float NULL DEFAULT NULL,
  ld float NULL DEFAULT NULL,
  ss_change int NULL DEFAULT NULL,
  qc_passed int NULL DEFAULT NULL,
  wco1 float NULL DEFAULT NULL,
  wco2 float NULL,
  additional json NULL,
  processing_note varchar(255) NULL,
	created_at datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
	updated_at datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  UNIQUE KEY `PRIMARY` (id) USING HASH,
  KEY stage_id (stage_id) USING CLUSTERED COLUMNSTORE,
  SHARD KEY idx_SHARDKEY (id)
)  AUTOSTATS_CARDINALITY_MODE=INCREMENTAL AUTOSTATS_HISTOGRAM_MODE=CREATE AUTOSTATS_SAMPLING=ON SQL_MODE='STRICT_ALL_TABLES';



DROP TABLE IF EXISTS ff3_parameter;

CREATE TABLE ff3_parameter  (
 id bigint UNSIGNED NOT NULL AUTO_INCREMENT,
  stage_id int NOT NULL,
  crew_id int NOT NULL,
  daq_sensor_id int NOT NULL,
  ff3_type varchar(10) NOT NULL,
  t_0 DATETIME(6) NULL,
  t_length_s float NULL,
  avg_injection_rate float NULL,
  p_r float NULL,
  e_y float NULL,
  reservoir_press_psiperft float NULL DEFAULT NULL,
  overburden_press float NULL DEFAULT NULL,
  biot_coeff float NULL DEFAULT NULL,
  tectonic_press float NULL DEFAULT NULL,
  nu_lim_var float NULL DEFAULT NULL,
  treatment_fluid_type varchar(25) CHARACTER SET latin1 COLLATE latin1_swedish_ci NULL DEFAULT NULL,
  beta float NULL DEFAULT NULL,
  compressibility_mpa float NULL DEFAULT NULL,
  flags_PDL int NULL DEFAULT NULL,
  flags_stress_shadow int NULL DEFAULT NULL,
  flags_poisson_ver int NULL DEFAULT NULL,
  flags_breaker int NULL DEFAULT NULL,
  ff3_wci1 float NULL DEFAULT NULL,
  ff3_wci2 float NULL DEFAULT NULL,
  additional json NULL,
	created_at datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
	updated_at datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  UNIQUE KEY `PRIMARY` (id) USING HASH,
  KEY stage_id (stage_id) USING CLUSTERED COLUMNSTORE,
  SHARD KEY idx_SHARDKEY (id)
)  AUTOSTATS_CARDINALITY_MODE=INCREMENTAL AUTOSTATS_HISTOGRAM_MODE=CREATE AUTOSTATS_SAMPLING=ON SQL_MODE='STRICT_ALL_TABLES';


DROP TABLE IF EXISTS ff3_result;

CREATE TABLE ff3_result  (
 id bigint UNSIGNED NOT NULL AUTO_INCREMENT,
  stage_id int NOT NULL,
  ff3_parameter_id int NOT NULL,
  crew_id int NOT NULL,
  inv_ver float NULL DEFAULT NULL,
  ff3_reprocessed int NOT NULL DEFAULT 0,
  reprocessed_t datetime NULL DEFAULT NULL,
  t_0 DATETIME(6) NULL DEFAULT NULL,
  t_length_s float NULL DEFAULT NULL,
  ffkw_isip float NULL DEFAULT NULL,
  ffkw_prop float NULL DEFAULT NULL,
  min_stress float NULL DEFAULT NULL,
  ff3_frac_pressure float NULL DEFAULT NULL,
  min_stress_gradient float NULL DEFAULT NULL,
  net_pressure float NULL DEFAULT NULL,
  st_well_potential float NULL DEFAULT NULL,
  st_reservoir_potential float NULL DEFAULT NULL,
  leakoff_par1 float NULL DEFAULT NULL,
  leakoff_par2 float NULL DEFAULT NULL,
  nwb_drop_psi float NULL DEFAULT NULL,
  c_nwb float NULL DEFAULT NULL,
  v_nwb float NULL DEFAULT NULL,
  nwb_compressibility float NULL DEFAULT NULL,
  nwb_length float NULL DEFAULT NULL,
  ff3_wc01 float NULL DEFAULT NULL,
  ff3_wc02 float NULL DEFAULT NULL,
  stress_shadow_psi float NULL DEFAULT NULL,
  res_pressure_psi float NULL DEFAULT NULL,
  ff3_poisson_rat float NULL DEFAULT NULL,
  processing_note varchar(255) NULL,
frac_efficiency float NULL DEFAULT NULL,
H float NULL DEFAULT NULL,
R float NULL DEFAULT NULL,
W0 float NULL DEFAULT NULL,
  shift_psi	float,
  r2	float,
  calc_isip	float,
  l_max	float,
  l_min	float,
  h_max	float,
  h_min	float,
additional json NULL,
created_at datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
updated_at datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
UNIQUE KEY `PRIMARY` (id) USING HASH,
KEY stage_id (stage_id) USING CLUSTERED COLUMNSTORE,
SHARD KEY idx_SHARDKEY (id)
)  AUTOSTATS_CARDINALITY_MODE=INCREMENTAL AUTOSTATS_HISTOGRAM_MODE=CREATE AUTOSTATS_SAMPLING=ON SQL_MODE='STRICT_ALL_TABLES';


DROP TABLE IF EXISTS user ;

CREATE TABLE IF NOT EXISTS user
(
id bigint UNSIGNED NOT NULL AUTO_INCREMENT ,
user_uuid char(36) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
email varchar(150) not null ,
username varchar(50) not null ,
password varchar(255) not null ,
created_at datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP ,
updated_at datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP ,
SHARD KEY idx_SHARDKEY (email),
 KEY idx_cluster_key (id) USING CLUSTERED COLUMNSTORE
);
 

DROP TABLE IF EXISTS project_user ;

CREATE TABLE IF NOT EXISTS project_user
(
id bigint UNSIGNED NOT NULL AUTO_INCREMENT ,
project_id int not null,
user_id int not null,
created_at datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP ,
updated_at datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP ,
SHARD KEY idx_SHARDKEY (id),
 KEY idx_cluster_key (project_id,user_id) USING CLUSTERED COLUMNSTORE
);
 

DROP TABLE IF EXISTS ff3_tvd ;

CREATE TABLE IF NOT EXISTS ff3_tvd
(
id bigint UNSIGNED NOT NULL AUTO_INCREMENT ,
stage_id int not null,
sigt	float,
pres	float,
p_r_calc	float,
latepress	float,
created_at datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP ,
updated_at datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP ,
SHARD KEY idx_SHARDKEY (id),
 KEY idx_cluster_key (stage_id) USING CLUSTERED COLUMNSTORE
);


DROP TABLE IF EXISTS cloud_sync_table_log ;

CREATE TABLE `cloud_sync_table_log` (
  `id` bigint(10) unsigned NOT NULL AUTO_INCREMENT,
  project_UUID char(36) not null, 
  `table_name` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `sync_status` varchar(25) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT 'Succeeded',
  `synch_date` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  SHARD KEY `idx_SHARDKEY` (`id`,project_UUID),
  KEY `idx_cluster_key` (`id`,project_UUID) USING CLUSTERED COLUMNSTORE
) AUTOSTATS_CARDINALITY_MODE=INCREMENTAL AUTOSTATS_HISTOGRAM_MODE=CREATE AUTOSTATS_SAMPLING=ON SQL_MODE='STRICT_ALL_TABLES';


-- Notes
-- frac_design_lookup table removed. value moved into Stage in frac_design field
-- frac_design_lookup table removed. Value stored in stage in plug_name
-- proppant_lookup table removed. Value stored in proppant table in proppant_name
-- plug_depth_unit_lookup removed. Values stored in plug_depth_unit (stage table: renamed plug_depth_unit_id to plug_depth_unit )
-- fluid_type_lookup table removed. Value stored in chem_fluids table in proppant_name