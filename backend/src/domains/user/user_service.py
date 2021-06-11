from uuid import UUID

from domains.user.user import User
from domains.user.user_repository import UserRepository


class UserService:
    def __init__(self, user_repository: UserRepository) -> None:
        self.user_repository = user_repository

    def exists(self, user: User) -> bool:
        users = [
            self.user_repository.find_by_nickname(user.nickname),
            self.user_repository.find_by_email(user.email)
        ]
        return any(users)

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
