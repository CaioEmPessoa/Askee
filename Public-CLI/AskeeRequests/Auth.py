from .Requests import Requests

class AuthRequests(Requests):
    def __init__(self):
        super().__init__("auth")

    def signup(self, body={}):
        return self.post_request(
            path="sign-up",
            body=body
        )

    def login(self, body={}):
        return self.post_request(
            path="sign-in",
            body=body
        )