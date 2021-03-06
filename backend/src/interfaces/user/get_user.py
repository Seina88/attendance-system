from flask_restful import Resource, reqparse, abort

from container import injector

from applications.user.get_user_request import GetUserRequest
from applications.user.get_user_response import GetUserResponse
from applications.user.user_application_service import UserApplicationService


class GetUser(Resource):
    def __init__(self) -> None:
        self.user_application_service = injector.get(UserApplicationService)

        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument(
            "api_token", location="cookies", required=True)

        super().__init__()

    def get(self, id: str) -> (dict, int):
        args = self.reqparse.parse_args()
        request = GetUserRequest(id, args.api_token)

        response = self.user_application_service.get(request)

        if isinstance(response, GetUserResponse):
            return response.body(), response.status
        else:
            abort(response.status, **response.body())
