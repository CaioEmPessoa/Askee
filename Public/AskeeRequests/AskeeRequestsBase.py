
import json
from Requests import Requests

class AskeeRequestsBase(Requests):
    def __init__(self, appname):
        super().__init__(appname)

    def get_all(self):
        r = self.get_request()
        return r.jsonResponse, r.statusCode

    def get_by_id(self, id):
        return self.get_request(id)

    def post_new(self, data):
        return self.post_request(
            body= data
        )

    def delete_id(self, id):
        return self.delete_request(id)