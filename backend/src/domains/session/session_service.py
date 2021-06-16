from datetime import datetime

from container import container, Container

from domains.session.session_repository import SessionRepository


class SessionService:
    def __init__(self, session_repository: SessionRepository) -> None:
        self.session_repository = session_repository

    def authenticated(self, api_token: str) -> bool:
        session = self.session_repository.find_by_api_token(api_token)

        if session is None:
            return False

        return session.expire_at >= datetime.now()


def builder(container: Container) -> SessionService:
    session_repository = container.inject("SessionRepository")
    return SessionService(session_repository)


container.register("SessionService", builder)
