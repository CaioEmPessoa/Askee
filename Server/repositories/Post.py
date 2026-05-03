import time
from .RepositoryBase import RepositoryBase

class Post(RepositoryBase):
    def __init__(self):
        super().__init__("Posts")

    def new_entry(self, info):
        info['data'] =  time.strftime("%Y-%m-%d %H:%M", time.gmtime())

        return super().new_entry(info)