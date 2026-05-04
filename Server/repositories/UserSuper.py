from User import UserRepository

from repositories.RepositoryBase import RepositoryBase

class UserSuperRepository(RepositoryBase):
    def __init__(self):
        super().__init__("Users")

    def new_entry(self, info):
        info["is_super"] = True
        return super().new_entry(info)