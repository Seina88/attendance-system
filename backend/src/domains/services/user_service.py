from domains.models.user import User
from domains.repositories.user_repository import UserRepository


class UserService:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def exists(self, user: User) -> bool:
        users = [
            self.user_repository.find_by_nickname(user.nickname),
            self.user_repository.find_by_email(user.email)
        ]
        return any(users)
