FROM python:3.11-slim

WORKDIR /app

# Instala git, curl e o gerenciador de pacotes 'uv'
RUN apt-get update && apt-get install -y git curl && \
    curl -LsSf https://astral.sh/uv/install.sh | sh && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Adiciona o uv ao PATH
ENV PATH="/root/.local/bin:${PATH}"

# Clona o repositório (contém pyproject.toml, uv.lock, e graphiti_mcp_server.py)
RUN git clone https://github.com/ceccato88/stacks.git .

# Instala as dependências
RUN uv sync

# Expõe a porta padrão do MCP server
EXPOSE 8000

# Executa o servidor MCP
CMD ["uv", "run", "graphiti_mcp_server.py"]
