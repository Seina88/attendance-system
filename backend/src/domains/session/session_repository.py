from abc import ABC, abstractmethod
from typing import Optional

from domains.session.session import Session


class SessionRepository(ABC):
    @abstractmethod
    def find_by_api_token(self, api_token: str) -> Optional[Session]:
        raise NotImplementedError

    @abstractmethod
    def add(self, session: Session) -> None:
        raise NotImplementedError

    @abstractmethod
    def commit(self) -> None:
        raise NotImplementedError
