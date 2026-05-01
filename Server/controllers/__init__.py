#Blueprint cria um mini app de rotas, criado pois usando apenas o app estava dando conflito
#Arquivo pra adicionar os bps de cada controller para não precisar mexer diretamente no main.py
from flask import Blueprint

from controllers.CategoryController  import category_bp
from controllers.CommentController import comment_bp
from controllers.PostController import post_bp
from controllers.UserController import user_bp


blueprints = [category_bp, comment_bp, user_bp, post_bp]