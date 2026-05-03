from flask_openapi3 import APIBlueprint, Tag
from flask import jsonify, g, request
from models.user_schemas import UserCreate, UserUpdate, UserResponse
from models.auth_schemas import APIResponse
from middlewares.AuthMiddleware import require_auth
from registers.User import user_repository

user_api = APIBlueprint('user', __name__, url_prefix='/users',
    abp_tags=[Tag(name='User', description='Endpoints de usuários')])

@user_api.post('')
def new_user(body: UserCreate):
    data = body.model_dump()
    response = user_repository.new_entry(data)
    if response:
        user_data = {k: v for k, v in response.items() if k != "password"}
        return jsonify({"status": 201, "message": "Usuario criado com sucesso.", "data": user_data}), 201
    return jsonify({"status": 500, "message": "Houve um erro ao criar o usuario."}), 500

@user_api.get('')
def list_users():
    users = user_repository.get_all()
    users_list = [{k: v for k, v in u.items() if k != "password"} for u in users.values()]
    return jsonify({"status": 200, "message": "OK", "data": users_list}), 200

@user_api.get('/<id>')
def list_user(id: str):
    user = user_repository.get_by_id(id)
    if not user:
        return jsonify({"status": 404, "message": "Usuario nao encontrado."}), 404
    user_data = {k: v for k, v in user.items() if k != "password"}
    return jsonify({"status": 200, "message": "OK", "data": user_data}), 200

@user_api.get('/@me')
@require_auth
def get_me():
    user = user_repository.get_by_id(g.user_id)
    if not user:
        return jsonify({"status": 404, "message": "Usuario não encontrado."}), 404
    user_data = {k: v for k, v in user.items() if k != "password"}
    return jsonify({"status": 200, "message": "OK", "data": user_data}), 200

@user_api.put('/<id>')
def update_user(id: str, body: UserUpdate):
    user = user_repository.get_by_id(id)
    if not user:
        return jsonify({"status": 404, "message": "Usuario nao encontrado."}), 404
    data = body.model_dump(exclude_unset=True)
    response = user_repository.update_on_id(id, data)
    if response:
        user_data = {k: v for k, v in response.items() if k != "password"}
        return jsonify({"status": 200, "message": "Usuario atualizado com sucesso.", "data": user_data}), 200
    return jsonify({"status": 500, "message": "Houve um erro ao atualizar o usuario."}), 500

@user_api.delete('/<id>')
def delete_user(id: str):
    user = user_repository.get_by_id(id)
    if not user:
        return jsonify({"status": 404, "message": "Usuario nao encontrado."}), 404
    response = user_repository.delete_on_id(id)
    if response:
        return jsonify({"status": 200, "message": "Usuario deletado com sucesso."}), 200
    return jsonify({"status": 500, "message": "Houve um erro ao deletar o usuario."}), 500
