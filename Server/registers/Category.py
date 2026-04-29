from flask import Blueprint

category_bp = Blueprint('category', __name__)

@category_bp.route('/categories', methods=['POST'])
def add_category():
    return "funcionando"

@category_bp.route('/categories', methods=['GET'])
def list_categories():
    return "funcionando get categorias"

@category_bp.route('/categories/<id>', methods=['GET'])
def list_category(id):
    return "funcionando get id categorias"

@category_bp.route('/categories/<id>', methods=['PUT'])
def update_category(id):
    return "funcionando put categorias"

@category_bp.route('/categories/<id>', methods=['DELETE'])
def delete_category(id):
    return "funcionando delete categorias"