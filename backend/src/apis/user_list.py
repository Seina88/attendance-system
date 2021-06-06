from flask_restful import Resource, reqparse, abort
from ..database import database
from ..models.user_model import UserModel, UserSchema
from ..services.user_service import UserService
from ..repositories.user_repository import UserRepository


class UserList(Resource):
    def __init__(self):
        self.service = UserService(UserRepository(database))
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument("nickname", required=True)
        self.reqparse.add_argument("first_name", required=True)
        self.reqparse.add_argument("last_name", required=True)
        self.reqparse.add_argument("email", required=True)
        self.reqparse.add_argument("password", required=True)
        super().__init__()

    def get(self):
        users = self.service.get_all()
        return {"users": UserSchema(many=True).dump(users)}

    def post(self):
        args = self.reqparse.parse_args()
        user = UserModel(args.nickname, args.first_name,
                         args.last_name, args.email, args.password)

        if self.service.exists(user):
            abort(409, **{"message": "そのメールアドレスはすでに登録されています。"})

        self.service.add(user)
        res = UserSchema().dump(user)
        return res, 201
