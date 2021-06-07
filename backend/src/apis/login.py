import os
from datetime import datetime, timedelta
from flask_restful import Resource, reqparse, abort
from ..database import database
from ..models.user_model import UserSchema
from ..models.session_model import SessionModel
from ..models.cookie import Cookie
from ..repositories.user_repository import UserRepository
from ..repositories.session_repository import SessionRepository
from ..services.login_service import LoginService
from ..services.session_service import SessionService


class Login(Resource):
    def __init__(self):
        self.user_repository = UserRepository(database)
        self.session_repository = SessionRepository(database)
        self.login_service = LoginService(self.user_repository)
        self.session_servive = SessionService(
            self.user_repository, self.session_repository)
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument("info", required=True)
        self.reqparse.add_argument("password", required=True)
        super().__init__()

    def post(self):
        args = self.reqparse.parse_args()
        user = self.login_service.find_by_info(args.info)

        if user is None:
            abort(404, **{"message": "ニックネームまたはメールアドレスが間違っています。"})

        if user.password == args.password:
            cookie = Cookie(20).get()
            session = SessionModel(
                user.id, cookie, expire_at=(datetime.now() + timedelta(minutes=10)))
            self.session_repository.add(session)
            self.session_repository.commit()

            res = {
                "user": UserSchema().dump(user),
                "cookie": cookie
            }
            return res, 200
        else:
            abort(401, **{"message": "パスワードが間違っています。"})
