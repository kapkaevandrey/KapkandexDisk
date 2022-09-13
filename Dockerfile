FROM python:3.10

ENV POETRY_VERSION=1.2.0

RUN pip install "poetry==$POETRY_VERSION"

WORKDIR /code
COPY poetry.lock pyproject.toml /code/

RUN poetry config virtualenvs.create false && poetry install --no-interaction --no-ansi

COPY ./alembic /code/alembic
COPY ./app /code/app
COPY ./tests /code/tests
COPY alembic.ini .