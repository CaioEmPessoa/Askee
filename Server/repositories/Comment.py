from .RegisterBase import RegisterBase

class Comment(RegisterBase):
    def __init__(self):
        super().__init__("Comments")

comment_repository = Comment()
