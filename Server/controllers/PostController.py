from flask import Blueprint, request, jsonify, g
from services.PostService import PostService
from middlewares.AuthMiddleware import require_auth
from repositories.Post import post_repository
#instaciar o repository
post_service = PostService(post_repository)
post_bp = Blueprint('post', __name__)

@post_bp.route('/post', methods=['POST'])
@require_auth
def new_post():
    data = request.json
    data["user_id"] = g.user_id

    post = post_service.new_post(data)
    return jsonify(post), post["status"]

@post_bp.route('/post', methods=['GET'])
@require_auth
def list_posts():
    post = post_service.list_posts()
    #Os status HTTP estão vindo direto do service
    return jsonify(post), post["status"]

@post_bp.route('/post/<id>', methods=['GET'])
@require_auth
def list_post(id):
    post = post_service.list_post(id)
    return jsonify(post), post["status"]

@post_bp.route('/post/<id>', methods=['DELETE'])
@require_auth
def delete_post(id):
    post = post_service.delete_post(id)
    return jsonify(post), post["status"]
