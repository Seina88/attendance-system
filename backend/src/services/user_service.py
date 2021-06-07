class UserService:
    def __init__(self, user_repository):
        self.user_repository = user_repository

    def exists(self, user):
        users = [
            self.user_repository.find_by_nickname(user.nickname),
            self.user_repository.find_by_email(user.email)
        ]
        return any(users)
