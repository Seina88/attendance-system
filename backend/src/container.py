from flask import Flask
from injector import Injector, Module, Binder, singleton

from domains.user.user_repository import UserRepository
from domains.user.user_service import UserService
from domains.user.user_service_impl import UserServiceImpl
from domains.session.session_repository import SessionRepository
from domains.session.session_service import SessionService
from domains.session.session_service_impl import SessionServiceImpl

from infrastructures.database import db, Database
from infrastructures.user.user_repository_impl import UserRepositoryImpl
from infrastructures.session.session_repository_impl import SessionRepositoryImpl


class Container(Module):
    def configure(self, binder: Binder) -> None:
        binder.bind(Flask, to=Flask(__name__), scope=singleton)
        binder.bind(Database, to=db, scope=singleton)

        binder.bind(UserRepository, to=UserRepositoryImpl)
        binder.bind(SessionRepository, to=SessionRepositoryImpl)

        binder.bind(UserService, to=UserServiceImpl)
        binder.bind(SessionService, to=SessionServiceImpl)


injector = Injector(modules=[Container])
