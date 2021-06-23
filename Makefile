#############
### Local ###
#############
.PHONY: install
install: frontend-install backend-install

.PHONY: frontend-install
frontend-install:
	cd frontend/; \
	yarn install; \
	cd -

.PHONY: backend-install
backend-install:
	cd backend/; \
	poetry install; \
	cd -

.PHONY: frontend-build
frontend-build:
	cd frontend/; \
	yarn run build; \
	cd -

.PHONY: frontend-start
frontend-start: frontend-build
	cd frontend/; \
	yarn run start

.PHONY: backend-start
backend-start:
	cd backend/src/; \
	sh ../bin/start.sh

##############
### Docker ###
##############
.PHONY: build
build:
	docker-compose build

.PHONY: no-cache-build
no-cache-build:
	docker-compose build --no-cache

.PHONY: start
start: build
	docker-compose up -d

.PHONY: stop
stop:
	docker-compose stop

.PHONY: clean
clean:
	docker-compose down --rmi all --volumes --remove-orphans

.PHONY: restart
restart: stop build start

.PHONY: frontend-attach
frontend-attach: start
	docker-compose exec frontend bash

.PHONY: backend-attach
backend-attach: start
	docker-compose exec backend bash

.PHONY: nginx-attach
nginx-attach: start
	docker-compose exec nginx bash

.PHONY: database-attach
database-attach: start
	docker-compose exec database mysql -u root -p

.PHONY: test
test: backend-test

.PHONY: backend-test
backend-test: start
	docker-compose exec backend pytest -vvv
