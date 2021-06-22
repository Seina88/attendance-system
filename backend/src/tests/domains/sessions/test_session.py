import pytest
from uuid import UUID, uuid4
from datetime import datetime

from domains.session.session import Session


class TestSession:
    def test_user_idを与えた場合に正常にインスタンスが生成される(self) -> None:
        user_id = uuid4()
        session = Session.Builder().user_id(user_id).build()

        assert session.user_id == user_id
        assert isinstance(session.id, UUID)
        assert isinstance(session.api_token, str)
        assert len(session.api_token) == 20
        assert isinstance(session.expire_at, datetime)
