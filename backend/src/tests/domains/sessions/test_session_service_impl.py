import freezegun

from tests.test_case_impl import TestCaseImpl

from container import injector

from domains.session.session_repository import SessionRepository
from domains.session.session_service import SessionService
from domains.session.session_service_impl import SessionServiceImpl

from infrastructures.session.session_dto import SessionDto


class TestSessionServiceImpl(TestCaseImpl):
    def test_インスタンスの生成(self) -> None:
        session_repository = injector.get(SessionRepository)
        session_service = SessionServiceImpl(session_repository)
        assert session_service.session_repository == session_repository


class TestAuthnticated(TestCaseImpl):
    def test_api_tokenが存在しない場合Falseを返す(self) -> None:
        session_service = injector.get(SessionService)
        assert session_service.authenticated("") is False

    # def test_api_tokenが存在して期限切れの場合Falseを返す(self) -> None:
    #     session = self.db.session.query(SessionDto).first()
    #     session_service = container.create_session_service()
    #     with freezegun.freeze_time("9999-01-01"):
    #         assert session_service.authenticated(session.api_token) is False

    def test_api_tokenが存在して期限切れでない場合Trueを返す(self) -> None:
        session = self.db.session.query(SessionDto).first()
        session_service = injector.get(SessionService)
        assert session_service.authenticated(session.api_token) is True
