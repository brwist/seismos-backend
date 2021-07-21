from marshmallow import Schema, fields


class JobInfoSchema(Schema):
    job_id = fields.Str()  # TODO Job id ambiguity
    job_name = fields.Str()
    job_type = fields.Str()
    afe_id = fields.Str()
    country_name = fields.Str()
    basin_name = fields.Str()
    state = fields.Str()
    job_start_date = fields.Integer()
    job_end_date = fields.Integer()


class PadInfoSchema(Schema):
    pad_name = fields.Str()
    pad_uuid = fields.Str()
    client_name = fields.Str()
    customer_field_rep = fields.Str()  # customer_field_rep -> name
    rep_contact_number = fields.Int()
    operator_name = fields.Str()
    service_company_name = fields.Str()
    wireline_company = fields.Str()


class WellInfoSchema(Schema):
    well_name = fields.Str()
    num_stages = fields.Int()
    well_api = fields.Str()
    #  ambiguity fields
    formation = fields.Str()
    lat = fields.Str()
    easting = fields.Str()
    northing = fields.Str()


class WellVolumeSchema(Schema):
    id = fields.Str()
    type = fields.Str()
    od = fields.Float()
    wt = fields.Float()
    depth_md = fields.Float()
    tol = fields.Str()  # ambiguity


class WellVolumeEstimationSchema(Schema):
    surface_vol = fields.Float()
    bbls = fields.Float()
    gallons = fields.Float()


class ClientInfoSchema(Schema):
    clientusername = fields.Str()
    title = fields.Str()
    password = fields.Str()


class CrewInfoSchema(Schema):
    role = fields.Str()
    name = fields.Str()
    phone_number = fields.Str()


class EquipmentSchema(Schema):
    trailers_id = fields.Int()
    powerpack_id = fields.Int()
    source_id = fields.Int()
    accumulator_id = fields.Int()
    hydrophones_id = fields.Int()
    transducer_id = fields.Int()
    hotspot_id = fields.Int()


class ProjectDataScehma(Schema):
    project_name = fields.Str()


class ProjectSchema(Schema):
    projectValues = fields.Nested(ProjectDataScehma)
    jobInfoValues = fields.Nested(JobInfoSchema)
    padInfoValues = fields.Nested(PadInfoSchema)
    wellInfoValues = fields.List(fields.Nested(WellInfoSchema))
    wellVolumeValues = fields.List(fields.List(fields.Nested(WellVolumeSchema)))
    wellVolumeEstimationsValues = fields.List(fields.Nested(WellVolumeEstimationSchema))
    clientInfoValues = fields.List(fields.Nested(ClientInfoSchema))
    crewInfoValues = fields.List(fields.Nested(CrewInfoSchema))
    equipmentValues = fields.Nested(EquipmentSchema)


class ProjectIdPathSchema(Schema):
    project_id = fields.Str(required=True)


class ProjectResponseDataSchema(Schema):
    id = fields.Int()


class ProjectResponseSchema(Schema):
    project = fields.Nested(ProjectResponseDataSchema)


class CreateProjectSuccessSchema(Schema):
    status = fields.Int(required=True)
    message = fields.Str(required=True)
    data = fields.Nested(ProjectResponseSchema)
