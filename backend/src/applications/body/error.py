class Error:
    def __init__(self, status: int, message: str):
        self.status = status
        self.message = message

    def jsonify(self) -> dict:
        return {"message": self.message}
