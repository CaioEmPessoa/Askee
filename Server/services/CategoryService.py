from utils.response import build_response

class CategoryService:
  def __init__(self, category_repository):
    self.repository = category_repository

  def validate_category(self, data):
    # Nome
    name = data.get("name")

    if not name or name.strip() == '':
      return build_response(400, "É necessário informar um nome para a categoria.")

    if len(name) > 20:
      return build_response(400, "O nome da categoria pode ter no maximo 20 caracteres.")

    existing_category = None # Lógica de busca

    if existing_category:
      return build_response(400, "Já existe uma categoria com o nome informado.")

    # Descrição
    description = data.get("description")

    if not description or description.strip() == '':
      return build_response(400, "É necessário informar uma descrição para a categoria.")

    if len(description) > 500:
      return build_response(400, "A descrição da categoria pode conter no máximo 500 caracteres.")

    # Ícone
    icon = data.get("icon")

    if not icon or icon.strip() == '':
      return build_response(400, "É necessário informar um ícone para a categoria.")

    if len(icon) != 3:
      return build_response(400, "O ícone deve ter exatamente 3 caracteres.")

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
      return build_response(200, "Categoria criada com sucesso.", response)
    else:
      return build_response(500, "Houve um erro ao criar a categoria.")

  def list_categories(self):
    categories = self.repository.get_all(id)

    if len(categories) == 0:
      return build_response(200, "Nenhuma categoria encontrada.")
    else:
      return build_response(200, "Categorias encontradas com sucesso.", categories)

  def get_category(self, id):
    response = self.repository.get_by_id(id)

    if response:
      return build_response(200, "Categoria encontrada!", response)
    else:
      return build_response(200, "Nenhuma categoria encontrada.")

  def update_category(self, id, data):
    validation = self.validate_category(data)

    if validation:
      return validation

    category = self.repository.get_by_id(id)

    updated_category = category | data

    response = False

    response = self.repository.update_on_id(id, updated_category)

    if response:
      return build_response(200, "Categoria atualizada com sucesso.", response)
    else:
      return build_response(500, "Houve um erro ao atualizar a categoria.")


  def delete_category(self, id):
    category = self.repository.get_by_id(id)
    response = False

    if not category:
      return build_response(400, "Categoria não encontrada.")

    response = self.repository.delete_on_id(id)

    if response:
      return build_response(200, "Categoria deletada com sucesso.")
    else:
      return build_response(500, "Houve um erro ao deletar a categoria.")