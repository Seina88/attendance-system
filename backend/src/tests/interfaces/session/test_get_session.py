import json

from tests.test_case_impl import TestCaseImpl

from infrastructures.database import Database
from infrastructures.user.user_dto import UserDto, UserSchema
from infrastructures.session.session_dto import SessionDto


def get_user_from_db(db: Database) -> (dict, str):
    user = db.session.query(UserDto).first()
    session = db.session.query(
        SessionDto).filter_by(user_id=user.id).first()

    expected = UserSchema().dump(user)
    del expected["created_at"], expected["updated_at"]

    return expected, session.api_token


class TestGetSession(TestCaseImpl):
    def test_セッションを取得(self) -> None:
        expected, api_token = get_user_from_db(self.db)
        self.client.set_cookie("localhost", "api_token", api_token)
        response = self.client.get("/api/session")
        data = json.loads(response.data)
        self.assert_status(response, 200)
        assert data == expected

    def test_api_tokenを付与しなかった場合400エラー(self) -> None:
        expected, _ = get_user_from_db(self.db)
        response = self.client.get("/api/session")
        self.assert_status(response, 400)

    def test_api_tokenが無効の場合404エラー(self) -> None:
        expected, _ = get_user_from_db(self.db)
        self.client.set_cookie("localhost", "api_token", "")
        response = self.client.get("/api/session".format(expected["id"]))
        self.assert_status(response, 404)
        data = json.loads(response.data)
        assert data["message"] == "無効なAPIトークンです。"
