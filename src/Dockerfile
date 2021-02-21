FROM python:3.8-slim-buster

RUN set -eux; \
    apt-get update; \
    apt-get install -y --no-install-recommends apt-utils; \
    apt-get clean; \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

EXPOSE 8000

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD [ "bash", "startup.sh" ]
