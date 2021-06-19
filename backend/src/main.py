from flask import Flask
from flask_cors import CORS
from flask_restful import Api

from container import injector

from configs.app_config import MainAppConfig
from configs.database_config import MainDatabaseConfig

from infrastructures.database import Database
from infrastructures.user.user_dto import UserDto
from infrastructures.session.session_dto import SessionDto

from interfaces.router import Router


def main(app_config: type, database_config: type) -> Flask:
    app = injector.get(Flask)
    app.config.from_object(app_config)
    app.config.from_object(database_config)

    CORS(app)

    db = injector.get(Database)
    db.initialize(app)

    api = Api(app)
    Router(api)

    return app


app = main(MainAppConfig, MainDatabaseConfig)
