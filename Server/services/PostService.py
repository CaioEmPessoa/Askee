from utils import response_api

class PostService:
  def __init__(self, post_repository):
    self.repository = post_repository

  def validate_post(self, data):
    # Título
    title = data.get("title")

    if not title or str(title).strip() == '':
      return response_api.build(400, "É necessário informar um título para a postagem.")

    if len(title) > 100:
      return response_api.build(400, "O título da postagem pode ter no máximo 100 caracteres.")

    # Conteúdo
    content = data.get("content")

    if not content or str(content).strip() == '':
      return response_api.build(400, "É necessário informar o conteúdo da postagem.")

    if len(content) < 30:
      return response_api.build(400, "O conteúdo deve conter pelo menos 30 caracteres.")

    # ID do usuário
    user_id = data.get("user_id")

    if not user_id or str(user_id).strip() == '':
      return response_api.build(400, "O post precisa de um autor.")

    # ID da categoria
    category_id = data.get("category_id")

    if not category_id or str(category_id).strip() == '':
      return response_api.build(400, "É necessário informar a categoria da postagem.")

    return None

  def new_post(self, data):
    validation = self.validate_post(data)

    if validation:
      return validation

    new_post = {
      "title": data.get("title").strip(),
      "content": data.get("content").strip(),
      "user_id": data.get("user_id").strip(),
      "category_id": data.get("category_id").strip(),
      "comments": []
    }

    response = self.repository.new_entry(new_post)

    if response:
      return response_api.build(200, "Postagem registrada com sucesso.", response)
    else:
      return response_api.build(500, "Houve um erro ao criar a postagem.")

  def list_posts(self):
    response = self.repository.get_all()

    if response is None:
      return response_api.build(500, "Houve um erro ao retornar as postagens.")
    if len(response) == 0:
      return response_api.build(200, "Nenhuma postagem encontrada.")
    else:
      return response_api.build(200, "Postagens encontradas com sucesso.", response)

  def list_posts_by_category(self, category_id):
    posts = self.list_posts()

    if posts["status"] != 200 or posts["data"] == []:
      return posts

    result = [post for post in posts["data"] if post["category_id"] == category_id]

    if result:
      return response_api.build(200, "Postagens encontradas com sucesso.", result)
    else:
      return response_api.build(200, "Nenhuma postagem encontrada para a categoria especificada.")

  def list_post(self, id):
    response = self.repository.get_by_id(id)

    if response:
      return response_api.build(200, "Postagem encontrada com sucesso.", response)
    else:
      return response_api.build(200, "Nenhuma postagem encontrada.")

  def delete_post(self, id):
    post = self.repository.get_by_id(id)

    if not post:
      return response_api.build(400, "Postagem não encontrada.")

    response = self.repository.delete_on_id(id)

    if response:
      return response_api.build(200, "Postagem deletada com sucesso.", post)
    else:
      return response_api.build(500, "Houve um erro ao deletar a postagem.")