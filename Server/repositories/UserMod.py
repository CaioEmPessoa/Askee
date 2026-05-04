
from User import UserRepository

from repositories.RepositoryBase import RepositoryBase

class UserModRepository(RepositoryBase):
    def __init__(self):
        super().__init__("Users")

    def new_entry(self, info):
        info["is_moderator"] = True
        return super().new_entry(info)