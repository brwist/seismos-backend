from marshmallow import Schema, fields


class JobInfoSchema(Schema):
    job_id = fields.Int(required=True)
    job_name = fields.Str(required=True)
    job_type = fields.Str(required=True)
    afe_id = fields.Int(required=True)
    county_name = fields.Str(required=True)
    basin_name = fields.Str(required=True)
    state = fields.Str(required=True)
    job_start_date = fields.Integer(required=True)
    job_end_date = fields.Integer(required=False)


class PadInfoSchema(Schema):
    pad_name = fields.Str(required=True)
    customer_name = fields.Str(required=True)
    customer_email = fields.Str(required=False)  # customer_field_rep -> name
    rep_contact_number = fields.Int(required=True)
    operator_name = fields.Str(required=True)
    service_company_name = fields.Str(required=True)
    wireline_company = fields.Str(required=True)


class WellInfoSchema(Schema):
    well_name = fields.Str(required=True)
    num_stages = fields.Int(required=True)
    well_api = fields.Str(required=True)
    formation = fields.Str(required=True)
    surface_latitude = fields.Float(required=True)
    surface_longitude = fields.Float(required=True)


class WellVolumeSchema(Schema):
    type = fields.Str(required=True)
    id = fields.Float(required=True)
    od = fields.Float(required=True)
    wt = fields.Float(required=True)
    depth_md = fields.Float(required=True)
    tol = fields.Float(required=True)


class WellVolumeEstimationSchema(Schema):
    surface_vol = fields.Float(required=True)
    bbls = fields.Float(required=True)
    gallons = fields.Float(required=True)


class ClientInfoSchema(Schema):
    clientusername = fields.Str(required=True)
    title = fields.Str(required=True)
    password = fields.Str(required=True)


class CrewInfoSchema(Schema):
    role = fields.Str(required=True)
    name = fields.Str(required=True)
    shift = fields.Str(required=True)


class EquipmentSchema(Schema):
    trailers_id = fields.Int(required=True)
    powerpack_id = fields.Int(required=True)
    source_id = fields.Int(required=True)
    accumulator_id = fields.Int(required=True)
    hydrophones_id = fields.Int(required=True)
    transducer_id = fields.Int(required=True)
    hotspot_id = fields.Int(required=True)


class ProjectDataScehma(Schema):
    project_name = fields.Str(required=True)


class ProjectSchema(Schema):
    projectValues = fields.Nested(ProjectDataScehma)
    jobInfoValues = fields.Nested(JobInfoSchema)
    padInfoValues = fields.Nested(PadInfoSchema)
    wellInfoValues = fields.List(fields.Nested(WellInfoSchema))
    wellVolumeValues = fields.List(fields.List(fields.Nested(WellVolumeSchema)))
    wellVolumeEstimationsValues = fields.List(fields.Nested(WellVolumeEstimationSchema))
    clientInfoValues = fields.List(fields.Nested(ClientInfoSchema))
    crewInfoValues = fields.List(fields.Nested(CrewInfoSchema))
    equipmentValues = fields.List(fields.Nested(EquipmentSchema))


class WellReturnData(Schema):
    uuid = fields.Str(required=True)
    well_name = fields.String(required=True)
    num_stages = fields.Int(required=True)


class ProjectReturnDataSchema(Schema):
    uuid = fields.Str(required=True)
    project_name = fields.Str(required=True)
    wells = fields.List(fields.Nested(WellReturnData))


class ProjectFieldSchema(Schema):
    project = fields.Nested(ProjectReturnDataSchema)
    last_sync_date = fields.Integer(required=True)


class ProjectReturnSchema(Schema):
    status = fields.Integer(required=True)
    message = fields.Str(required=True)
    data = fields.Nested(ProjectFieldSchema)


class ProjectUuidPathSchema(Schema):
    project_uuid = fields.UUID(required=True)


class ProjectResponseDataSchema(Schema):
    uuid = fields.Str(required=True)


class ProjectResponseSchema(Schema):
    project = fields.Nested(ProjectResponseDataSchema)


class CreateProjectSuccessSchema(Schema):
    status = fields.Int(required=True)
    message = fields.Str(required=True)
    data = fields.Nested(ProjectResponseSchema)


class ProjectListItemSchema(Schema):
    uuid = fields.String(required=True)
    project_name = fields.String(required=True)
    job_name = fields.String(required=True)
    job_id = fields.Int(required=True)
    created_date = fields.String(required=True)
    created_by = fields.String(required=True)
    created_time = fields.String(required=True)


class ProjectListSchema(Schema):
    projects = fields.List(fields.Nested(ProjectListItemSchema))
