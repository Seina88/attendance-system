import json
from uuid import UUID

from tests.test_case_impl import TestCaseImpl

from infrastructures.database import Database
from infrastructures.user.user_dto import UserDto, UserSchema


def get_user_from_db(db: Database) -> (dict):
    user = db.session.query(UserDto).first()
    expected = UserSchema().dump(user)
    del expected["created_at"], expected["updated_at"]
    return expected


class TestCreateUser(TestCaseImpl):
    def test_nicknameを指定してセッションを生成(self) -> None:
        expected = get_user_from_db(self.db)
        request = {
            "info": expected["nickname"],
            "password": expected["password"]
        }
        response = self.client.post(
            "/api/login", data=json.dumps(request), content_type="application/json"
        )
        data = json.loads(response.data)
        self.assert_status(response, 200)
        assert data == expected
        assert len(response.headers["Set-Cookie"].split("=")[1]) == 20

    def test_emailを指定してセッションを生成(self) -> None:
        expected = get_user_from_db(self.db)
        request = {
            "info": expected["email"],
            "password": expected["password"]
        }
        response = self.client.post(
            "/api/login", data=json.dumps(request), content_type="application/json"
        )
        data = json.loads(response.data)
        self.assert_status(response, 200)
        assert data == expected
        assert len(response.headers["Set-Cookie"].split("=")[1]) == 20

    def test_必要なパラメータを指定しなかった場合400エラー(self) -> None:
        request = {}
        response = self.client.post(
            "/api/login", data=json.dumps(request), content_type="application/json"
        )
        self.assert_status(response, 400)

    def test_指定したnicknameまたはemailが存在しない場合404エラー(self) -> None:
        expected = get_user_from_db(self.db)
        request = {
            "info": "test",
            "password": expected["password"]
        }
        response = self.client.post(
            "/api/login", data=json.dumps(request), content_type="application/json"
        )
        data = json.loads(response.data)
        self.assert_status(response, 404)
        assert data["message"] == "ニックネームまたはメールアドレスが間違っています。"

    def test_パスワードが間違っていた場合401エラー(self) -> None:
        expected = get_user_from_db(self.db)
        request = {
            "info": expected["nickname"],
            "password": "password"
        }
        response = self.client.post(
            "/api/login", data=json.dumps(request), content_type="application/json"
        )
        data = json.loads(response.data)
        self.assert_status(response, 401)
        assert data["message"] == "パスワードが間違っています。"
