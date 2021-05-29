from flask import Flask
from flask_cors import CORS
from flask_restful import Api
from .config import Config
from .database import Database
from .routes import Router


def create_app():
    app = Flask(__name__)

    CORS(app)

    app.config.from_object(Config)
    Database().initialize(app)

    api = Api(app)
    router = Router(api).set()
    return app


app = create_app()
