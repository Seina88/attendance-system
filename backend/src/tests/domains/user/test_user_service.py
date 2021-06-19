from tests.test_case_impl import TestCaseImpl

from container import injector

from domains.user.user_repository import UserRepository
from domains.user.user_service import UserService

from infrastructures.user.user_dto import UserDto


class TestUserService(TestCaseImpl):
    def test_インスタンスの生成(self) -> None:
        user_repository = injector.get(UserRepository)
        user_service = UserService(user_repository)
        assert user_service.user_repository == user_repository


class TestExistsWithNickname(TestCaseImpl):
    def test_nicknameがすでに存在する場合Trueを返す(self) -> None:
        user = self.db.session.query(UserDto).first()
        user_service = injector.get(UserService)
        exists = user_service.exists_with_nickname(user.nickname)
        assert exists is True

    def test_nicknameが存在しない場合Falseを返す(self) -> None:
        user_service = injector.get(UserService)
        exists = user_service.exists_with_nickname("nickname")
        assert exists is False


class TestExistsWithEmail(TestCaseImpl):
    def test_emailがすでに存在する場合Trueを返す(self) -> None:
        user = self.db.session.query(UserDto).first()
        user_service = injector.get(UserService)
        exists = user_service.exists_with_email(user.email)
        assert exists is True

    def test_nicknameが存在しない場合Falseを返す(self) -> None:
        user_service = injector.get(UserService)
        exists = user_service.exists_with_email("email@example.com")
        assert exists is False


class TestCanUpdateNickname(TestCaseImpl):
    def test_nicknameが存在しない場合Trueを返す(self) -> None:
        user = self.db.session.query(UserDto).first()
        user_service = injector.get(UserService)
        can_update = user_service.can_update_nickname(user.id, "new nickname")
        assert can_update is True

    def test_nicknameがすでに存在してidが一致した場合Trueを返す(self) -> None:
        user = self.db.session.query(UserDto).first()
        other_user = self.db.session.query(
            UserDto).order_by(UserDto.id.desc()).first()
        user_service = injector.get(UserService)
        can_update = user_service.can_update_nickname(user.id, user.nickname)
        assert can_update is True

    def test_nicknameがすでに存在してidが一致しなかった場合Falseを返す(self) -> None:
        user = self.db.session.query(UserDto).first()
        other_user = self.db.session.query(
            UserDto).order_by(UserDto.id.desc()).first()
        user_service = injector.get(UserService)
        can_update = user_service.can_update_nickname(
            user.id, other_user.nickname)
        assert can_update is False


class TestCanUpdateEmail(TestCaseImpl):
    def test_emailが存在しない場合Trueを返す(self) -> None:
        user = self.db.session.query(UserDto).first()
        user_service = injector.get(UserService)
        can_update = user_service.can_update_email(
            user.id, "new_email@example.com")
        assert can_update is True

    def test_emailがすでに存在してidが一致した場合Trueを返す(self) -> None:
        user = self.db.session.query(UserDto).first()
        other_user = self.db.session.query(
            UserDto).order_by(UserDto.id.desc()).first()
        user_service = injector.get(UserService)
        can_update = user_service.can_update_email(user.id, user.email)
        assert can_update is True

    def test_emailがすでに存在してidが一致しなかった場合Falseを返す(self) -> None:
        user = self.db.session.query(UserDto).first()
        other_user = self.db.session.query(
            UserDto).order_by(UserDto.id.desc()).first()
        user_service = injector.get(UserService)
        can_update = user_service.can_update_email(
            user.id, other_user.email)
        assert can_update is False
