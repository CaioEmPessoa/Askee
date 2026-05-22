from .AskeeRequestsBase import AskeeRequestsBase

class CommentRequests(AskeeRequestsBase):
    def __init__(self):
        super().__init__("comments")