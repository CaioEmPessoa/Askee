from repositories.User import user_repository
from utils import response_api
from utils.auth import generate_token
import re

# Serviço para o domínio de autenticação
class AuthService:
    def __init__(self, repository):
        self.repository = repository

    # Cadastrar um novo usuário
    def sign_up(self, data):
        username = data.get("username")
        email = data.get("email")
        password = data.get("password")
        name = data.get("name")
        icon = data.get("icon")
        about = data.get("about")
        is_super = data.get("is_super")
        is_moderator = data.get("is_moderator")

        # Validações (só se o service não foi chamado pelo nosso controler que já tem validação pelo pydantic.)
        if not username or not email or not password:
            return response_api.build(400, "Username, email e password são obrigatórios.")
        if not name:
            return response_api.build(400, "Name é obrigatório.")
        if is_super is None or is_moderator is None:
            return response_api.build(400, "is_super e is_moderator são obrigatórios.")
        if not isinstance(is_super, bool) or not isinstance(is_moderator, bool):
            return response_api.build(400, "is_super e is_moderator devem ser booleanos.")

        normalized_email = email.strip().lower()
        normalized_username = username.strip()
        if normalized_username == "":
            return response_api.build(400, "Username não pode ser vazio.")
        if name.strip() == "":
            return response_api.build(400, "Name não pode ser vazio.")
        if icon is not None and isinstance(icon, str) and icon.strip() == "":
            return response_api.build(400, "Icon não pode ser vazio quando informado.")
        if about is not None and isinstance(about, str) and about.strip() == "":
            return response_api.build(400, "About não pode ser vazio quando informado.")
        if icon is not None and not isinstance(icon, str):
            return response_api.build(400, "Icon deve ser uma string quando informado.")
        if about is not None and not isinstance(about, str):
            return response_api.build(400, "About deve ser uma string quando informado.")
        if icon is not None and not re.match(r"^data:image\/(webp|png|jpg|jpeg);base64,", icon.strip(), re.IGNORECASE):
            return response_api.build(400, "Icon deve ser base64 com data URI de webp/png/jpg/jpeg.")

        # Validações adicionais de DTO
        if len(normalized_username) < 3:
            return response_api.build(400, "Username deve ter pelo menos 3 caracteres.")
        if not re.match(r"[^@]+@[^@]+\.[^@]+", normalized_email):
            return response_api.build(400, "Formato de email inválido.")
        if len(password) < 6:
            return response_api.build(400, "Password deve ter pelo menos 6 caracteres.")

        # Verificar se usuário ou email já foram cadastrados
        if self.repository.get_by_email(normalized_email):
            return response_api.build(400, "Já existe um usuário com este email.")
        if self.repository.get_by_username(normalized_username):
            return response_api.build(400, "Já existe um usuário com este username.")

        # Payload final do usuário - tanto que vamos salvar no banco e enviar como resposta no controller (omitindo a senha)
        new_user = {
            "username": normalized_username,
            "email": normalized_email,
            "password": password,
            "name": name.strip(),
            "icon": icon.strip() if isinstance(icon, str) else None,
            "about": about.strip() if isinstance(about, str) else None,
            "is_super": is_super,
            "is_moderator": is_moderator
        }

        response = self.repository.new_entry(new_user)
        if response:
            # Criar token JWT para autenticação em rotas protegidas
            token = generate_token(response["id"])
            if not token:
                return response_api.build(500, "AUTH_JWT_SECRET não está configurado.")

            # Omitir a senha na resposta e incluir o token
            user_data = {k: v for k, v in response.items() if k != 'password'}
            user_data["token"] = token

            return response_api.build(201, "Usuário criado com sucesso.", user_data)
        else:
            return response_api.build(500, "Houve um erro ao criar o usuário.")

    # Autenticar um usuário já existente
    def sign_in(self, data):
        email = data.get("email")
        password = data.get("password")

        if not email or not password:
            return response_api.build(400, "Email e senha são obrigatórios.")

        user = self.repository.get_by_email(email.strip().lower())
        if not user:
            return response_api.build(401, "Email ou senha inválidos.")

        if user.get("password") != password:
            return response_api.build(401, "Email ou senha inválidos.")

        # Criar token JWT para autenticação em rotas protegidas
        token = generate_token(user["id"])
        if not token:
            return response_api.build(500, "AUTH_JWT_SECRET não está configurado.")

        user_data = {k: v for k, v in user.items() if k != 'password'}
        user_data["token"] = token

        return response_api.build(200, "Login realizado com sucesso.", user_data)

auth_service = AuthService(user_repository)
