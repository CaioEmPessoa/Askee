from flask_openapi3 import APIBlueprint, Tag
from flask import request, jsonify
from models.auth_schemas import SignUpRequest, SignInRequest, APIResponse
from services.AuthService import auth_service

auth_api = APIBlueprint('auth', __name__, url_prefix='/auth',
    abp_tags=[Tag(name='Auth', description='Endpoints de autenticacao')])

@auth_api.post('/sign-up')
def sign_up(body: SignUpRequest):
    data = body.model_dump()
    response = auth_service.sign_up(data)
    return jsonify(response), response.get("status", 200)

@auth_api.post('/sign-in')
def sign_in(body: SignInRequest):
    data = body.model_dump()
    response = auth_service.sign_in(data)
    return jsonify(response), response.get("status", 200)
