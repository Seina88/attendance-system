class LoginService:
    def __init__(self, user_repository):
        self.user_repository = user_repository

    def find_by_info(self, info):
        return self.user_repository.find_by_nickname(
            info) or self.user_repository.find_by_email(info)
