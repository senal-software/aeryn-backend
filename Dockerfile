FROM python:3.13
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/
WORKDIR /code
COPY ./pyproject.toml /code/pyproject.toml
COPY ./uv.lock /code/uv.lock
COPY ./.python-version /code/.python-version
COPY ./alembic.ini /code/alembic.ini
COPY ./alembic /code/alembic
RUN uv sync --locked
COPY ./app /code/app
CMD ["uv", "run", "fastapi", "dev", "app/main.py", "--port", "8000"]