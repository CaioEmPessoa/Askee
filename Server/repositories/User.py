from repositories.RepositoryBase import RepositoryBase

# Repositório para o domínio de usuários, aqui vai ter metodos uteis check_permissions, etc.
class UserRepository(RepositoryBase):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(UserRepository, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        if not getattr(self, '_initialized', False):
            super().__init__("Users")
            self._initialized = True

    def get_by_email(self, email):
        if not email:
            return None
        for user in self.cache.values():
            if user.get("email") == email:
                return user
        return None

    def get_by_username(self, username):
        if not username:
            return None
        for user in self.cache.values():
            if user.get("username") == username:
                return user
        return None

user_repository = UserRepository()
