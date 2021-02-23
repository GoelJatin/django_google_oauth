FROM python:3.8-slim-buster

# Setup env
ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONFAULTHANDLER 1
ENV PYTHONUNBUFFERED 1

EXPOSE 8000

WORKDIR /app

RUN set -eux; \
    apt-get update; \
    apt-get install -y --no-install-recommends apt-utils; \
    pip install pipenv; \
    apt-get clean; \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

COPY Pipfile* ./
RUN pipenv lock --keep-outdated --requirements > requirements.txt; \
    pip install -r requirements.txt

COPY . .

CMD [ "bash", "startup.sh" ]
