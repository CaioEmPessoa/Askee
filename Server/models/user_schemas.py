from pydantic import BaseModel, Field
from typing import Optional

# Arquivo de schemas para o domínio de usuários, usado para validação e formatação de dados
# Esses schemas são usados tanto para validar as requisições recebidas nos controllers quanto para formatar as respostas enviadas

# O que esperamos receber num body de criação de usuário
class UserCreate(BaseModel):
    username: str = Field(..., min_length=3, max_length=50)
    email: str
    password: str = Field(..., min_length=6)
    name: str = Field(..., min_length=1, max_length=100)
    icon: Optional[str] = None
    about: Optional[str] = None
    is_super: bool
    is_moderator: bool

# O que vamos receber num body de update
class UserUpdate(BaseModel):
    username: Optional[str] = Field(None, min_length=3, max_length=50)
    email: Optional[str] = None
    name: Optional[str] = Field(None, min_length=1, max_length=100)
    icon: Optional[str] = None
    about: Optional[str] = None

# O que vamos enviar como resposta quando um usuário for criado ou atualizado
class UserResponse(BaseModel):
    id: str
    username: str
    email: str
    name: str
    icon: Optional[str] = None
    about: Optional[str] = None
    is_super: bool
    is_moderator: bool
