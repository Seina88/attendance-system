from uuid import UUID, uuid4
import random
import string
from datetime import datetime, timedelta


class Session:
    def __init__(self, id: UUID, user_id: UUID, api_token: str = None, expire_at: datetime = None) -> None:
        self.id = id or uuid4()
        self.user_id = user_id
        self.api_token = api_token or self.__create_api_token()
        self.expire_at = expire_at or self.__create_expire_at()

    def __create_api_token(self, length: int = 20) -> str:
        string_set = string.digits + string.ascii_lowercase + string.ascii_uppercase
        return "".join([random.choice(string_set) for _ in range(length)])

    def __create_expire_at(self) -> datetime:
        return datetime.now() + timedelta(minutes=10)
