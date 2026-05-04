from User import UserRepository
from UserMod import UserModRepository
from UserSuper import UserSuperRepository

class UserFactory:
    def __init__(self):
        self._UserModRepository = UserModRepository()
        self._UserSuperRepository = UserSuperRepository()
        self._UserRepository = UserRepository()

    def new_user(self, info, user_type):
        valid_types = ['mod', 'super', 'regular']
        if user_type not in valid_types:
            raise ValueError(f"Invalid user type: {user_type}. Must be one of {valid_types}")

        result = None
        match user_type:
            case 'mod':
                result = self._UserModRepository.new_entry(info)
            case 'super':
                result = self._UserSuperRepository.new_entry(info)
            case _:
                result = self._UserRepository.new_entry(info)
        return result
