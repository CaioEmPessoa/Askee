from User import UserRepository
from repositories.RepositoryBase import RepositoryBase

class UserSuperRepository(RepositoryBase):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(UserSuperRepository, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        if not getattr(self, '_initialized', False):
            super().__init__("Users")
            self._initialized = True

    def new_entry(self, info):
        info["is_super"] = True
        return super().new_entry(info)
