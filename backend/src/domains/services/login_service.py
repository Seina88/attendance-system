from domains.repositories.user_repository import UserRepository


class LoginService:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def find_by_info(self, info: str) -> dict:
        return self.user_repository.find_by_nickname(
            info) or self.user_repository.find_by_email(info)
