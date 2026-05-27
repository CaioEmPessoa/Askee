from .AskeeRequestsBase import AskeeRequestsBase

class UsersRequests(AskeeRequestsBase):
    def __init__(self):
        super().__init__("users")