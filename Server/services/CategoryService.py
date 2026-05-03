from utils import response_api

class CategoryService:
  def __init__(self, category_repository):
    self.repository = category_repository

  def get_category(self, id):
    response = self.repository.get_by_id(id)

    if response:
      return response_api.build(200, "Categoria encontrada!", response)
    else:
      return response_api.build(200, "Nenhuma categoria encontrada.")

  def list_categories(self):
    response = self.repository.get_all(id)

    if len(categories) == 0:
      return response_api.build(200, "Nenhuma categoria encontrada.")
    else:
      return response_api.build(200, "Categorias encontradas com sucesso.", categories)

  def add_category(self, data):
    # Nome
    name = data.get("name")

    if not name or name.strip() == '':
       return response_api.build(400, "É necessário informar um nome para a categoria.")

    existing_category = None # Lógica de busca

    if existing_category:
      return response_api.build(400, "Já existe uma categoria com o nome informado.")

    if len(name) > 20:
      return response_api.build(400, "O nome da categoria pode ter no maximo 20 caracteres.")

    # Pode conter caracteres não alfabéticos? sim&nao! talvez? >.<
    # Nome pode conter mais de uma palavra? nao vejo por que nao  poderia t er  es pa  co

    # Descrição
    description = data.get("description")

    if not description or description.strip() == '':
      return response_api.build(400, "É necessário informar uma descrição para a categoria.")

    # Remover?
    if len(description) > 500:
      return response_api.build(400, "A descrição deve conter pelo menos 10 caracteres.")

    # Ícone
    icon = data.get("icon")

    if not icon or icon.strip() == '':
       return response_api.build(400, "É necessário informar um ícone para a categoria.")

    if len(icon) != 3:
       return response_api.build(400, "O ícone deve ter exatamente 3 caracteres.")

    # Ver lógica dos moderadores

    new_category = {
       "name": name.strip(),
       "description": description.strip(),
       "icon": icon.strip(),
       "moderators": []
    }

    response = self.repository.new_entry(new_category)
    if response:
      return response_api.build(200, "Categoria criada com sucesso.", response)
    else:
      return response_api.build(500, "Houve um erro ao criar a categoria.")

  def update_category(self, id, data):
    category = self.repository.get_by_id(id)
    response = False

    # Validar novos dados

    response = self.repository.update_on_id(id)

    if response:
      return response_api.build(200, "Categoria atualizada com sucesso.", response)
    else:
      return response_api.build(500, "Houve um erro ao atualizar a categoria.")

  def delete_category(self, id):
    category = self.repository.get_by_id(id)
    response = False

    if not category:
      return response_api.build(400, "Categoria não encontrada.")

    response = self.repository.delete_on_id(id)

    if response:
      return response_api.build(200, "Categoria deletada com sucesso.")
    else:
      return Response(500, "Houve um erro ao deletar a categoria.")