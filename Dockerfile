FROM ghcr.io/astral-sh/uv:0.9.2-python3.12-bookworm-slim

WORKDIR /app
COPY pyproject.toml uv.lock ./
RUN uv sync --frozen
ENV FLASK_APP=src.app

COPY src src
CMD ["uv", "run", "flask", "run", "--host", "0.0.0.0"]