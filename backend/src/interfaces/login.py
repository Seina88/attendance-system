import os
from datetime import datetime, timedelta
from flask_restful import Resource, reqparse, abort
from database import database
from domains.repositories.user_repository import UserRepository
from domains.repositories.session_repository import SessionRepository
from domains.services.login_service import LoginService
from applications.body.response import Response
from applications.body.error import Error
from applications.services.login_application_service import LoginApplicationService


class Login(Resource):
    def __init__(self):
        self.user_repository = UserRepository(database)
        self.session_repository = SessionRepository(database)
        self.login_service = LoginService(self.user_repository)
        self.login_application_service = LoginApplicationService(
            self.session_repository, self.login_service)

        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument("info", required=True)
        self.reqparse.add_argument("password", required=True)

        super().__init__()

    def post(self):
        args = self.reqparse.parse_args()

        response = self.login_application_service.create(
            args.info, args.password)

        if isinstance(response, Response):
            return response.data, response.status, response.headers
        else:
            abort(response.status, **response.jsonify())
