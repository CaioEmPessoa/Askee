from ..models.response import Response

class ServicesTamplate:
    def __init__(self, repository):
        self.repository = repository

    def get_one(self, id:int) -> Response():
        return Response()

    def get_all(self) -> Response():
        return Response()

    def new(self, data:dict) -> Response():
        return Response()

    def update(self, id:int, data:dict) -> Response():
        return Response()

    def delete(self, id:int) -> Response():
        return Response()