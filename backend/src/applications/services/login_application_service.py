from typing import Union
from applications.body.response import Response
from applications.body.error import Error
from domains.models.user import UserSchema
from domains.models.session import Session
from domains.models.api_token import ApiToken
from domains.services.login_service import LoginService
from domains.repositories.session_repository import SessionRepository


class LoginApplicationService:
    def __init__(self, session_repository: SessionRepository, login_service: LoginService):
        self.session_repository = session_repository
        self.login_service = login_service

    def create(self, info: str, password: str) -> Union[Response, Error]:
        user = self.login_service.find_by_info(info)

        if user is None:
            return Error(404, "ニックネームまたはメールアドレスが間違っています。")

        if user.password == password:
            api_token = ApiToken().get()
            session = Session(user.id, api_token)
            self.session_repository.add(session)
            self.session_repository.commit()

            user_dumped = UserSchema().dump(user)
            del user_dumped["created_at"], user_dumped["updated_at"]

            return Response(200, user_dumped, {"Set-Cookie": "api_token={}".format(api_token)})
        else:
            return Error(401, "パスワードが間違っています。")
