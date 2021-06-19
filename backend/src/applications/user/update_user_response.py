from applications.response import Response

from domains.user.user import User


class UpdateUserResponse(Response):
    def __init__(self, status: int, user: User) -> None:
        self.status = status
        self.user = user

    def body(self) -> dict:
        return {
            "id": str(self.user.id),
            "nickname": self.user.nickname,
            "first_name": self.user.first_name,
            "last_name": self.user.last_name,
            "email": self.user.email,
            "password": self.user.password
        }
