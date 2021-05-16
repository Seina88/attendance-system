install: frontend-install backend-install

frontend-install:
	cd frontend/; \
	yarn install; \
	cd -

backend-install:
	cd backend/; \
	poetry install; \
	cd -

frontend-start:
	cd frontend/; \
	yarn run start

backend-start:
	cd backend/; \
	sh ./bin/start.sh

build:
	docker-compose build

start:
	docker-compose up -d

stop:
	docker-compose stop

restart: build start

frontend-attach:
	docker-compose exec frontend bash

backend-attach:
	docker-compose exec backend bash
