# Askee

O Askee é um app de forum, onde usuários podem criar posts e interagir com outros usuários.

## Como configurar e rodar o servidor

Este projeto utiliza [uv](https://docs.astral.sh/uv/) para gerenciar o ambiente Python e as dependências.

1. **Instale o uv** (se ainda não tiver):
   ```bash
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```

2. **Entre na pasta do servidor**:
   ```bash
   cd Server
   ```

3. **Sincronize o ambiente e instale as dependências**:
   Isso criará o ambiente virtual (`.venv`) e instalará tudo que é necessário.
   ```bash
   uv sync
   ```

4. **Rode o servidor**:
   ```bash
   uv run python main.py
   ```
