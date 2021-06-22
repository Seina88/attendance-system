from typing import Callable


def builder(*attributes: list) -> Callable[type, type]:
    def decorator(Class: type) -> type:
        class Builder:
            def __init__(self) -> None:
                self.kwargs = {}
                for attribute in attributes:
                    self.kwargs[attribute] = None
                    setattr(self, attribute, self.generate_setter(attribute))

            def generate_setter(self, key: str) -> Callable[str, "Builder"]:
                def set_value(value: str) -> "Builder":
                    self.kwargs[key] = value
                    return self
                return set_value

            def build(self) -> Class:
                return Class(**self.kwargs)

        Class.Builder = Builder

        return Class
    return decorator
