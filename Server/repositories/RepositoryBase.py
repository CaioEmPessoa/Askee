import json
import uuid
from os import getcwd

class RepositoryBase():
    def __init__(self, db_register_name):
        self._register_name = db_register_name
        self._register_location = f"{getcwd()}/../Database/{self._register_name}.json"

        self.cache = None
        self._build_cache()

    ## ===== HELPER FUNCTIONS =====
    def _read_file (self):
        result = ''
        with open(self._register_location, "r") as r:
            result = json.load(r)

        return result

    def _write_file(self, info):
        with open(self._register_location, "w") as w:
            json.dump(info, w, indent=4)

        self._build_cache()

    def _write_cache(self):
        converted_values = list(self.cache.values())
        self._write_file(converted_values)

    def _build_cache(self):
        self.cache = {item['id']: item for item in self._read_file()}

    def _gen_id(self):
        # try: new_id = max(self.cache)+1
        # except ValueError: new_id = 1
        # except TypeError: raise Exception(f"{self._register_name} possui um registro inválido!")
        return uuid.uuid4().hex

    def _update_on_id(self, id, info):
        if id not in self.cache:
            return False

        info['id'] = id

        self.cache[id] = info
        self._write_cache()

        return self.cache[id]

    def _append_info(self, info):
        if 'id' in info:
            return False

        new_id = self._gen_id()

        info['id'] = new_id

        self.cache[new_id] = info
        self._write_cache()

        return self.cache[new_id]

    def _delete_on_id(self, id):
        if id not in self.cache or id == None:
            return False

        self.cache.pop(id)
        self._write_cache()

        return True

    ## ===== INSERT FUNCTIONS =====
    def new_entry(self, info):
        return self._append_info(info)

    def update_on_id(self, id, info):
        updt_info = self.cache[id] | info
        return self._update_on_id(id, updt_info)

    def delete_on_id(self, id):
        return self._delete_on_id(id)

    ## ===== QUERY FUNCTIONS =====
    def get_all(self):
        return self.cache

    def get_by_id(self, id):
        return self.cache[id] if id in self.cache else None
