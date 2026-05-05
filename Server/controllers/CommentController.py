from flask import Blueprint, jsonify, g, request
from repositories.Comment import comment_repository
from services.CommentService import CommentService
from middlewares.AuthMiddleware import require_auth

comment_service = CommentService(comment_repository)
comment_bp = Blueprint('comment', __name__)

@comment_bp.route('/comments', methods=['POST'])
def new_comments():
    data = request.json

    comment = comment_service.new_comment(data)
    return jsonify(comment), comment["status"]

@comment_bp.route('/comments', methods=['GET'])
def list_allComments():
    comment = comment_service.list_comments()
    return jsonify(comment), comment["status"]

@comment_bp.route('/comments/<id>', methods=['GET'])
def list_comments(id):
    comment = comment_service.list_comment(id)
    return jsonify(comment), comment["status"]

@comment_bp.route('/comments/<id>', methods=['DELETE'])
def delete_comments(id):
    comment = comment_service.delete_comment(id)
    return jsonify(comment), comment["status"]