from abc import ABC, abstractmethod
from typing import Optional

from domains.session.session import Session


class SessionRepository(ABC):
    def __init__(self) -> None:
        pass

    @abstractmethod
    def find_by_api_token(self, api_token: str) -> Optional[Session]:
        pass

    @abstractmethod
    def add(self, session: Session) -> None:
        pass

    @abstractmethod
    def commit(self) -> None:
        pass
