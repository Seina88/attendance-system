from abc import ABC, abstractmethod


class SessionService(ABC):
    @abstractmethod
    def authenticated(self, api_token: str) -> bool:
        raise NotImplementedError
