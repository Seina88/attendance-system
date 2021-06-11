from applications.response import Response

from domains.user.user import User


class CreateSessionResponse(Response):
    def __init__(self, status: int, user: User, api_token: str) -> None:
        self.status = status
        self.user = user
        self.api_token = api_token

    def body(self) -> dict:
        return {
            "id": str(self.user.id),
            "nickname": self.user.nickname,
            "first_name": self.user.first_name,
            "last_name": self.user.last_name,
            "email": self.user.email,
            "password": self.user.password
        }

    def header(self) -> dict:
        return {"Set-Cookie": "api_token={}".format(self.api_token)}
