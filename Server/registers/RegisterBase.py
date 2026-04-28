from bson.objectid import ObjectId

class RegisterBase():
    def __init__(self, db_coll_name, db_conn):
        self.__collection_name = db_coll_name
        self.__db_connection = db_conn
        self.__collection = self.__db_connection.get_collection(self.__collection_name)

    ## ===== HELPER FUNCTIONS =====
    def __parse_hidden_fields(self, hiddenFields, showId=False):
        result = {}

        if not showId:
            result["_id"] = 0

        for field in hiddenFields:
            result[field] = 0

        return result if result else None  # None means return all fields

    def __parse_field_exists(self, fields: list):
        result = {}

        for field in fields:
            result[field] = {"$exists": True}

        return result

    def __filter_many(self, filters, hiddenFields, showId, raw=False):
        data = self.__collection.find(filters, self.__parse_hidden_fields(hiddenFields, showId))
        response = data if raw else [i for i in data]
        return response

    def __filter_one(self, filters, hiddenFields, showId):
        data = self.__collection.find_one(filters, self.__parse_hidden_fields(hiddenFields, showId))
        return data

    ## ===== INSERT FUNCTIONS =====
    def insert_document(self, document):
        self.__collection.insert_one(document)

    def insert_documents(self, documents):
        self.__collection.insert_many(documents)

    ## ===== QUERY FUNCTIONS =====
    # get all without filters
    def select_all(self, hiddenFields=[], showId=False):
        return self.__filter_many({}, hiddenFields, showId)

    # get by id
    def select_by_id(self, id, hiddenFields=[], showId=True):
        return self.__filter_one({"_id": ObjectId(id)}, hiddenFields, showId)

    # get with filters
    def select_many(self, filters, hiddenFields=[], showId=False):
        return self.__filter_many(filters, hiddenFields, showId)

    # get with filters but only returns ONE
    def select_one(self, filters, hiddenFields=[], showId=False):
        return self.__filter_one(filters, hiddenFields, showId)


    ## ===== APPEND QUERIES =====
    # Não sei se essas funcoes sao taaooo uteis assim mas elas servem bem como
    # referencia caso alguem vá fazer queries mais complexas.
    def select_filter_or(self, filters: list, hiddenFields=[], showId=False):
        response = self.__filter_many({"$or": filters}, hiddenFields, showId)
        return response

    def select_filter_exists(self, fields, hiddenFields=[], showId=False):
        response = self.__filter_many(self.__parse_field_exists(fields), hiddenFields, showId)
        return response