from uuid import uuid4, UUID

from tests.test_case_impl import TestCaseImpl

from container import container

from domains.user.user import User

from infrastructures.user.user_dto import UserDto
from infrastructures.user.user_repository_impl import UserRepositoryImpl


class TestUserRepositoryImpl(TestCaseImpl):
    def test_コンストラクタ(self) -> None:
        db = container.inject("Database")
        user_repository = UserRepositoryImpl(db)
        assert user_repository.db == db


class TestFindById(TestCaseImpl):
    def test_存在するユーザのIDを指定するとUser型のインスタンスが返される(self) -> None:
        expected = self.db.session.query(UserDto).first()
        user_repository = container.inject("UserRepository")
        user = user_repository.find_by_id(expected.id)
        assert isinstance(user, User)
        assert user.id == expected.id
        assert user.nickname == expected.nickname
        assert user.first_name == expected.first_name
        assert user.last_name == expected.last_name
        assert user.email == expected.email
        assert user.password == expected.password

    def test_存在しないユーザのIDを指定するとNoneが返される(self) -> None:
        user_repository = container.inject("UserRepository")
        user = user_repository.find_by_id(uuid4())
        assert user is None


class TestFindByNickname(TestCaseImpl):
    def test_存在するユーザのnicknameを指定するとUser型のインスタンスが返される(self) -> None:
        expected = self.db.session.query(UserDto).first()
        user_repository = container.inject("UserRepository")
        user = user_repository.find_by_nickname(expected.nickname)
        assert isinstance(user, User)
        assert user.id == expected.id
        assert user.nickname == expected.nickname
        assert user.first_name == expected.first_name
        assert user.last_name == expected.last_name
        assert user.email == expected.email
        assert user.password == expected.password

    def test_存在しないユーザのnicknameを指定するとNoneが返される(self) -> None:
        user_repository = container.inject("UserRepository")
        user = user_repository.find_by_nickname("nickname")
        assert user is None


class TestFindByEmail(TestCaseImpl):
    def test_存在するユーザのemailを指定するとUser型のインスタンスが返される(self) -> None:
        expected = self.db.session.query(UserDto).first()
        user_repository = container.inject("UserRepository")
        user = user_repository.find_by_email(expected.email)
        assert isinstance(user, User)
        assert user.id == expected.id
        assert user.nickname == expected.nickname
        assert user.first_name == expected.first_name
        assert user.last_name == expected.last_name
        assert user.email == expected.email
        assert user.password == expected.password

    def test_存在しないユーザのemailを指定するとNoneが返される(self) -> None:
        user_repository = container.inject("UserRepository")
        user = user_repository.find_by_email("email")
        assert user is None


class TestFindByEmail(TestCaseImpl):
    def test_存在するユーザのemailを指定するとUser型のインスタンスが返される(self) -> None:
        expected = self.db.session.query(UserDto).first()
        user_repository = container.inject("UserRepository")
        user = user_repository.find_by_email(expected.email)
        assert isinstance(user, User)
        assert user.id == expected.id
        assert user.nickname == expected.nickname
        assert user.first_name == expected.first_name
        assert user.last_name == expected.last_name
        assert user.email == expected.email
        assert user.password == expected.password

    def test_存在しないユーザのemailを指定するとNoneが返される(self) -> None:
        user_repository = container.inject("UserRepository")
        user = user_repository.find_by_email("email")
        assert user is None


class TestFindByEmail(TestCaseImpl):
    def test_存在するユーザのemailを指定するとUser型のインスタンスが返される(self) -> None:
        expected = self.db.session.query(UserDto).first()
        user_repository = container.inject("UserRepository")
        user = user_repository.find_by_email(expected.email)
        assert isinstance(user, User)
        assert user.id == expected.id
        assert user.nickname == expected.nickname
        assert user.first_name == expected.first_name
        assert user.last_name == expected.last_name
        assert user.email == expected.email
        assert user.password == expected.password

    def test_存在しないユーザのemailを指定するとNoneが返される(self) -> None:
        user_repository = container.inject("UserRepository")
        user = user_repository.find_by_email("email")
        assert user is None


class TestFindByInfo(TestCaseImpl):
    def test_存在するユーザのnicknameを指定するとUser型のインスタンスが返される(self) -> None:
        expected = self.db.session.query(UserDto).first()
        user_repository = container.inject("UserRepository")
        user = user_repository.find_by_info(expected.nickname)
        assert isinstance(user, User)
        assert user.id == expected.id
        assert user.nickname == expected.nickname
        assert user.first_name == expected.first_name
        assert user.last_name == expected.last_name
        assert user.email == expected.email
        assert user.password == expected.password

    def test_存在するユーザのemailを指定するとUser型のインスタンスが返される(self) -> None:
        expected = self.db.session.query(UserDto).first()
        user_repository = container.inject("UserRepository")
        user = user_repository.find_by_info(expected.email)
        assert isinstance(user, User)
        assert user.id == expected.id
        assert user.nickname == expected.nickname
        assert user.first_name == expected.first_name
        assert user.last_name == expected.last_name
        assert user.email == expected.email
        assert user.password == expected.password

    def test_存在しないユーザのnicknameまたはemailを指定するとNoneが返される(self) -> None:
        user_repository = container.inject("UserRepository")
        user = user_repository.find_by_info("info")
        assert user is None


class TestAdd(TestCaseImpl):
    def test_ユーザを追加(self) -> None:
        prev_count = self.db.session.query(UserDto).count()
        user_repository = container.inject("UserRepository")
        user = User(None, "nickname", "first_name", "last_name",
                    "email@example.com", "password")
        user_repository.add(user)
        user_repository.commit()
        assert self.db.session.query(UserDto).count() == prev_count + 1
