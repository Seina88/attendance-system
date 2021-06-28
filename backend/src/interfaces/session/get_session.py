from flask_restful import Resource, reqparse, abort

from container import injector

from applications.session.get_session_request import GetSessionRequest
from applications.session.get_session_response import GetSessionResponse
from applications.session.session_application_service import SessionApplicationService


class GetSession(Resource):
    def __init__(self) -> None:
        self.session_application_service = injector.get(
            SessionApplicationService)

        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument(
            "api_token", location="cookies", required=True)

        super().__init__()

    def get(self) -> (dict, int):
        args = self.reqparse.parse_args()
        request = GetSessionRequest(args.api_token)

        response = self.session_application_service.get(request)

        if isinstance(response, GetSessionResponse):
            return response.body(), response.status
        else:
            abort(response.status, **response.body())
