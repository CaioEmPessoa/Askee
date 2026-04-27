from dotenv import load_dotenv
from database import connection

load_dotenv()

conn = connection.connect()
print(conn.get_collection("local"))