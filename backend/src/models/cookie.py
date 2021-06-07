import random
import string


class Cookie:
    def __init__(self, length):
        self.strings = string.digits + string.ascii_lowercase + string.ascii_uppercase
        self.cookie = self.create(length)

    def create(self, length):
        return "".join([random.choice(self.strings) for _ in range(length)])

    def get(self):
        return self.cookie
