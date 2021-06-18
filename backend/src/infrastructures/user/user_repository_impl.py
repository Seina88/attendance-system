from typing import Optional
from uuid import UUID
from injector import inject

from domains.user.user import User
from domains.user.user_repository import UserRepository

from infrastructures.database import Database
from infrastructures.user.user_dto import UserDto


class UserRepositoryImpl(UserRepository):
    @inject
    def __init__(self, db: Database) -> None:
        super().__init__()
        self.db = db

    def find_by_id(self, id: UUID) -> Optional[User]:
        user_dto = self.db.session.query(
            UserDto).filter_by(id=id).first()

        if user_dto is None:
            return None

        return self.__dto_to_domain_model(user_dto)

    def find_by_nickname(self, nickname: str) -> Optional[User]:
        user_dto = self.db.session.query(
            UserDto).filter_by(nickname=nickname).first()

        if user_dto is None:
            return None

        return self.__dto_to_domain_model(user_dto)

    def find_by_email(self, email: str) -> Optional[User]:
        user_dto = self.db.session.query(
            UserDto).filter_by(email=email).first()

        if user_dto is None:
            return None

        return self.__dto_to_domain_model(user_dto)

    def find_by_info(self, info: str) -> Optional[User]:
        user_dto = self.find_by_nickname(info) or self.find_by_email(info)

        if user_dto is None:
            return None

        return self.__dto_to_domain_model(user_dto)

    def add(self, user: User) -> None:
        user_dto = self.__domain_model_to_dto(user)
        self.db.session.add(user_dto)

    def update(self, user: User) -> None:
        user_dto = self.db.session.query(UserDto).filter_by(id=user.id).first()
        user_dto.update(user)
        self.db.session.add(user_dto)

    def commit(self) -> None:
        self.db.session.commit()

    def __dto_to_domain_model(self, user_dto: UserDto) -> User:
        return User(user_dto.id, user_dto.nickname, user_dto.first_name, user_dto.last_name, user_dto.email, user_dto.password)

    def __domain_model_to_dto(self, user: User) -> UserDto:
        return UserDto(id=user.id, nickname=user.nickname, first_name=user.first_name, last_name=user.last_name, email=user.email, password=user.password)
