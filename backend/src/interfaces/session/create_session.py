import os
from datetime import datetime, timedelta
from flask_restful import Resource, reqparse, abort

from container import container

from applications.session.create_session_request import CreateSessionRequest
from applications.session.create_session_response import CreateSessionResponse


from container import container


class CreateSession(Resource):
    def __init__(self) -> None:
        self.session_application_service = container.create_session_application_service()

        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument("info", required=True)
        self.reqparse.add_argument("password", required=True)

        super().__init__()

    def post(self) -> (dict, int, dict):
        args = self.reqparse.parse_args()
        request = CreateSessionRequest(args.info, args.password)

        response = self.session_application_service.create(request)

        if isinstance(response, CreateSessionResponse):
            return response.body(), response.status, response.header()
        else:
            abort(response.status, **response.body())
