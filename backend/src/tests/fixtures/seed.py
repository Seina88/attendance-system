from datetime import datetime, timedelta
from random import randint
from hashlib import md5
from faker import Faker
import pykakasi

from domains.user.user import User
from domains.session.session import Session

from infrastructures.database import Database
from infrastructures.user.user_dto import UserDto
from infrastructures.session.session_dto import SessionDto


def seed(db: Database) -> None:
    users = create_users(5)
    sessions = create_sessions(5, users)

    for user in users:
        db.session.add(user)
    for session in sessions:
        db.session.add(session)
    db.session.commit()


def create_users(num_users: int) -> list[UserDto]:
    faker = Faker("ja_JP")
    kakasi = pykakasi.kakasi()

    users = []
    for _ in range(num_users):
        last_name, first_name = faker.name().split(" ")
        nickname = "{}-{}".format(kakasi.convert(first_name)[
            0]["passport"], randint(0, 100))
        email = nickname + "@example.com"
        password = md5(nickname.encode("utf-8")).hexdigest()
        user = User(None, nickname, first_name, last_name, email, password)
        users.append(UserDto(id=user.id, nickname=user.nickname, first_name=user.first_name,
                             last_name=user.last_name, email=user.email, password=user.password))
    return users


def create_sessions(num_sessions: int, users: list[UserDto]) -> list[SessionDto]:
    sessions = []
    for i in range(num_sessions):
        user_id = users[i].id
        expire_at = datetime.now() + timedelta(days=10)
        session = Session(None, user_id, expire_at=expire_at)
        sessions.append(SessionDto(
            id=session.id, user_id=session.user_id, api_token=session.api_token, expire_at=session.expire_at))
    return sessions
