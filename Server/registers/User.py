from flask import Blueprint

user_bp = Blueprint('user', __name__)

@user_bp.route('/users', methods=['POST'])
def new_user():
    return "Funcionando POST user"

@user_bp.route('/users', methods=['GET'])
def list_users():
    return "Funcionando GET user"

@user_bp.route('/users/<id>', methods=['GET'])
def list_user(id):
    return "Funcionando GET ID user"

@user_bp.route('/users/<id>', methods=['PUT'])
def update_user(id):
    pass

@user_bp.route('/users/<id>', methods=['DELETE'])
def delete_user(id):
    pass