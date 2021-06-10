import random
import string


class ApiToken:
    def __init__(self, length: int = 20):
        self.strings = string.digits + string.ascii_lowercase + string.ascii_uppercase
        self.value = self.create(length)

    def create(self, length: int) -> str:
        return "".join([random.choice(self.strings) for _ in range(length)])

    def get(self) -> str:
        return self.value
