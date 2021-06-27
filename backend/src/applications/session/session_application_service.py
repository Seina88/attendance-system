from typing import Union
from uuid import UUID
from injector import inject

from applications.error import Error
from applications.session.get_session_request import GetSessionRequest
from applications.session.get_session_response import GetSessionResponse
from applications.session.create_session_request import CreateSessionRequest
from applications.session.create_session_response import CreateSessionResponse

from domains.session.session import Session
from domains.user.user_repository import UserRepository
from domains.session.session_repository import SessionRepository
from domains.session.session_service import SessionService


class SessionApplicationService:
    @inject
    def __init__(self, user_repository: UserRepository, session_repository: SessionRepository, session_service: SessionService) -> None:
        self.user_repository = user_repository
        self.session_repository = session_repository
        self.session_service = session_service

    def get(self, request: GetSessionRequest) -> Union[GetSessionResponse, Error]:
        if not self.session_service.authenticated(request.api_token):
            return Error(404, "無効なAPIトークンです。")

        session = self.session_repository.find_by_api_token(request.api_token)
        user = self.user_repository.find_by_id(session.user_id)

        return GetSessionResponse(200, user)

    def create(self, request: CreateSessionRequest) -> Union[CreateSessionResponse, Error]:
        user = self.user_repository.find_by_info(request.info)

        if user is None:
            return Error(404, "ニックネームまたはメールアドレスが間違っています。")

        if user.password == request.password:
            session = Session.Builder().user_id(user.id).build()

            self.session_repository.add(session)
            self.session_repository.commit()

            return CreateSessionResponse(200, user, session.api_token)
        else:
            return Error(401, "パスワードが間違っています。")
