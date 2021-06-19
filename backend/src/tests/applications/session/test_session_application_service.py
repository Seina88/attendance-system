import json
from uuid import UUID

from container import injector

from tests.test_case_impl import TestCaseImpl

from applications.error import Error
from applications.session.session_application_service import SessionApplicationService
from applications.session.create_session_request import CreateSessionRequest
from applications.session.create_session_response import CreateSessionResponse

from domains.user.user_repository import UserRepository
from domains.session.session_repository import SessionRepository

from infrastructures.database import Database
from infrastructures.user.user_dto import UserDto, UserSchema


def get_user_from_db(db: Database) -> dict:
    user = db.session.query(UserDto).first()
    expected = UserSchema().dump(user)
    del expected["created_at"], expected["updated_at"]
    return expected


class TestSessionApplicationService(TestCaseImpl):
    def test_コンストラクタ(self) -> None:
        user_repository = injector.get(UserRepository)
        session_repository = injector.get(SessionRepository)
        session_application_service = SessionApplicationService(
            user_repository, session_repository)
        assert session_application_service.user_repository == user_repository
        assert session_application_service.session_repository == session_repository


class TestCreate(TestCaseImpl):
    def test_nicknameを指定してセッションを生成(self) -> None:
        expected = get_user_from_db(self.db)
        request = CreateSessionRequest(
            expected["nickname"], expected["password"])
        session_application_service = injector.get(SessionApplicationService)
        response = session_application_service.create(request)
        assert isinstance(response, CreateSessionResponse)
        assert response.status == 200
        assert response.body() == expected
        assert len(response.api_token) == 20

    def test_emailを指定してセッションを生成(self) -> None:
        expected = get_user_from_db(self.db)
        request = CreateSessionRequest(
            expected["email"], expected["password"])
        session_application_service = injector.get(SessionApplicationService)
        response = session_application_service.create(request)
        assert isinstance(response, CreateSessionResponse)
        assert response.status == 200
        assert response.body() == expected
        assert len(response.api_token) == 20

    def test_指定したnicknameまたはemailが存在しない場合404エラー(self) -> None:
        expected = get_user_from_db(self.db)
        request = CreateSessionRequest("test", expected["password"])
        session_application_service = injector.get(SessionApplicationService)
        response = session_application_service.create(request)
        assert isinstance(response, Error)
        assert response.status == 404
        assert response.message == "ニックネームまたはメールアドレスが間違っています。"

    def test_パスワードが間違っていた場合401エラー(self) -> None:
        expected = get_user_from_db(self.db)
        request = CreateSessionRequest(expected["email"], "password")
        session_application_service = injector.get(SessionApplicationService)
        response = session_application_service.create(request)
        assert isinstance(response, Error)
        assert response.status == 401
        assert response.message == "パスワードが間違っています。"
