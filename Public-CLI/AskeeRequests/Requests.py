import requests
import json

PROTOCOL="http"
IP="localhost"
PORT="5000"

class RequestReturn: # not really that much usefull. Made cause it was fun
    def __init__(self, response=None):
        self.response = response

        self.jsonResponse = self.getJsonResponse()
        self.httpCode = self.getHttpCode()
        self.statusCode = self.getStatusCode()

    def getHttpCode(self):
        return self.response.status_code

    def getStatusCode(self):
        return self.getJsonResponse().get('status')

    def getJsonResponse(self):
        return self.response.json()

class Requests:
    def __init__(self, root=""):
        self.start_path = f"{PROTOCOL}://{IP}:{PORT}/{root}"
        return

    def _build_path(self, path):
        return f"{self.start_path}{"/" if path else ""}{path}"

    def get_request(self, path="", params={}):
        return RequestReturn( requests.get(
            url=self._build_path(path),
            params= params
        ) )

    def post_request(self, path="", params={}, body={}):
        return RequestReturn( requests.post(
            url=self._build_path(path),
            params= params,
            json=body
        ) )

    def delete_request(self, path="", params={}, body={}):
        return RequestReturn( requests.post(
            url=self._build_path(path),
            params= params,
            json=body
        ) )

    def put_request(self, path="", params={}, body={}):
        return RequestReturn( requests.put(
            url=self._build_path(path),
            params= params,
            json=body
        ) )
