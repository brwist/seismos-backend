from app.models.mixin_models import TimestampMixin, ModelMixin
from app import db


class Client(TimestampMixin, db.Model, ModelMixin):

    __tablename__ = "client"

    id = db.Column(db.Integer, primary_key=True)
    client_uuid = db.Column(db.String(36), nullable=False)
    client_name = db.Column(db.Text)
    customer_field_rep_id = db.Column(db.Integer, nullable=False)
    project_id = db.Column(db.Integer, nullable=False)
    operator_name = db.Column(db.Text)
    service_company_name = db.Column(db.Text)
    wireline_company = db.Column(db.Text)
    other_comments = db.Column(db.String(200))
    password = db.Column(db.String(50))
    title = db.Column(db.String(50))
