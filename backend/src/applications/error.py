class Error:
    def __init__(self, status: int, message: str) -> None:
        self.status = status
        self.message = message

    def body(self) -> dict:
        return {"message": self.message}
