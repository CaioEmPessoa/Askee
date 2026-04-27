from os import getenv
from dotenv import load_dotenv
from pymongo import MongoClient, errors

def connect():
    print("Starting dabase connection...")

    DB_INFO = {
        "ip"    : getenv("DATABASE_IP")       or "localhost",
        "port"  : getenv("DATABASE_PORT")     or "27017",
        "user"  : getenv("DATABASE_USER")     or "admin",
        "psswrd": getenv("DATABASE_PASSWORD") or "password",

        "name"       : getenv("DATABASE_NAME")       or "Askee",
        "collection" : getenv("DATABASE_COLLECTION") or "local"
    }

    CONN_STR = f"mongodb://{DB_INFO["user"]}:{DB_INFO["psswrd"]}@{DB_INFO["ip"]}:{DB_INFO["port"]}/?authSource={DB_INFO["name"]}"

    # esse print é completamente desnecessario eu so quis fazer pq to no python posso fazer essas coisas idiotas kk
    conn_pswr_lctn = len(f"mongodb://{DB_INFO["user"]}:")
    print("Generated connection string: " + f"{CONN_STR[:conn_pswr_lctn]}****{CONN_STR[conn_pswr_lctn+len(DB_INFO["psswrd"]):]}")


    # Creates connection to database
    CLIENT = MongoClient(str(CONN_STR), serverSelectionTimeoutMS=5000)

    # Tests connection
    try:
        CLIENT.server_info()
    except (errors.ServerSelectionTimeoutError, errors.OperationFailure) as err:
        print("Connection failed!")
        raise err

    # Gets connection and collection
    DB_CONN = CLIENT[DB_INFO['name']]

    print("Connected to database!")

    return DB_CONN

if __name__ == "__main__":

    # Test values
    load_dotenv()
    conn = connect()
    print(conn.get_collection("local"))