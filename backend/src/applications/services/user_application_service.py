from typing import Union
from applications.body.response import Response
from applications.body.error import Error
from domains.models.user import User, UserSchema
from domains.services.user_service import UserService
from domains.services.session_service import SessionService
from domains.repositories.user_repository import UserRepository


class UserApplicationService:
    def __init__(self, user_service: UserService, session_service: SessionService, user_repository: UserRepository):
        self.user_service = user_service
        self.session_service = session_service
        self.user_repository = user_repository

    def get(self, id: str, api_token: str) -> Union[Response, Error]:
        if not self.session_service.authenticated(api_token):
            return Error(403, "権限がありません。")

        user = self.user_repository.find_by_id(id)

        if user is None:
            return Error(404, "ユーザーは存在しません。")

        user_dumped = UserSchema().dump(user)
        del user_dumped["created_at"], user_dumped["updated_at"]

        return Response(200, user_dumped, None)

    def create(self, user: User) -> Union[Response, Error]:
        if self.user_service.exists(user):
            return Error(409, "そのユーザーはすでに登録されています。")

        self.user_repository.add(user)
        self.user_repository.commit()

        user_dumped = UserSchema().dump(user)
        del user_dumped["created_at"], user_dumped["updated_at"]

        return Response(201, user_dumped, None)
