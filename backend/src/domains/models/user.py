import uuid
from datetime import datetime
from sqlalchemy_utils import UUIDType
from flask_marshmallow import Marshmallow
from flask_marshmallow.fields import fields
from database import database as db
from domains.models.session import Session


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(UUIDType(binary=False),
                   primary_key=True, default=uuid.uuid4)
    nickname = db.Column(db.String(255), nullable=False, unique=True)
    first_name = db.Column(db.String(255), nullable=False)
    last_name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now)
    updated_at = db.Column(db.DateTime, nullable=False,
                           default=datetime.now, onupdate=datetime.now)

    sessions = db.relationship(Session, backref="users", lazy=True)

    def __init__(self, nickname: str, first_name: str, last_name: str, email: str, password: str):
        self.nickname = nickname
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password


class UserSchema(Marshmallow().SQLAlchemyAutoSchema):
    class Meta:
        model = User
        load_instance = True

    created_at = fields.DateTime('%Y-%m-%dT%H:%M:%S')
    updated_at = fields.DateTime('%Y-%m-%dT%H:%M:%S')
