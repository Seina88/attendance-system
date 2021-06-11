from abc import ABC, abstractmethod
from typing import Optional
from uuid import UUID

from domains.user.user import User


class UserRepository(ABC):
    def __init__(self) -> None:
        pass

    @abstractmethod
    def find_by_id(self, id: UUID) -> Optional[User]:
        pass

    @abstractmethod
    def find_by_nickname(self, nickname: str) -> Optional[User]:
        pass

    @abstractmethod
    def find_by_email(self, email: str) -> Optional[User]:
        pass

    @abstractmethod
    def find_by_info(self, info: str) -> Optional[User]:
        pass

    @abstractmethod
    def add(self, user: User) -> None:
        pass

    @abstractmethod
    def update(self, user: User) -> None:
        pass

    @abstractmethod
    def commit(self) -> None:
        pass
