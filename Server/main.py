from dotenv import load_dotenv
from database import connection
from flask import Flask
from registers import blueprints

app = Flask(__name__)

for bp in blueprints:
    app.register_blueprint(bp)

load_dotenv()

conn = connection.connect()
print(conn.get_collection("local"))

if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)
