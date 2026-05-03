from utils.response import build_response

class PostService:
  def __init__(self, post_repository):
    self.repository = post_repository

  def validate_post(self, data):
    [
      {
        "id": "Exemplo",
        "title": "Exemplo",
        "date": "Exemplo",
        "content": "Exemplo",
        "user_id": "Exemplo",
        "category_id": "Exemplo",
        "comments": [
          {
            "user_id": "Exemplo",
            "content": "Exemplo"
          }
        ]
      }
    ]

    # Título
    title = data.get("title")

    if not title or title.strip() == "":
      return build_response(400, "É necessário informar um título para a postagem.")

    if len(title) > 50:
      return build_response(400, "O título da postagem pode ter no maximo 50 caracteres.")

    # data?

    content = data.get("content")

    if not content or content.strip() == "":
      return build_response(400, "É necessário informar o corpo da postagem.")

    if len(content) > 1000:
      return build_response(400, "O corpo da postagem pode ter no maximo 1000 caracteres.")


  def add_post(self, data):
    validation = self.validate_post(data)

    if validation:
      return validation

    new_post = {
      "title": "Exemplo",
      "date": "Exemplo",
      "content": "Exemplo",
      "user_id": "Exemplo",
      "category_id": "Exemplo",
      "comments": [
        {
          "user_id": "Exemplo",
          "content": "Exemplo"
        }
      ]
    }

