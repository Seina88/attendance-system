import uuid
from datetime import datetime
from sqlalchemy_utils import UUIDType
from flask_marshmallow import Marshmallow
from flask_marshmallow.fields import fields

from container import container

from domains.user.user import User

from infrastructures.session.session_dto import SessionDto


db = container.inject("Database")


class UserDto(db.Model):
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

    sessions = db.relationship(SessionDto, backref="users", lazy=True)

    def update(self, user: User) -> None:
        self.nickname = user.nickname
        self.first_name = user.first_name
        self.last_name = user.last_name
        self.email = user.email
        self.password = user.password


class UserSchema(Marshmallow().SQLAlchemyAutoSchema):
    class Meta:
        model = UserDto
        load_instance = True

    created_at = fields.DateTime('%Y-%m-%dT%H:%M:%S')
    updated_at = fields.DateTime('%Y-%m-%dT%H:%M:%S')
