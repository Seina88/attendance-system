from flask_restful import Resource, reqparse, abort
from ..database import database
from ..models.user_model import UserModel, UserSchema
from ..services.user_service import UserService
from ..repositories.user_repository import UserRepository


class User(Resource):
    def __init__(self):
        self.service = UserService(UserRepository(database))
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument("nickname", required=True)
        self.reqparse.add_argument("first_name", required=True)
        self.reqparse.add_argument("last_name", required=True)
        self.reqparse.add_argument("email", required=True)
        self.reqparse.add_argument("password", required=True)
        super().__init__()

    def get(self, id):
        user = self.service.get_by_id(id)

        if user is None:
            abort(404, **{"message": "ユーザーは存在しません。"})

        res = UserSchema().dump(user)
        return res, 200
