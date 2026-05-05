from utils import response_api

class PostService:
  def __init__(self, post_repository):
    self.repository = post_repository

  def validate_post(self, data):
    #title
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

    # User ID
    user_id = data.get("user_id")

    if not user_id or str(user_id).strip() == '':
      return response_api.build(400, "O post precisa de um autor")

    # Category ID
    category_id = data.get("category_id")

    if not category_id or str(category_id).strip() == '':
      return response_api.build(400, "É necessário informar a categoria da postagem")

    return None

  def new_post(self, data):
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
    posts = self.repository.get_all()

    if len(posts) == 0:
      return response_api.build(200, "Nenhuma postagem encontrada.")
    else:
      return response_api.build(200, "Postagens encontradas com sucesso.", posts)

  def list_post(self, id):
    post = self.repository.get_by_id(id)

    if post:
      return response_api.build(200, "Postagem encontrada com sucesso.", post)
    else:
      return response_api.build(200, "Nenhuma postagem encontrada.")

  def delete_post(self, id):
    post = self.repository.get_by_id(id)

    if not post:
      return response_api.build(400, "Postagem não encontrada.")

    response = self.repository.delete_on_id(id)

    if response:
      return response_api.build(200, "Postagem deletada com sucesso.")
    else:
      return response_api.build(500, "Houve um erro ao deletar a postagem.")