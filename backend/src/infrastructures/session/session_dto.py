import uuid
from datetime import datetime, timedelta
from sqlalchemy_utils import UUIDType
from flask_marshmallow import Marshmallow
from flask_marshmallow.fields import fields

from infrastructures.database import db


class SessionDto(db.Model):
    __tablename__ = "sessions"

    id = db.Column(UUIDType(binary=False),
                   primary_key=True, default=uuid.uuid4)
    user_id = db.Column(UUIDType(binary=False),
                        db.ForeignKey("users.id"), nullable=False)
    api_token = db.Column(db.String(255), nullable=False, unique=True)
    expire_at = db.Column(db.DateTime, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now)
    updated_at = db.Column(db.DateTime, nullable=False,
                           default=datetime.now, onupdate=datetime.now)


class SessionSchema(Marshmallow().SQLAlchemyAutoSchema):
    class Meta:
        model = SessionDto
        load_instance = True

    expire_at = fields.DateTime('%Y-%m-%dT%H:%M:%S')
    created_at = fields.DateTime('%Y-%m-%dT%H:%M:%S')
    updated_at = fields.DateTime('%Y-%m-%dT%H:%M:%S')
