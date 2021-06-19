from abc import ABC, abstractmethod
from uuid import UUID

from domains.user.user import User
from domains.user.user_repository import UserRepository


class UserService(ABC):
    @abstractmethod
    def exists_with_nickname(self, nickname: str) -> bool:
        raise NotImplementedError

    @abstractmethod
    def exists_with_email(self, email: str) -> bool:
        raise NotImplementedError

    @abstractmethod
    def can_update_nickname(self, id: UUID, nickname: str) -> bool:
        raise NotImplementedError

    @abstractmethod
    def can_update_email(self, id: UUID, email: str) -> bool:
        raise NotImplementedError
