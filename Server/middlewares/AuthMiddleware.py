import os
import jwt
from flask import request, jsonify, g

# Middleware para validar autenticação de usuários. Provavelmente vamos criar um middleware para checagem de permissões (is_super e is_moderator), mas esse só valida os tokens gerados no sign-in e sign-up.

def require_auth(handler):
    def wrapper(*args, **kwargs):
        auth_header = request.headers.get("Authorization", "")
        if not auth_header.startswith("Bearer "):
            return jsonify({"status": 401, "message": "Header Authorization ausente ou inválido."}), 401

        token = auth_header.replace("Bearer ", "", 1).strip()
        if token == "":
            return jsonify({"status": 401, "message": "Header Authorization ausente ou inválido."}), 401

        secret = os.getenv("AUTH_JWT_SECRET")
        if not secret:
            return jsonify({"status": 500, "message": "AUTH_JWT_SECRET não está configurado."}), 500

        try:
            payload = jwt.decode(token, secret, algorithms=["HS256"])
        except jwt.ExpiredSignatureError:
            return jsonify({"status": 401, "message": "Token expirado."}), 401
        except jwt.InvalidTokenError:
            return jsonify({"status": 401, "message": "Token inválido."}), 401

        g.user_id = payload.get("user_id")
        if not g.user_id:
            return jsonify({"status": 401, "message": "Token inválido."}), 401

        return handler(*args, **kwargs)

    wrapper.__name__ = handler.__name__
    return wrapper
