class CreateUserRequest:
    def __init__(self, nickname: str, first_name: str, last_name: str, email: str, password: str) -> None:
        self.nickname = nickname
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
