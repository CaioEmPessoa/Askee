from utils.response import build_response

class PostService:
  def __init__(self, post_repository):
    self.repository = post_repository

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
      return build_response(200, "Postagem registrada com sucesso.", response)
    else:
      return build_response(500, "Houve um erro ao criar a postagem.")

  def list_posts(self):
    posts = self.repository.get_all()

    if len(posts) == 0:
      return build_response(200, "Nenhuma postagem encontrada.")
    else:
      return build_response(200, "Postagens encontradas com sucesso.", posts)

  def list_post(self, id):
    post = self.repository.get_by_id(id)

    if post:
      return build_response(200, "Postagem encontrada com sucesso.", post)
    else:
      return build_response(200, "Nenhuma postagem encontrada.")

  def delete_post(self, id):
    post = self.repository.get_by_id(id)

    if not post:
      return build_response(400, "Postagem não encontrada.")

    response = self.repository.delete_on_id(id)

    if response:
      return build_response(200, "Postagem deletada com sucesso.")
    else:
      return build_response(500, "Houve um erro ao deletar a postagem.")