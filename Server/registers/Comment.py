from flask import Blueprint
comment_bp = Blueprint('comment', __name__)

@comment_bp.route('/comments', methods=['POST'])
def new_comments():
    return "Comentario funcionando"

@comment_bp.route('/comments', methods=['GET'])
def list_allComments():
    pass

@comment_bp.route('/comments/<id>', methods=['GET'])
def list_comments(id):
    pass

@comment_bp.route('/comments/<id>', methods=['DELETE'])
def delete_comments():
    pass