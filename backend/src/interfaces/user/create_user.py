from flask_restful import Resource, reqparse, abort

from container import container

from applications.user.create_user_request import CreateUserRequest
from applications.user.create_user_response import CreateUserResponse
from applications.user.user_application_service import UserApplicationService


class CreateUser(Resource):
    def __init__(self) -> None:
        self.user_application_service = container.create_user_application_service()

        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument("nickname", required=True)
        self.reqparse.add_argument("first_name", required=True)
        self.reqparse.add_argument("last_name", required=True)
        self.reqparse.add_argument("email", required=True)
        self.reqparse.add_argument("password", required=True)

        super().__init__()

    def post(self) -> (dict, int):
        args = self.reqparse.parse_args()
        request = CreateUserRequest(args.nickname, args.first_name,
                                    args.last_name, args.email, args.password)

        response = self.user_application_service.create(request)

        if isinstance(response, CreateUserResponse):
            return response.body(), response.status
        else:
            abort(response.status, **response.body())
