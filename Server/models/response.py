class Response:
    def __init__(self, status, message, data=None):
        self.status = status
        self.message = message
        self.data = data

    def build():
        return {
            "status": self.status,
            "message": self.message,
            "data": self.data if self.data is not None else {}
        }