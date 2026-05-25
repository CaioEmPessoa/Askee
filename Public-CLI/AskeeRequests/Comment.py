from .AskeeRequestsBase import AskeeRequestsBase

class CommentRequests(AskeeRequestsBase):
    def __init__(self):
        super().__init__("comments")

    def get_comments_by_post_id(self, post_id):
        response = self.get_request(
            path="/post/" + post_id
        )

        return response