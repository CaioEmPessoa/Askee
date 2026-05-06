from utils import response_api

class CommentService:
  def __init__(self, comment_repository):
    self.repository = comment_repository

  def validate_comment(self, data):
    # Validação do usuário
    user_id = data.get("user_id")
    post_id = data.get("post_id")

    if not user_id or str(user_id).strip() == '':
      return response_api.build(400, "O comentário precisa de um autor.")
    if not post_id or str(post_id).strip() == '':
      return response_api.build(400, "O comentário precisa de um post.")

    # Validação do conteúdo
    content = data.get("content")

    if not content or str(content).strip() == '':
      return response_api.build(400, "O comentário não pode estar vazio.")

    if len(str(content)) > 1000:
      return response_api.build(400, "O comentário pode ter no máximo 1000 caracteres.")

    return None

  def new_comment(self, data):
    validation = self.validate_comment(data)

    if validation:
      return validation

    new_comment = {
      "user_id": str(data.get("user_id")).strip(),
      "post_id": str(data.get("post_id")).strip(),
      "content": str(data.get("content")).strip()
    }

    response = self.repository.new_entry(new_comment)

    if response:
      return response_api.build(200, "Comentário registrado com sucesso.", response)
    else:
      return response_api.build(500, "Houve um erro ao criar o comentário.")

  def list_comments(self):
    response = self.repository.get_all()

    if response is None:
      return response_api.build(500, "Houve um erro ao retornar os comentários.")
    if len(response) == 0:
      return response_api.build(200, "Nenhum comentário encontrado.")
    else:
      return response_api.build(200, "Comentários encontrados com sucesso.", response)

  def list_comment(self, id):
    response = self.repository.get_by_id(id)

    if response:
      return response_api.build(200, "Comentário encontrado com sucesso.", response)
    else:
      return response_api.build(200, "Nenhum comentário encontrado.")

  def delete_comment(self, id):
    comment = self.repository.get_by_id(id)

    if not comment:
      return response_api.build(400, "Comentário não encontrado.")

    response = self.repository.delete_on_id(id)

    if response:
      return response_api.build(200, "Comentário deletado com sucesso.")
    else:
      return response_api.build(500, "Houve um erro ao deletar o comentário.")