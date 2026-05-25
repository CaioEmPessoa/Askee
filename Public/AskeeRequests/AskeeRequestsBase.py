
import json
from Requests import Requests

# Design pattern: Adapter
# Atua como um tradutor, convertendo a interface de requisições HTTP em uma interface simplificada que o restante do sistema espera utilizar
class AskeeRequestsBase(Requests):
    def __init__(self, appname):
        super().__init__(appname)

    def get_all(self):
        try: r = self.get_request()
        except: return {"data": None, "statusCode": 500}
        return r.jsonResponse, r.statusCode

    def get_by_id(self, id):
        return self.get_request(id)

    def post_new(self, data):
        return self.post_request(
            body= data
        )

    def delete_id(self, id):
        return self.delete_request(id)
