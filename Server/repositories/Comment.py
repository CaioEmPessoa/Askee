from .RepositoryBase import RepositoryBase

class Comment(RepositoryBase):
    def __init__(self):
        super().__init__("Comments")

comment_repository = Comment()
