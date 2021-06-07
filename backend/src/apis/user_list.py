from flask_restful import Resource, reqparse, abort
from ..database import database
from ..models.user_model import UserModel, UserSchema
from ..repositories.user_repository import UserRepository
from ..repositories.session_repository import SessionRepository
from ..services.user_service import UserService
from ..services.session_service import SessionService


class UserList(Resource):
    def __init__(self):
        self.user_repository = UserRepository(database)
        self.session_repository = SessionRepository(database)
        self.user_service = UserService(self.user_repository)
        self.session_service = SessionService(
            self.user_repository, self.session_repository)
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument("Cookie", location="headers")
        self.reqparse.add_argument("nickname")
        self.reqparse.add_argument("first_name")
        self.reqparse.add_argument("last_name")
        self.reqparse.add_argument("email")
        self.reqparse.add_argument("password")
        super().__init__()

    def get(self):
        args = self.reqparse.parse_args()
        cookie = args["Cookie"]
        if not self.session_service.authenticated(cookie):
            abort(403, **{"message": "権限がありません。"})

        users = self.user_repository.find_all()
        res = {"users": UserSchema(many=True).dump(users)}
        return res, 200

    def post(self):
        args = self.reqparse.parse_args()
        user = UserModel(args.nickname, args.first_name,
                         args.last_name, args.email, args.password)

        if self.user_service.exists(user):
            abort(409, **{"message": "そのユーザーはすでに登録されています。"})

        self.user_repository.add(user)
        self.user_repository.commit()
        res = UserSchema().dump(user)
        return res, 201
