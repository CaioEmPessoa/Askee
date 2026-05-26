from .AskeeRequestsBase import AskeeRequestsBase

class PostRequests(AskeeRequestsBase):
    def __init__(self):
        super().__init__("posts")

    def get_posts_by_category_id(self, category_id):
        response = self.get_request(
            path="/category/" + category_id
        )

        return response


if __name__ == "__main__":
    postRequest = PostRequests()

    print(postRequest.get_all()) # for testing