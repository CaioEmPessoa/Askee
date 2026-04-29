#Blueprint cria um mini app de rotas, criado pois usando apenas o app estava dando conflito
#Arquivo pra adicionar os bps de cada registers para não precisar mexer diretamente no main.py

from flask import Blueprint

from registers.Category  import category_bp
from registers.Comment import comment_bp
from registers.Post import post_bp
from registers.User import user_bp


blueprints = [category_bp, comment_bp, user_bp, post_bp]