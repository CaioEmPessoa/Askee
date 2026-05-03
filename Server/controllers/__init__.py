from flask_openapi3 import APIBlueprint

from controllers.AuthController import auth_api
from controllers.UserController import user_api
from controllers.CategoryController import category_bp
from controllers.CommentController import comment_bp
from controllers.PostController import post_bp

apis = [auth_api, user_api]
blueprints = [category_bp, comment_bp, post_bp]
