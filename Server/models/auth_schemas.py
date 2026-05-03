from pydantic import BaseModel, Field
from typing import Optional

# Arquivo de schemas para o domínio de autenticação de usu[arios], usado para validação e formatação de dados
# Esses schemas são usados tanto para validar as requisições recebidas nos controllers quanto para formatar as respostas enviadas

# O que esperamos enviar num body de sign-up
class APIResponse(BaseModel):
    status: int
    message: str
    data: Optional[dict] = None

# O que esperamos receber num body de sign-up
class SignUpRequest(BaseModel):
    username: str = Field(..., min_length=3, max_length=50)
    email: str
    password: str = Field(..., min_length=6)
    name: str = Field(..., min_length=1, max_length=100)
    icon: Optional[str] = None
    about: Optional[str] = None
    is_super: bool
    is_moderator: bool

# O que esperamos receber num body de sign-in
class SignInRequest(BaseModel):
    email: str
    password: str

# O que vamos enviar como resposta quando um usuário fizer sign-in com sucesso
class AuthResponse(BaseModel):
    id: str
    username: str
    email: str
    name: str
    icon: Optional[str] = None
    about: Optional[str] = None
    is_super: bool
    is_moderator: bool
    token: str
