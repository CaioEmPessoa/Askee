from .RepositoryBase import RepositoryBase
import time

class Comment(RepositoryBase):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Comment, cls).__new__(cls)

        return cls._instance

    def __init__(self):
        if not hasattr(self, 'initialized'):
            super().__init__("Comments")
            self.initialized = True

    def new_entry(self, info):
        info['data'] = time.strftime("%Y-%m-%d %H:%M", time.gmtime())
        return super().new_entry(info)
