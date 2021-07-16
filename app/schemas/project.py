from marshmallow import Schema, fields


class JobInfoSchema(Schema):
    job_id = fields.Str()
    job_name = fields.Str()
    job_type = fields.Str()
    afe_id = fields.Str()
    country_name = fields.Str()
    basin_name = fields.Str()
    state = fields.Str()
    job_start_date = fields.DateTime()
    job_end_time = fields.DateTime()


class PadInfoSchema(Schema):
    pad_name = fields.Str()
    pad_uuid = fields.Str()
    client_name = fields.Str()
    customer_field_rep = fields.Str()
    rep_contact_number = fields.Int()
    operator_name = fields.Str()
    service_company_name = fields.Str()
    wireline_company = fields.Str()


class WellInfoSchema(Schema):
    well_name = fields.Str()
    num_stages = fields.Int()
    well_api = fields.Str()
    formation = fields.Str()
    lat = fields.Str()
    easting = fields.Str()
    northing = fields.Str()


class ProjectSchema(Schema):
    name = fields.Str(required=True)
    jobInfoValues = fields.Nested(JobInfoSchema)
    padInfoValues = fields.Nested(PadInfoSchema)
    wellInfoValues = fields.List(fields.Nested(WellInfoSchema))


class ProjectIdPathSchema(Schema):
    project_id = fields.Str(required=True)
