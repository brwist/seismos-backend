##########################################
## flask app
##########################################
FROM python:3.9-slim-buster

ENV CURR_ENV dev
ENV PYTHONFAULTHANDLER 1
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PIP_NO_CACHE_DIR off
ENV PIP_DISABLE_PIP_VERSION_CHECK on
ENV PYTHONHASHSEED random

RUN apt-get update
# RUN apt-get upgrade && apt-get -y dist-upgrade
RUN apt-get full-upgrade
RUN apt-get install -y curl default-libmysqlclient-dev gcc
RUN apt install -y netcat

RUN python -m pip install --upgrade pip
# install poetry
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
ENV PATH="${PATH}:/root/.poetry/bin"
RUN poetry self update
COPY poetry.lock .
COPY pyproject.toml .
RUN poetry config virtualenvs.create false \
  && poetry install $(test "$CURR_ENV" == prod && echo "--no-dev") --no-interaction --no-ansi

COPY . .
COPY ./entrypoint.sh /bin/entrypoint.sh
RUN chmod +x /bin/entrypoint.sh
EXPOSE 5000
WORKDIR /
ENTRYPOINT [ "entrypoint.sh" ]
# ENTRYPOINT [ "poetry" ]
# CMD ["run", "flask", "run", "--host=0.0.0.0", "--port=5000"]
