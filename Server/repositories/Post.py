import time
from .RegisterBase import RegisterBase

class Post(RegisterBase):
    def __init__(self):
        super().__init__("Posts")

    def new_entry(self, info):
        info['data'] =  time.strftime("%Y-%m-%d %H:%M", time.gmtime())

        return self.__append_info(info)