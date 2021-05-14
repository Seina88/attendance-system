install: backend-local-install

backend-install:
	cd backend/; \
	poetry install; \
	cd -;

backend-start:
	cd backend/; \
	sh ./bin/start.sh
