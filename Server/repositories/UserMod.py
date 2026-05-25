from User import UserRepository
from repositories.RepositoryBase import RepositoryBase

# Design Pattern: Singleton
# O método __new__ intercepta a alocação do objeto, garantindo que apenas uma única instância da classe seja criada na memória e retornada em todas as chamadas futuras
class UserModRepository(RepositoryBase):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(UserModRepository, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        if not getattr(self, '_initialized', False):
            super().__init__("Users")
            self._initialized = True

    def new_entry(self, info):
        info["is_moderator"] = True
        return super().new_entry(info)
