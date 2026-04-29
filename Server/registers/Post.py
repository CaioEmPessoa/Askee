from .RegisterBase import RegisterBase
from flask import Blueprint

post_bp = Blueprint('post', __name__)

class Post_repository(RegisterBase):
    def __init__(self, db_conn):
        super().__init__("local", db_conn)

@post_bp.route('/post', methods=['POST'])
def new_post():
    return "Teste post"

@post_bp.route('/post', methods=['GET'])
def list_posts():
    return "Teste post GET"

@post_bp.route('/post/<id>', methods=['GET'])
def list_post(id):
    pass

@post_bp.route('/post/<id>', methods=['DELETE'])
def delete_post(id):
    pass
