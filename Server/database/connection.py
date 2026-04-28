from os import getenv
from dotenv import load_dotenv
from pymongo import MongoClient, errors

class DBConnectionHandler:
    def __init__(self):
        self.__DB_INFO = {
            "ip"    : getenv("DATABASE_IP")       or "localhost",
            "port"  : getenv("DATABASE_PORT")     or "27017",
            "user"  : getenv("DATABASE_USER")     or "admin",
            "psswrd": getenv("DATABASE_PASSWORD") or "password",

            "name"       : getenv("DATABASE_NAME")       or "Askee",
            "collection" : getenv("DATABASE_COLLECTION") or "local"
        }

        self.__CONN_STR = "mongodb://{}:{}@{}:{}/?authSource={}".format(
            self.__DB_INFO["user"],
            self.__DB_INFO["psswrd"],
            self.__DB_INFO["ip"],
            self.__DB_INFO["port"],
            self.__DB_INFO["name"]
        )

        self.__client = None
        self.__db_conn = None


    def connect(self):
        print("Starting dabase connection...")

        conn_pswr_lctn = len(f"mongodb://{self.__DB_INFO["user"]}:") # esse print é completamente desnecessario eu so quis fazer pq to no python posso fazer essas coisas idiotas kk
        print("Generated connection string: " +
            self.__CONN_STR[:conn_pswr_lctn] +
            self.__CONN_STR[conn_pswr_lctn+len(self.__DB_INFO["psswrd"]):]
        )

        # Creates connection to database
        self.__client = MongoClient(str(self.__CONN_STR), serverSelectionTimeoutMS=5000)

        # Tests connection
        try:
            self.__client.server_info()
        except (errors.ServerSelectionTimeoutError, errors.OperationFailure) as err:
            print("Connection failed!")
            raise err

        # Gets connection
        self.__db_conn = self.__client[self.__DB_INFO['name']]

        print("Connected to database!")

        return self.__db_conn

if __name__ == "__main__":

    # Test values
    load_dotenv()
    conn_hndlr = DBConnectionHandler()

    conn = conn_hndlr.connect()

    print(conn.get_collection("local"))