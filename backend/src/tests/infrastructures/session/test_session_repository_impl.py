from uuid import uuid4, UUID

from tests.test_case_impl import TestCaseImpl

from container import injector

from domains.session.session import Session
from domains.session.session_repository import SessionRepository

from infrastructures.database import Database
from infrastructures.user.user_dto import UserDto
from infrastructures.session.session_dto import SessionDto
from infrastructures.session.session_repository_impl import SessionRepositoryImpl


class TestSessionRepositoryImpl(TestCaseImpl):
    def test_コンストラクタ(self) -> None:
        db = injector.get(Database)
        session_repository = SessionRepositoryImpl(db)
        assert session_repository.db == db


class TestFindByApiToken(TestCaseImpl):
    def test_存在するAPIトークンを指定するとSession型のインスタンスが返される(self) -> None:
        expected = self.db.session.query(SessionDto).first()
        session_repository = injector.get(SessionRepository)
        session = session_repository.find_by_api_token(expected.api_token)
        assert isinstance(session, Session)
        assert session.id == expected.id
        assert session.user_id == expected.user_id
        assert session.api_token == expected.api_token
        assert session.expire_at == expected.expire_at

    def test_存在するAPIトークンを指定するとSession型のインスタンスが返される(self) -> None:
        expected = self.db.session.query(SessionDto).first()
        session_repository = injector.get(SessionRepository)
        session = session_repository.find_by_api_token("api_token")
        assert session is None


class TestAdd(TestCaseImpl):
    def test_セッションを追加(self) -> None:
        prev_count = self.db.session.query(SessionDto).count()
        user = self.db.session.query(UserDto).first()
        session_repository = injector.get(SessionRepository)
        session = Session(None, user.id)
        session_repository.add(session)
        session_repository.commit()
        assert self.db.session.query(SessionDto).count() == prev_count + 1
