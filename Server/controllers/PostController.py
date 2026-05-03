from flask import Blueprint

post_bp = Blueprint('post', __name__)

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
