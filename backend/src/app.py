from flask import Flask
from flask_cors import CORS
from flask_restful import Api
from .config import Config
from .database import database
from .routes import Router
from .models import *


class App(Flask):
    def __init__(self, database, Config):
        super().__init__(__name__)

        CORS(self)

        self.config.from_object(Config)

        database.initialize(self)

        self.api = Api(self)
        self.router = Router(self.api).set()


app = App(database, Config)
