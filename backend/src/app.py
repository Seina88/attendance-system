from flask import Flask
from flask_cors import CORS
from flask_restful import Api
from .configs.app_config import AppConfig
from .configs.database_config import DatabaseConfig
from .database import database
from .router import Router
from .models import *


class App(Flask):
    def __init__(self, import_name, app_config, database_config, database):
        super().__init__(import_name)

        CORS(self)

        self.config.from_object(app_config)
        self.config.from_object(database_config)

        database.initialize(self)

        self.api = Api(self)
        self.router = Router(self.api).set()


app = App(__name__, AppConfig, DatabaseConfig, database)
