from datetime import datetime
from flask_marshmallow import Marshmallow
from flask_marshmallow.fields import fields
from ..database import database as db


ma = Marshmallow()


class UserModel(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nickname = db.Column(db.String(255), nullable=False)
    first_name = db.Column(db.String(255), nullable=False)
    last_name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now)
    updated_at = db.Column(db.DateTime, nullable=False,
                           default=datetime.now, onupdate=datetime.now)

    def __init__(self, nickname, first_name, last_name, email, password):
        self.nickname = nickname
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password


class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = UserModel
        load_instance = True

    created_at = fields.DateTime('%Y-%m-%dT%H:%M:%S')
    updated_at = fields.DateTime('%Y-%m-%dT%H:%M:%S')
