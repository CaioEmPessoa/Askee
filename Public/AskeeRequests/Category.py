from .AskeeRequestsBase import AskeeRequestsBase

class CategoryRequests(AskeeRequestsBase):
    def __init__(self):
        super().__init__("categories")