from flask import Flask
from flask_cors import CORS
from flask_restful import Api

from app import app

from configs.app_config import AppConfig
from configs.database_config import MainDatabaseConfig

from infrastructures.database import db, Database

from interfaces.router import Router


def main(app: Flask, db: Database, app_config: type, database_config: type) -> None:
    CORS(app)

    app.config.from_object(app_config)
    app.config.from_object(database_config)

    db.initialize(app)

    api = Api(app)
    Router(api)


main(app, db, AppConfig, MainDatabaseConfig)
