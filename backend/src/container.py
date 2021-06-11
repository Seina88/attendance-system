from flask import Flask

from app import app

from domains.user.user_repository import UserRepository
from domains.session.session_repository import SessionRepository
from domains.user.user_service import UserService
from domains.session.session_service import SessionService

from infrastructures.database import db, Database
from infrastructures.user.user_repository_impl import UserRepositoryImpl
from infrastructures.session.session_repository_impl import SessionRepositoryImpl

from applications.user.user_application_service import UserApplicationService
from applications.session.session_application_service import SessionApplicationService


class Container:
    def __init__(self, app: Flask, db: Database) -> None:
        self.app = app

        self.db = db

        self.user_repository = None
        self.session_repository = None

        self.user_service = None
        self.session_service = None

        self.user_application_service = None
        self.session_application_service = None

    def create_user_repository(self) -> UserRepository:
        self.user_repository = self.user_repository or UserRepositoryImpl(
            self.db)
        return self.user_repository

    def create_session_repository(self) -> SessionRepository:
        self.session_repository = self.session_repository or SessionRepositoryImpl(
            self.db)
        return self.session_repository

    def create_user_service(self) -> UserService:
        user_repository = self.create_user_repository()
        self.user_service = self.user_service or UserService(user_repository)
        return self.user_service

    def create_session_service(self) -> SessionService:
        session_repository = self.create_session_repository()
        self.session_service = self.session_service or SessionService(
            session_repository)
        return self.session_service

    def create_user_application_service(self) -> UserApplicationService:
        user_repository = self.create_user_repository()
        session_repository = self.create_session_repository()
        user_service = self.create_user_service()
        session_service = self.create_session_service()
        self.user_application_service = self.user_application_service or UserApplicationService(
            user_repository, session_repository, user_service, session_service)
        return self.user_application_service

    def create_session_application_service(self) -> SessionApplicationService:
        user_repository = self.create_user_repository()
        session_repository = self.create_session_repository()
        self.session_application_service = self.session_application_service or SessionApplicationService(
            user_repository, session_repository)
        return self.session_application_service


container = Container(app, db)
