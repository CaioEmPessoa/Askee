from .Requests import Requests

class UsersRequests(Requests):
    def __init__(self):
        super().__init__("users")