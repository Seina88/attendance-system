from sqlalchemy_utils import UUIDType
import uuid
from datetime import datetime
from ..database import Database
from flask_marshmallow import Marshmallow
from flask_marshmallow.fields import fields


db = Database().sqlAlchemy
ma = Marshmallow()


class UserModel(db.Model):
    __tablename__ = "user"
    id = db.Column(UUIDType(binary=False),
                   primary_key=True, default=uuid.uuid4)
    name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    password = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now)
    updated_at = db.Column(db.DateTime, nullable=False,
                           default=datetime.now, onupdate=datetime.now)

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password


class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = UserModel
        load_instance = True

    created_at = fields.DateTime('%Y-%m-%dT%H:%M:%S')
    updated_at = fields.DateTime('%Y-%m-%dT%H:%M:%S')
