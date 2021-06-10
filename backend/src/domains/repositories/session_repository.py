from typing import Optional
from database import Database
from domains.models.session import Session


class SessionRepository:
    def __init__(self, database: Database):
        self.session = database.session
        self.model = Session

    def find_by_api_token(self, api_token: str) -> Optional[Session]:
        return self.session.query(
            self.model).filter_by(api_token=api_token).first()

    def add(self, session: Session) -> None:
        self.session.add(session)

    def commit(self) -> None:
        self.session.commit()
