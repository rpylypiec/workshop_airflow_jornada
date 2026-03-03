# Dockerfile - Opção 3
FROM python:3.10-slim

# Instalar dependências de sistema
RUN apt-get update && apt-get install -y \
    gcc \
    g++ \
    curl \
    python3-venv \
    && rm -rf /var/lib/apt/lists/*

# Criar diretório para o Poetry
ENV POETRY_HOME=/opt/poetry
RUN python3 -m venv $POETRY_HOME
RUN $POETRY_HOME/bin/pip install --no-cache-dir poetry
RUN ln -s $POETRY_HOME/bin/poetry /usr/local/bin/poetry

WORKDIR /app

# Copiar apenas os arquivos de dependências primeiro (para cache)
COPY pyproject.toml poetry.lock* ./

RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi --no-root

# Copiar o resto do código
COPY . .

# Criar arquivo de log
RUN touch execution_logs.log && chmod 666 execution_logs.log

EXPOSE 8501

CMD ["streamlit", "run", "exemplo_04.py", "--server.port=8501", "--server.address=0.0.0.0"]