from app.models.mixin_models import TimestampMixin, ModelMixin, uuid_string
from app import db


class Client(TimestampMixin, db.Model, ModelMixin):

    __tablename__ = "client"

    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    client_uuid = db.Column(db.String(36), nullable=False, default=uuid_string)
    client_name = db.Column(db.Text)
    customer_field_rep_id = db.Column(db.Text)
    project_id = db.Column(db.BigInteger, nullable=True)
    operator_name = db.Column(db.Text)
    service_company_name = db.Column(db.Text)
    wireline_company = db.Column(db.Text)
    other_comments = db.Column(db.Text)

    customer_field_rep = db.relationship(
        "CustomerFieldRep",
        foreign_keys=[customer_field_rep_id],
        primaryjoin="CustomerFieldRep.id == Client.customer_field_rep_id",
        cascade="all,delete",
    )
