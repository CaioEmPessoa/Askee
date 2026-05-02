import json
import uuid

exemplo_request = {
    "id": "   Exemplo.  ",
    "name": "Nome",
    "description": "Easasxemplo.  ",
    "icon": "Elo",
    "moderators": ["Exemplo"]
  }

# Temporário
def build_response(status, message, data = {}):
  return {
     "status": status,
     "message": message,
     "data": data
  }

with open('/Users/joao/Documents/Outros/Askee/Database/Categories.json', 'r') as file:
    data_dict = json.load(file)

class CategoryService:
  def _init_(self, category_repository):
    self.repository = category_repository

  def add_category(self, data):
    # Nome
    name = data.get("name")

    if not name or name.strip() == '':
       return build_response(400, "É necessário informar um nome para a categoria.")

    existing_category = None # Lógica de busca

    if existing_category:
      return build_response(400, "Já existe uma categoria com o nome informado.")

    if len(name) > 20:
      return build_response(400, "O nome da categoria pode ter no maximo 20 caracteres.")

    # Pode conter caracteres não alfabéticos? sim&nao! talvez? >.<
    # Nome pode conter mais de uma palavra? nao vejo por que nao  poderia t er  es pa  co

    # Descrição
    description = data.get("description")

    if not description or description.strip() == '':
      return build_response(400, "É necessário informar uma descrição para a categoria.")

    # Remover?
    if len(description) > 500:
      return build_response(400, "A descrição deve conter pelo menos 10 caracteres.")

    # Ícone
    icon = data.get("icon")

    if not icon or icon.strip() == '':
       return build_response(400, "É necessário informar um ícone para a categoria.")

    if len(icon) != 3:
       return build_response(400, "O ícone deve ter exatamente 3 caracteres.")

    # Ver lógica dos moderadores

    new_category = {
       "id": uuid.uuid4().hex,
       "name": name.strip(),
       "description": description.strip(),
       "icon": icon.strip(),
       "moderators": []
    }

    # Inserir no JSON

    return build_response(200, "Categoria criada com sucesso.", new_category)

  def list_categories(self):
    categories = [] # Lógica de listagem

    if len(categories) == 0:
      return build_response(200, "Nenhuma categoria encontrada.")

    else:
      return build_response(200, "Categorias encontradas com sucesso.", categories)

  def update_category(self, id, data):
    category = {} # Lógica de busca

    # Validar novos dados

    updated_category = category | data

    # Atualizar o JSON

    return build_response(200, "Categoria atualizada com sucesso.", updated_category)

  def delete_category(self, id):
    category = {} # Lógica de busca

    if not category:
      return build_response(400, "Categoria não encontrada.")

    # Deletar do JSON

    build_response(200, "Categoria deletada com sucesso.")

xisde = CategoryService(data_dict)

print(xisde.list_categories())