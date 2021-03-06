import pytest
from uuid import UUID, uuid4

from domains.user.user import User


@pytest.fixture(scope="class")
def set_fields() -> (UUID, str, str, str, str, str):
    id = uuid4()
    nickname = "nickname"
    first_name = "first_name"
    last_name = "last_name"
    email = "email@example.com"
    password = "password"
    return id, nickname, first_name, last_name, email, password


@pytest.fixture(scope="class")
def update_fields() -> (str, str, str, str, str):
    nickname = "new_nickname"
    first_name = "new_first_name"
    last_name = "new_last_name"
    email = "new_email@example.com"
    password = "new_password"
    return nickname, first_name, last_name, email, password


class TestUser:
    def test_すべての引数を与えた場合に正常にインスタンスが生成される(self, set_fields: tuple) -> None:
        id, nickname, first_name, last_name, email, password = set_fields
        user = User.Builder().id(id).nickname(nickname).first_name(
            first_name).last_name(last_name).email(email).password(password).build()
        assert user.id == id
        assert user.nickname == nickname
        assert user.first_name == first_name
        assert user.last_name == last_name
        assert user.email == email
        assert user.password == password

    def test_idをNoneで与えた場合にUUIDが発行される(self, set_fields: tuple) -> None:
        _, nickname, first_name, last_name, email, password = set_fields
        user = User.Builder().nickname(nickname).first_name(
            first_name).last_name(last_name).email(email).password(password).build()
        assert isinstance(user.id, UUID)

    def test_update関数を実行するとid以外のメンバ変数が更新される(self, set_fields: tuple, update_fields: tuple) -> None:
        id, nickname, first_name, last_name, email, password = set_fields
        user = User.Builder().id(id).nickname(nickname).first_name(
            first_name).last_name(last_name).email(email).password(password).build()

        new_nickname, new_first_name, new_last_name, new_email, new_password = update_fields
        user.update(new_nickname, new_first_name,
                    new_last_name, new_email, new_password)
        assert user.id == id
        assert user.nickname == new_nickname
        assert user.first_name == new_first_name
        assert user.last_name == new_last_name
        assert user.email == new_email
        assert user.password == new_password

    def test_update関数の引数にNoneを指定したメンバ変数は更新されない(self, set_fields: tuple, update_fields: tuple) -> None:
        id, nickname, first_name, last_name, email, password = set_fields
        user = User.Builder().id(id).nickname(nickname).first_name(
            first_name).last_name(last_name).email(email).password(password).build()

        _, new_first_name, new_last_name, new_email, new_password = update_fields
        user.update(None, new_first_name,
                    new_last_name, new_email, new_password)
        assert user.id == id
        assert user.nickname == nickname
        assert user.first_name == new_first_name
        assert user.last_name == new_last_name
        assert user.email == new_email
        assert user.password == new_password
