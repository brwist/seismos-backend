from datetime import datetime

from sqlalchemy import func
from sqlalchemy.ext.hybrid import hybrid_property
from werkzeug.security import generate_password_hash, check_password_hash

from app import db
from .mixin_models import ModelMixin


class User(db.Model, ModelMixin):

    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(60), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now)

    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'created_at': self.created_at.timestamp(),
        }

    @hybrid_property
    def password(self):
        return self.password_hash

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    @classmethod
    def authenticate(cls, user_id, password):
        user = cls.query.filter(
            db.or_(func.lower(cls.username) == func.lower(user_id), func.lower(cls.email) == func.lower(user_id))
        ).first()
        if user is not None and check_password_hash(user.password, password):
            return user

    def __repr__(self):
        return f"<User: {self.username}>"


class UserProjects(db.Model):

    __tablename__ = "user_projects"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    project_id = db.Column(db.Integer, nullable=False)
