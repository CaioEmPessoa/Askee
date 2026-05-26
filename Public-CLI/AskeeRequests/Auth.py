from .Requests import Requests

class AuthRequests(Requests):
    def __init__(self):
        super().__init__("auth")

    def signin(self, body={}):
        return self.post_request(
            path="sign-in",
            body=body
        )

    def login(self, body={}):
        return self.post_request(
            path="sign-in",
            body=body
        )