from app.models.mixin_models import TimestampMixin, ModelMixin
from app import db


class CustomerFieldRep(TimestampMixin, ModelMixin, db.Model):

    __tablename__ = "customer_field_rep"

    id = db.Column(db.BigInteger, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    email = db.Column(db.Text)
    customer_field_rep_num = db.Column(db.Integer)
