from typing import Optional

from domains.session.session import Session
from domains.session.session_repository import SessionRepository

from infrastructures.database import Database
from infrastructures.session.session_dto import SessionDto


class SessionRepositoryImpl(SessionRepository):
    def __init__(self, db: Database) -> None:
        super().__init__()
        self.db = db

    def find_by_api_token(self, api_token: str) -> Optional[Session]:
        session_dto = self.db.session.query(
            SessionDto).filter_by(api_token=api_token).first()

        if session_dto is None:
            return None

        return self.__dto_to_domain_model(session_dto)

    def add(self, session: Session) -> None:
        session_dto = self.__domain_model_to_dto(session)
        self.db.session.add(session_dto)

    def commit(self) -> None:
        self.db.session.commit()

    def __dto_to_domain_model(self, session_dto: SessionDto) -> Session:
        return Session(session_dto.id, session_dto.user_id, session_dto.api_token)

    def __domain_model_to_dto(self, session: Session) -> SessionDto:
        return SessionDto(id=session.id, user_id=session.user_id, api_token=session.api_token, expire_at=session.expire_at)
