from flask_restful import Resource, reqparse, abort
from database import database
from domains.models.user import User, UserSchema
from domains.services.user_service import UserService
from domains.repositories.user_repository import UserRepository
from applications.body.response import Response
from applications.body.error import Error
from applications.services.user_application_service import UserApplicationService


class CreateUser(Resource):
    def __init__(self):
        self.user_repository = UserRepository(database)
        self.user_service = UserService(self.user_repository)
        self.user_application_service = UserApplicationService(
            self.user_service, None, self.user_repository)

        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument("nickname", required=True)
        self.reqparse.add_argument("first_name", required=True)
        self.reqparse.add_argument("last_name", required=True)
        self.reqparse.add_argument("email", required=True)
        self.reqparse.add_argument("password", required=True)

        super().__init__()

    def post(self):
        args = self.reqparse.parse_args()
        user = User(args.nickname, args.first_name,
                    args.last_name, args.email, args.password)

        response = self.user_application_service.create(user)

        if isinstance(response, Response):
            return response.data, response.status, response.headers
        else:
            abort(response.status, **response.jsonify())
