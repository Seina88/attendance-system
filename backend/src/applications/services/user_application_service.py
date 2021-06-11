from typing import Union
from applications.body.response import Response
from applications.body.error import Error
from domains.models.user import User, UserSchema
from domains.services.user_service import UserService
from domains.services.session_service import SessionService
from domains.repositories.user_repository import UserRepository
from domains.repositories.session_repository import SessionRepository


class UserApplicationService:
    def __init__(self, user_service: UserService = None, session_service: SessionService = None, user_repository: UserRepository = None, session_repository: SessionRepository = None):
        self.user_service = user_service
        self.session_service = session_service
        self.user_repository = user_repository
        self.session_repository = session_repository

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

    def update(self, api_token: str, new_user: User) -> Union[Response, Error]:
        if not self.session_service.authenticated(api_token):
            return Error(403, "権限がありません。")

        if self.user_service.exists(new_user):
            return Error(409, "そのユーザーはすでに登録されています。")

        session = self.session_repository.find_by_api_token(api_token)

        user = self.user_repository.find_by_id(session.user_id)

        if user is None:
            return Error(404, "ユーザーは存在しません。")

        user.update(new_user.nickname, new_user.first_name,
                    new_user.last_name, new_user.email, new_user.password)

        self.user_repository.add(user)
        self.user_repository.commit()

        user_dumped = UserSchema().dump(user)
        del user_dumped["created_at"], user_dumped["updated_at"]

        return Response(201, user_dumped, None)
