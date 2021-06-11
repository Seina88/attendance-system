from flask_restful import Resource, reqparse, abort
from database import database
from domains.models.user import User, UserSchema
from domains.services.user_service import UserService
from domains.services.session_service import SessionService
from domains.repositories.user_repository import UserRepository
from domains.repositories.session_repository import SessionRepository
from applications.body.response import Response
from applications.body.error import Error
from applications.services.user_application_service import UserApplicationService


class UpdateUser(Resource):
    def __init__(self):
        self.user_repository = UserRepository(database)
        self.session_repository = SessionRepository(database)
        self.user_service = UserService(self.user_repository)
        self.session_service = SessionService(self.session_repository)
        self.user_application_service = UserApplicationService(
            user_service=self.user_service, session_service=self.session_service, user_repository=self.user_repository, session_repository=self.session_repository)

        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument(
            "api_token", location="cookies", required=True)
        self.reqparse.add_argument("nickname", required=True)
        self.reqparse.add_argument("first_name", required=True)
        self.reqparse.add_argument("last_name", required=True)
        self.reqparse.add_argument("email", required=True)
        self.reqparse.add_argument("password", required=True)

        super().__init__()

    def put(self, id: str):
        args = self.reqparse.parse_args()
        new_user = User(args.nickname, args.first_name,
                        args.last_name, args.email, args.password)

        response = self.user_application_service.update(
            args.api_token, new_user)

        if isinstance(response, Response):
            return response.data, response.status, response.headers
        else:
            abort(response.status, **response.jsonify())
