from flask_restful import Resource, reqparse, abort

from container import container

from applications.user.update_user_request import UpdateUserRequest
from applications.user.update_user_response import UpdateUserResponse


class UpdateUser(Resource):
    def __init__(self) -> None:
        self.user_application_service = container.create_user_application_service()

        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument(
            "api_token", location="cookies", required=True)
        self.reqparse.add_argument("nickname")
        self.reqparse.add_argument("first_name")
        self.reqparse.add_argument("last_name")
        self.reqparse.add_argument("email")
        self.reqparse.add_argument("password")

        super().__init__()

    def put(self, id: str) -> (dict, int):
        args = self.reqparse.parse_args()
        request = UpdateUserRequest(args.api_token, id, args.nickname,
                                    args.first_name, args.last_name, args.email, args.password)

        response = self.user_application_service.update(request)

        if isinstance(response, UpdateUserResponse):
            return response.body(), response.status
        else:
            abort(response.status, **response.body())
