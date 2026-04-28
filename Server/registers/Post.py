from .RegisterBase import RegisterBase
from main import app

class Post_repository(RegisterBase):
    def __init__(self, db_conn):
        super().__init__("local", db_conn)

@app.route('/post', methods=['POST'])
def new_post():
    pass

@app.route('/post', methods=['GET'])
def list_posts(id):
    pass

@app.route('/post/<id>', methods=['GET'])
def list_post(id):
    pass

@app.route('/post/<id>', methods=['DELETE'])
def delete_post(id):
    pass
