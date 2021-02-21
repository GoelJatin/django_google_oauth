.PHONY: setup build up down restart web nuke-it-all

docker_compose = docker-compose -f docker-compose.yml

setup:
	pip install pipenv
	pipenv lock -r > src/requirements.txt

build:
	cp .env.development .env
	$(docker_compose) build

up:
	$(docker_compose) up

down:
	$(docker_compose) down

restart:
	$(MAKE) down
	$(MAKE) up

# local-setup:
# 	$(MAKE) setup
# 	cd ./src/ && pip install -r requirements.txt

# setup-local-db:
# 	$(MAKE) local-setup
# 	cd ./src/google_oauth && python manage.py migrate

# web:
# 	$(MAKE) local-setup
# 	$(MAKE) setup-local-db
# 	bash startup.sh;

all:
	$(MAKE) setup
	$(MAKE) build
	$(MAKE) up

nuke-it-all:
	$(docker_compose) down --volumes --remove-orphans
	docker system prune
	rm .env
	rm src/requirements.txt
