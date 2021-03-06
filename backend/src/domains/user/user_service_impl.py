from uuid import UUID
from injector import inject

from domains.user.user import User
from domains.user.user_repository import UserRepository
from domains.user.user_service import UserService


class UserServiceImpl(UserService):
    @inject
    def __init__(self, user_repository: UserRepository) -> None:
        self.user_repository = user_repository

    def exists_with_nickname(self, nickname: str) -> bool:
        return self.user_repository.find_by_nickname(nickname) is not None

    def exists_with_email(self, email: str) -> bool:
        return self.user_repository.find_by_email(email) is not None

    def can_update_nickname(self, id: UUID, nickname: str) -> bool:
        user = self.user_repository.find_by_nickname(nickname)

        if user is None:
            return True

        return user.id == id

    def can_update_email(self, id: UUID, email: str) -> bool:
        user = self.user_repository.find_by_email(email)

        if user is None:
            return True

        return user.id == id
