from typing import TypeVar


T = TypeVar("T")


class Container:
    def __init__(self) -> None:
        self.store = {}

    def register(self, key: str, builder: "function") -> None:
        self.store[key] = builder

    def inject(self, key: str) -> T:
        return self.store[key](self)


container = Container()
