from flask import Flask
from injector import Injector, Module, Binder, singleton

from applications.user.user_application_service import UserApplicationService
from applications.session.session_application_service import SessionApplicationService

from domains.user.user_repository import UserRepository
from domains.user.user_service import UserService
from domains.session.session_repository import SessionRepository
from domains.session.session_service import SessionService

from infrastructures.database import db, Database
from infrastructures.user.user_repository_impl import UserRepositoryImpl
from infrastructures.session.session_repository_impl import SessionRepositoryImpl


class Container(Module):
    def configure(self, binder: Binder) -> None:
        binder.bind(Flask, to=Flask(__name__), scope=singleton)
        binder.bind(Database, to=db, scope=singleton)

        binder.bind(UserRepository, to=UserRepositoryImpl)
        binder.bind(SessionRepository, to=SessionRepositoryImpl)

        binder.bind(UserService, to=UserService)
        binder.bind(SessionService, to=SessionService)

        binder.bind(UserApplicationService, to=UserApplicationService)
        binder.bind(SessionApplicationService, to=SessionApplicationService)


injector = Injector(modules=[Container])
