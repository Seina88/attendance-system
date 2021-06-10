from typing import Optional
from database import Database
from domains.models.user import User


class UserRepository:
    def __init__(self, database: Database):
        self.session = database.session
        self.model = User

    def find_by_id(self, id: str) -> Optional[User]:
        return self.session.query(self.model).filter_by(id=id).first()

    def find_by_nickname(self, nickname: str) -> Optional[User]:
        return self.session.query(self.model).filter_by(
            nickname=nickname).first()

    def find_by_email(self, email: str) -> Optional[User]:
        return self.session.query(self.model.id).filter_by(email=email).first()

    def add(self, user: User) -> None:
        self.session.add(user)

    def commit(self) -> None:
        self.session.commit()
