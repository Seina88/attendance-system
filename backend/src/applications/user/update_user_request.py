class UpdateUserRequest:
    def __init__(self, api_token: str, id: str, nickname: str, first_name: str, last_name: str, email: str, password: str) -> None:
        self.api_token = api_token
        self.id = id
        self.nickname = nickname
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
