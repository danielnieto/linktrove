ARG PYTHON_VERSION=3.11-slim-bullseye

# Stage 1: Install Node.js and build frontend assets
FROM node:20 AS node_builder

WORKDIR /code

COPY . /code

RUN npm run build

# Stage 2: Build django app
FROM python:${PYTHON_VERSION}

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir -p /code

WORKDIR /code

RUN pip install poetry
COPY pyproject.toml poetry.lock /code/
RUN poetry config virtualenvs.create false
RUN poetry install --only main --no-root --no-interaction
COPY . /code

# Copy built frontend assets from node_builder stage
COPY --from=node_builder /code/linktrove/static/dist /code/linktrove/static/dist

RUN python manage.py collectstatic --noinput

EXPOSE 8000

CMD ["gunicorn", "--bind", ":8000", "--workers", "2", "config.wsgi"]
