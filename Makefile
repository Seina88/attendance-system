install: frontend-install backend-install

frontend-install:
	cd frontend/; \
	yarn install; \
	cd -

backend-install:
	cd backend/; \
	poetry install; \
	cd -

frontend-build:
	cd frontend/; \
	yarn run build; \
	cd -

frontend-start:
	cd frontend/; \
	yarn run start

backend-start:
	cd backend/src/; \
	sh ../bin/start.sh

build:
	docker-compose build

no-cache-build:
	docker-compose build --no-cache

start:
	docker-compose up -d

stop:
	docker-compose stop

clean:
	docker-compose down --rmi all --volumes --remove-orphans

restart: stop build start

frontend-attach:
	docker-compose exec frontend bash

backend-attach:
	docker-compose exec backend bash

nginx-attach:
	docker-compose exec nginx bash

database-attach:
	docker-compose exec database mysql -u root -p
