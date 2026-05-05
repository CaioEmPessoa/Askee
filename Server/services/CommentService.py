from utils.response import build_response

class CommentService:
  def __init__(self, comment_repository):
    self.repository = comment_repository


  def validate_comment(self, data):
      # Validação do Usuário
    user_id = data.get("user_id")

    if not user_id or str(user_id).strip() == '':
      return build_response(400, "O comentario precisa de um autor.")

      # Validação do Conteúdo
    content = data.get("content")

    if not content or str(content).strip() == '':
      return build_response(400, "O comentário não pode estar vazio.")
        
    if len(str(content)) > 1000: 
      return build_response(400, "O comentário pode ter no máximo 1000 caracteres.")

    return None

  def new_comment(self, data):
    new_comment = {
      "user_id": data.get("user_id").strip(),
      "content": data.get("content").strip()
    }

    response = self.repository.new_entry(new_comment)

    if response:
      return build_response(200, "Comentário registrado com sucesso.", response)
    else:
      return build_response(500, "Houve um erro ao criar o comentário.")

  def list_comments(self):
    comments = self.repository.get_all()

    if len(comments) == 0:
      return build_response(200, "Nenhum comentário encontrado.")
    else:
      return build_response(200, "Comentários encontrados com sucesso.", comments)

  def list_comment(self, id):
    comment = self.repository.get_by_id(id)

    if comment:
      return build_response(200, "Comentário encontrado com sucesso.", comment)
    else:
      return build_response(200, "Nenhum comentário encontrado.")

  def delete_comment(self, id):
    comment = self.repository.get_by_id(id)

    if not comment:
      return build_response(400, "Comentário não encontrado.")

    response = self.repository.delete_on_id(id)

    if response:
      return build_response(200, "Comentário deletado com sucesso.")
    else:
      return build_response(500, "Houve um erro ao deletar o comentário.")