install: frontend-install backend-install

frontend-install:
	cd frontend/; \
	yarn install; \
	cd -;

backend-install:
	cd backend/; \
	poetry install; \
	cd -;

frontend-start:
	cd frontend/; \
	yarn start

backend-start:
	cd backend/; \
	sh ./bin/start.sh
