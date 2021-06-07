from flask_restful import Resource, reqparse, abort
from ..database import database
from ..models.user_model import UserModel, UserSchema
from ..repositories.user_repository import UserRepository
from ..repositories.session_repository import SessionRepository
from ..services.user_service import UserService


class UserList(Resource):
    def __init__(self):
        self.user_repository = UserRepository(database)
        self.user_service = UserService(self.user_repository)
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument("nickname", required=True)
        self.reqparse.add_argument("first_name", required=True)
        self.reqparse.add_argument("last_name", required=True)
        self.reqparse.add_argument("email", required=True)
        self.reqparse.add_argument("password", required=True)
        super().__init__()

    def get(self):
        users = self.user_repository.find_all()
        return {"users": UserSchema(many=True).dump(users)}, 200

    def post(self):
        args = self.reqparse.parse_args()
        user = UserModel(args.nickname, args.first_name,
                         args.last_name, args.email, args.password)

        if self.user_service.exists(user):
            abort(409, **{"message": "そのメールアドレスはすでに登録されています。"})

        self.user_repository.add(user)
        self.user_repository.commit()
        res = UserSchema().dump(user)
        return res, 201
