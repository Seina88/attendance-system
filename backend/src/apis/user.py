from flask_restful import Resource, reqparse, abort
from ..database import database
from ..models.user_model import UserSchema
from ..repositories.user_repository import UserRepository
from ..repositories.session_repository import SessionRepository
from ..services.user_service import UserService
from ..services.session_service import SessionService


class User(Resource):
    def __init__(self):
        self.user_repository = UserRepository(database)
        self.session_repository = SessionRepository(database)
        self.user_service = UserService(self.user_repository)
        self.session_service = SessionService(
            self.user_repository, self.session_repository)
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument(
            "Cookie", location="headers", required=True)
        super().__init__()

    def get(self, id):
        args = self.reqparse.parse_args()
        cookie = args["Cookie"]
        if not self.session_service.authenticated(cookie):
            abort(403, **{"message": "権限がありません。"})

        user = self.user_repository.find_by_id(id)

        if user is None:
            abort(404, **{"message": "ユーザーは存在しません。"})

        res = UserSchema().dump(user)
        return res, 200
