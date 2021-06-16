from flask import Flask
from flask_cors import CORS
from flask_restful import Api

import driver
from app import app
from container import container

from configs.app_config import MainAppConfig
from configs.database_config import MainDatabaseConfig

from infrastructures.database import Database
from infrastructures.user.user_dto import UserDto
from infrastructures.session.session_dto import SessionDto

from interfaces.router import Router


def main(app: Flask, app_config: type, database_config: type) -> Flask:
    CORS(app)

    app.config.from_object(app_config)
    app.config.from_object(database_config)

    db = container.inject("Database")
    db.initialize(app)

    api = Api(app)
    Router(api)

    return app


app = main(app, MainAppConfig, MainDatabaseConfig)
