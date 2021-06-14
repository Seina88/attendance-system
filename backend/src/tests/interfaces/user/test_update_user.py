import json
from uuid import uuid4

from tests.main_test_case import MainTestCase

from infrastructures.database import Database
from infrastructures.user.user_dto import UserDto, UserSchema
from infrastructures.session.session_dto import SessionDto


def get_user_from_db(db: Database) -> (dict, str):
    user = db.session.query(UserDto).first()
    session = db.session.query(
        SessionDto).filter_by(user_id=user.id).first()

    prev_user = UserSchema().dump(user)
    del prev_user["created_at"], prev_user["updated_at"]

    return prev_user, session.api_token


class TestUpdateUser(MainTestCase):
    def test_すべてのパラメータを指定してユーザ情報を更新(self) -> None:
        prev_user, api_token = get_user_from_db(self.db)
        self.client.set_cookie("localhost", "api_token", api_token)
        request = {
            "nickname": "nickname",
            "first_name": "first_name",
            "last_name": "last_name",
            "email": "email@example.com",
            "password": "password"
        }
        response = self.client.put(
            "/api/users/{}".format(prev_user["id"]), data=json.dumps(request), content_type="application/json"
        )
        data = json.loads(response.data)
        self.assert_status(response, 201)
        expected = request
        expected["id"] = prev_user["id"]
        assert data == expected

    def test_指定しなかったパラメータは更新されない(self) -> None:
        prev_user, api_token = get_user_from_db(self.db)
        self.client.set_cookie("localhost", "api_token", api_token)
        request = {
            "first_name": "first_name",
            "last_name": "last_name",
            "email": "email@example.com",
            "password": "password"
        }
        response = self.client.put(
            "/api/users/{}".format(prev_user["id"]), data=json.dumps(request), content_type="application/json"
        )
        data = json.loads(response.data)
        self.assert_status(response, 201)
        assert data["nickname"] == prev_user["nickname"]

    def test_api_tokenを付与しなかった場合400エラー(self) -> None:
        prev_user, api_token = get_user_from_db(self.db)
        request = {
            "nickname": "nickname",
            "first_name": "first_name",
            "last_name": "last_name",
            "email": "email@example.com",
            "password": "password"
        }
        response = self.client.put(
            "/api/users/{}".format(prev_user["id"]), data=json.dumps(request), content_type="application/json"
        )
        self.assert_status(response, 400)

    def test_api_tokenが無効の場合403エラー(self) -> None:
        prev_user, _ = get_user_from_db(self.db)
        request = {
            "nickname": "nickname",
            "first_name": "first_name",
            "last_name": "last_name",
            "email": "email@example.com",
            "password": "password"
        }
        self.client.set_cookie("localhost", "api_token", "")
        response = self.client.put(
            "/api/users/{}".format(prev_user["id"]), data=json.dumps(request), content_type="application/json"
        )
        self.assert_status(response, 403)
        data = json.loads(response.data)
        assert data["message"] == "権限がありません。"

    def test_他のユーザーのidを指定した場合403エラー(self) -> None:
        _, api_token = get_user_from_db(self.db)
        request = {
            "nickname": "nickname",
            "first_name": "first_name",
            "last_name": "last_name",
            "email": "email@example.com",
            "password": "password"
        }
        self.client.set_cookie("localhost", "api_token", api_token)
        response = self.client.put(
            "/api/users/{}".format(uuid4()), data=json.dumps(request), content_type="application/json"
        )
        self.assert_status(response, 403)
        data = json.loads(response.data)
        assert data["message"] == "ユーザーが一致しません。"

    def test_指定したnicknameがすでに使用されている場合409エラー(self) -> None:
        prev_user, api_token = get_user_from_db(self.db)
        other_user = self.db.session.query(
            UserDto).order_by(UserDto.id.desc()).first()
        request = {
            "nickname": other_user.nickname,
            "first_name": "first_name",
            "last_name": "last_name",
            "email": "email@example.com",
            "password": "password"
        }
        self.client.set_cookie("localhost", "api_token", api_token)
        response = self.client.put(
            "/api/users/{}".format(prev_user["id"]), data=json.dumps(request), content_type="application/json"
        )
        self.assert_status(response, 409)
        data = json.loads(response.data)
        assert data["message"] == "そのニックネームはすでに使用されています。"

    def test_指定したemailがすでに使用されている場合409エラー(self) -> None:
        prev_user, api_token = get_user_from_db(self.db)
        other_user = self.db.session.query(
            UserDto).order_by(UserDto.id.desc()).first()
        request = {
            "nickname": "nickname",
            "first_name": "first_name",
            "last_name": "last_name",
            "email": other_user.email,
            "password": "password"
        }
        self.client.set_cookie("localhost", "api_token", api_token)
        response = self.client.put(
            "/api/users/{}".format(prev_user["id"]), data=json.dumps(request), content_type="application/json"
        )
        self.assert_status(response, 409)
        data = json.loads(response.data)
        assert data["message"] == "そのメールアドレスはすでに登録されています。"
