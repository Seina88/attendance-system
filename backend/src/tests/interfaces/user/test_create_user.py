import json
from uuid import UUID

from tests.main_test_case import MainTestCase

from infrastructures.user.user_dto import UserDto


class TestCreateUser(MainTestCase):
    def test_ユーザを作成(self) -> None:
        request = {
            "nickname": "nickname",
            "first_name": "first_name",
            "last_name": "last_name",
            "email": "email@example.com",
            "password": "password"
        }
        response = self.client.post(
            "/api/users", data=json.dumps(request), content_type="application/json"
        )
        data = json.loads(response.data)
        self.assert_status(response, 201)
        assert isinstance(UUID(data["id"]), UUID)
        request["id"] = data["id"]
        assert data == request

    def test_必要なパラメータを指定しなかった場合400エラー(self) -> None:
        request = {}
        response = self.client.post(
            "/api/users", data=json.dumps(request), content_type="application/json"
        )
        self.assert_status(response, 400)

    def test_すでに存在するnicknameを指定した場合409エラー(self) -> None:
        user = self.db.session.query(UserDto).first()
        request = {
            "nickname": user.nickname,
            "first_name": "first_name",
            "last_name": "last_name",
            "email": "email@example.com",
            "password": "password"
        }
        response = self.client.post(
            "/api/users", data=json.dumps(request), content_type="application/json"
        )
        data = json.loads(response.data)
        self.assert_status(response, 409)
        assert data["message"] == "そのニックネームはすでに使用されています。"

    def test_すでに存在するemailを指定した場合409エラー(self) -> None:
        user = self.db.session.query(UserDto).first()
        request = {
            "nickname": "nickname",
            "first_name": "first_name",
            "last_name": "last_name",
            "email": user.email,
            "password": "password"
        }
        response = self.client.post(
            "/api/users", data=json.dumps(request), content_type="application/json"
        )
        data = json.loads(response.data)
        self.assert_status(response, 409)
        assert data["message"] == "そのメールアドレスはすでに登録されています。"
