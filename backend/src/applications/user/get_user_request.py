class GetUserRequest:
    def __init__(self, id: str, api_token: str) -> None:
        self.id = id
        self.api_token = api_token
