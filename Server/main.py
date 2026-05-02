from dotenv import load_dotenv
from database import connection
from flask import Flask
from registers import blueprints
import json

load_dotenv()

app = Flask(__name__)

for bp in blueprints:
    app.register_blueprint(bp)


if __name__ == '__main__':
    app.run(host='localhost', port=5000)