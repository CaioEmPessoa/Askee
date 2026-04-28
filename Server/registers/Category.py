from flask import Blueprint

category_bp = Blueprint('category', __name__)

@category_bp.route('/categories', methods=['POST'])
def add_category():
    return "funcionando"

@category_bp.route('/categories', methods=['GET'])
def list_categories():
    return "funcionando"

@category_bp.route('/categories/<id>', methods=['GET'])
def list_category(id):
    pass

@category_bp.route('/categories/<id>', methods=['PUT'])
def update_category(id):
    pass

@category_bp.route('/categories/<id>', methods=['DELETE'])
def delete_category(id):
    pass