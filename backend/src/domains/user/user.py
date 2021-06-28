from uuid import UUID, uuid4
from instance_builder import builder


@builder("id", "nickname", "first_name", "last_name", "email", "password")
class User:
    def __init__(self, id: UUID, nickname: str, first_name: str, last_name: str, email: str, password: str) -> None:
        self.id = id or uuid4()
        self.nickname = nickname
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password

    def update(self, nickname: str = None, first_name: str = None, last_name: str = None, email: str = None, password: str = None) -> None:
        self.nickname = nickname or self.nickname
        self.first_name = first_name or self.first_name
        self.last_name = last_name or self.last_name
        self.email = email or self.email
        self.password = password or self.password
