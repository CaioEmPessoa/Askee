
import json
from .Requests import Requests

class AskeeRequestsBase(Requests):
    def __init__(self, appname):
        super().__init__(appname)

    def get_all(self):
        try: r = self.get_request()
        except: return {"data": None, "statusCode": 500}
        return r.jsonResponse

    def get_by_id(self, id):
        return self.get_request(id)

    def post_new(self, data):
        return self.post_request(
            body= data
        )

    def delete_id(self, id):
        return self.delete_request(id)

    def update(self, id, body):
        self.put_request(
            id,
            body=body
        )