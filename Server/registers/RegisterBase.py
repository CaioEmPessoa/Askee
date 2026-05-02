import json
import uuid
from os import getcwd

class RegisterBase():
    def __init__(self, db_register_name):
        self.__register_name = db_register_name
        self.__register_location = f"{getcwd()}/Database/{self.__register_name}.json"

        self.cache = None
        self.__build_cache()

    ## ===== HELPER FUNCTIONS =====
    def __read_file (self):
        result = ''
        with open(self.__register_location, "r") as r:
            result = json.load(r)

        return result

    def __write_file(self, info):
        with open(self.__register_location, "w") as w:
            json.dump(info, w, indent=4)

        self.__build_cache()

    def __write_cache(self):
        converted_values = list(self.cache.values())
        self.__write_file(converted_values)

    def __build_cache(self):
        self.cache = {item['id']: item for item in self.__read_file()}

    def __gen_id(self):
        # try: new_id = max(self.cache)+1
        # except ValueError: new_id = 1
        # except TypeError: raise Exception(f"{self.__register_name} possui um registro inválido!")
        return uuid.uuid4().hex

    def __update_on_id(self, id, info):
        if id not in self.cache:
            return False

        info['id'] = id

        self.cache[id] = info
        self.__write_cache()

        return self.cache[id]

    def __append_info(self, info):
        if 'id' in info:
            return False

        new_id = self.__gen_id()

        info['id'] = new_id

        self.cache[new_id] = info
        self.__write_cache()

        return self.cache[new_id]

    def __delete_on_id(self, id):
        if id not in self.cache or id == None:
            return False

        self.cache.pop(id)
        self.__write_cache()

        return True

    ## ===== INSERT FUNCTIONS =====
    def new_entry(self, info):
        return self.__append_info(info)

    def update_on_id(self, id, info):
        updt_info = self.cache[id] | info
        return self.__update_on_id(id, updt_info)

    def delete_on_id(self, id):
        return self.__delete_on_id(id)

    ## ===== QUERY FUNCTIONS =====
    def get_all(self):
        return self.cache

    def get_by_id(self, id):
        return self.cache[id] if id in self.cache else None