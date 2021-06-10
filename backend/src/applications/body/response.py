class Response:
    def __init__(self, status: int, data: str, headers: str):
        self.status = status
        self.data = data
        self.headers = headers
