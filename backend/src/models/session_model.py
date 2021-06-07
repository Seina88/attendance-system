from datetime import datetime
from flask_marshmallow import Marshmallow
from flask_marshmallow.fields import fields
from ..database import database as db


ma = Marshmallow()


class SessionModel(db.Model):
    __tablename__ = "sessions"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    cookie = db.Column(db.String(255), nullable=False, unique=True)
    expire_at = db.Column(db.DateTime)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now)
    updated_at = db.Column(db.DateTime, nullable=False,
                           default=datetime.now, onupdate=datetime.now)

    def __init__(self, user_id, cookie, expire_at=None):
        self.user_id = user_id
        self.cookie = cookie
        self.expire_at = expire_at


class SessionSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = SessionModel
        load_instance = True

    expire_at = fields.DateTime('%Y-%m-%dT%H:%M:%S')
    created_at = fields.DateTime('%Y-%m-%dT%H:%M:%S')
    updated_at = fields.DateTime('%Y-%m-%dT%H:%M:%S')
