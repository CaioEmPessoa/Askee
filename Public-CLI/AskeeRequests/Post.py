from .AskeeRequestsBase import AskeeRequestsBase

class PostRequests(AskeeRequestsBase):
    def __init__(self):
        super().__init__("posts")


if __name__ == "__main__":
    postRequest = PostRequests()

    print(postRequest.get_all()) # for testing