from .RegisterBase import RegisterBase

class Post_repository(RegisterBase):
    def __init__(self, db_conn):
        super().__init__("local", db_conn)