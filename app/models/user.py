from datetime import datetime

from sqlalchemy import func
from sqlalchemy.ext.hybrid import hybrid_property
from werkzeug.security import check_password_hash
from app import db
from .mixin_models import ModelMixin, uuid_string


class User(db.Model, ModelMixin):

    __tablename__ = "user"

    id = db.Column(db.BigInteger, primary_key=True)
    username = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(150), nullable=False)
    password = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now)
    user_uuid = db.Column(db.String(36), default=uuid_string)

    def to_dict(self):
        return {
            "username": self.username,
            "email": self.email,
            "created_at": self.created_at.timestamp(),
        }

    # @password.setter
    # def password(self, password):
    #     self.password = generate_password_hash(password)

    @classmethod
    def authenticate(cls, user_id, password):
        user = cls.query.filter(
            db.or_(
                func.lower(cls.username) == func.lower(user_id),
                func.lower(cls.email) == func.lower(user_id),
            )
        ).first()
        if user is not None and check_password_hash(user.password, password):
            return user

    def __repr__(self):
        return f"<User: {self.username}, {self.email}>"


class UserProjects(db.Model):

    __tablename__ = "project_user"

    id = db.Column(db.BigInteger, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    project_id = db.Column(db.BigInteger, nullable=False)
