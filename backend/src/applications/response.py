from abc import ABC, abstractmethod


class Response(ABC):
    @abstractmethod
    def body(self) -> dict:
        pass
