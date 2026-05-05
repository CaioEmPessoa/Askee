from flask import Blueprint, jsonify, g, request
from repositories.Category import Category
from services.CategoryService import CategoryService
from middlewares.AuthMiddleware import require_auth

categoryRepository = Category()
category_service = CategoryService(categoryRepository)

category_bp = Blueprint('category', __name__)

@category_bp.route('/categories', methods=['POST'])
def add_category():
    data = request.json
    category = category_service.add_category(data)
    return jsonify(category), category["status"]

@category_bp.route('/categories', methods=['GET'])
def list_categories():
    category = category_service.list_categories()
    return jsonify(category), category["status"]

@category_bp.route('/categories/<id>', methods=['GET'])
def list_category(id):
    category = category_service.list_category(id)
    return jsonify(category), category["status"]

@category_bp.route('/categories/<id>', methods=['PUT'])
def update_category(id):
    data = request.json
    category = category_service.update_category(id, data)
    return jsonify(category), category["status"]

@category_bp.route('/categories/<id>', methods=['DELETE'])
def delete_category(id):
    category = category_service.delete_category(id)
    return jsonify(category), category["status"]
