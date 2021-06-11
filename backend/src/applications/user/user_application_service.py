from typing import Union
from uuid import UUID

from applications.error import Error
from applications.user.get_user_request import GetUserRequest
from applications.user.get_user_response import GetUserResponse
from applications.user.create_user_request import CreateUserRequest
from applications.user.create_user_response import CreateUserResponse
from applications.user.update_user_request import UpdateUserRequest
from applications.user.update_user_response import UpdateUserResponse

from domains.user.user import User
from domains.user.user_repository import UserRepository
from domains.session.session_repository import SessionRepository
from domains.user.user_service import UserService
from domains.session.session_service import SessionService


class UserApplicationService:
    def __init__(self, user_repository: UserRepository, session_repository: SessionRepository, user_service: UserService, session_service: SessionService) -> None:
        self.user_repository = user_repository
        self.user_service = user_service
        self.session_repository = session_repository
        self.session_service = session_service

    def get(self, request: GetUserRequest) -> Union[GetUserResponse, Error]:
        if not self.session_service.authenticated(request.api_token):
            return Error(403, "権限がありません。")

        user = self.user_repository.find_by_id(request.id)

        if user is None:
            return Error(404, "ユーザーは存在しません。")

        return GetUserResponse(200, user)

    def create(self, request: CreateUserRequest) -> Union[CreateUserResponse, Error]:
        user = User(None, request.nickname, request.first_name,
                    request.last_name, request.email, request.password)

        if self.user_service.exists(user):
            return Error(409, "そのユーザーはすでに登録されています。")

        self.user_repository.add(user)
        self.user_repository.commit()

        return CreateUserResponse(201, user)

    def update(self, request: UpdateUserRequest) -> Union[UpdateUserResponse, Error]:
        if not self.session_service.authenticated(request.api_token):
            return Error(403, "権限がありません。")

        session = self.session_repository.find_by_api_token(request.api_token)
        user = self.user_repository.find_by_id(session.user_id)

        if str(user.id) != request.id:
            return Error(404, "ユーザーが一致しません。")

        new_user = User(None, request.nickname, request.first_name,
                        request.last_name, request.email, request.password)

        if not self.user_service.can_update_nickname(UUID(request.id), new_user.nickname):
            return Error(409, "そのニックネームはすでに使用されています。")

        if not self.user_service.can_update_email(UUID(request.id), new_user.email):
            return Error(409, "そのメールアドレスはすでに登録されています。")

        user.update(new_user.nickname, new_user.first_name,
                    new_user.last_name, new_user.email, new_user.password)

        self.user_repository.update(user)
        self.user_repository.commit()

        return UpdateUserResponse(201, user)
