class CreateSessionRequest:
    def __init__(self, info: str, password: str) -> None:
        self.info = info
        self.password = password
