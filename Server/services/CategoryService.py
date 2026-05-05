from utils import response_api

class CategoryService:
  def __init__(self, category_repository):
    self.repository = category_repository

  def validate_category(self, data):
    # Nome
    name = data.get("name")

    if not name or name.strip() == '':
      return response_api.build(400, "É necessário informar um nome para a categoria.")

    all_categories = self.list_categories()

    existing_category = next((category for category in all_categories if category["name"] == name), None)

    if existing_category:
      return response_api.build(400, "Já existe uma categoria com o nome informado.")

    if len(name) > 20:
      return response_api.build(400, "O nome da categoria pode ter no máximo 20 caracteres.")

    # Descrição
    description = data.get("description")

    if not description or description.strip() == '':
      return response_api.build(400, "É necessário informar uma descrição para a categoria.")

    if len(description) > 500:
      return response_api.build(400, "A descrição deve conter pelo menos 10 caracteres.")

    # Ícone
    icon = data.get("icon")

    if not icon or icon.strip() == '':
      return response_api.build(400, "É necessário informar um ícone para a categoria.")

    if len(icon) > 3:
      return response_api.build(400, "O ícone pode ter até 3 caracteres.")

    return None

  def add_category(self, data):
    validation = self.validate_category(data)

    if validation:
      return validation

    new_category = {
      "name": data.get("name").strip(),
      "description": data.get("description").strip(),
      "icon": data.get("icon").strip(),
      "moderators": []
    }

    response = self.repository.new_entry(new_category)

    if response:
      return response_api.build(200, "Categoria criada com sucesso.", response)
    else:
      return response_api.build(500, "Houve um erro ao criar a categoria.")

  def get_category(self, id):
    category = self.repository.get_by_id(id)

    if category:
      return response_api.build(200, "Categoria encontrada!", category)
    else:
      return response_api.build(200, "Nenhuma categoria encontrada.")

  def list_categories(self):
    categories = self.repository.get_all(id)

    if len(categories) == 0:
      return response_api.build(200, "Nenhuma categoria encontrada.")
    else:
      return response_api.build(200, "Categorias encontradas com sucesso.", categories)

  def list_category(self, id):
    category = self.repository.get_by_id(id)

    if category:
      return response_api.build(200, "Categoria encontrado com sucesso.", category)
    else:
      return response_api.build(200, "Nenhuma categoria encontrado.")

  def update_category(self, id, data):
    validation = self.validate_category(data)

    if validation:
      return validation

    category = self.repository.get_by_id(id)

    updated_category = category | data

    response = self.repository.update_on_id(id, updated_category)

    if response:
      return response_api.build(200, "Categoria atualizada com sucesso.", response)
    else:
      return response_api.build(500, "Houve um erro ao atualizar a categoria.")

  def delete_category(self, id):
    category = self.repository.get_by_id(id)

    if not category:
      return response_api.build(400, "Categoria não encontrada.")

    response = self.repository.delete_on_id(id)

    if response:
      return response_api.build(200, "Categoria deletada com sucesso.")
    else:
      return response_api.build(500, "Houve um erro ao deletar a categoria.")