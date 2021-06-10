from flask_restful import Resource, reqparse, abort
from database import database
from domains.models.user import UserSchema
from domains.services.user_service import UserService
from domains.services.session_service import SessionService
from domains.repositories.user_repository import UserRepository
from domains.repositories.session_repository import SessionRepository
from applications.body.response import Response
from applications.body.error import Error
from applications.services.user_application_service import UserApplicationService


class GetUser(Resource):
    def __init__(self):
        self.user_repository = UserRepository(database)
        self.session_repository = SessionRepository(database)
        self.user_service = UserService(self.user_repository)
        self.session_service = SessionService(self.session_repository)
        self.user_application_service = UserApplicationService(
            self.user_service, self.session_service, self.user_repository)

        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument(
            "api_token", location="cookies", required=True)

        super().__init__()

    def get(self, id: str):
        args = self.reqparse.parse_args()

        response = self.user_application_service.get(id, args.api_token)

        if isinstance(response, Response):
            return response.data, response.status, response.headers
        else:
            abort(response.status, **response.jsonify())
