from flask import Blueprint, jsonify, g, request
from repositories.Comment import Comment
from services.CommentService import CommentService
from middlewares.AuthMiddleware import require_auth

commentRepository = Comment()
comment_service = CommentService(commentRepository)

comment_bp = Blueprint('comment', __name__)

@comment_bp.route('/comments', methods=['POST'])
def new_comments():
    data = request.json

    comment = comment_service.new_comment(data)
    return jsonify(comment), comment["status"]

@comment_bp.route('/comments', methods=['GET'])
def list_all_comments():
    comment = comment_service.list_comments()
    return jsonify(comment), comment["status"]

@comment_bp.route('/comments/post/<post_id>', methods=['GET'])
def list_comment_by_post_id(post_id):
    comment = comment_service.list_comment_by_post_id(post_id)
    return jsonify(comment), comment["status"]

@comment_bp.route('/comments/<id>', methods=['GET'])
def list_comments(id):
    comment = comment_service.list_comment(id)
    return jsonify(comment), comment["status"]

@comment_bp.route('/comments/<id>', methods=['DELETE'])
def delete_comments(id):
    comment = comment_service.delete_comment(id)
    return jsonify(comment), comment["status"]
