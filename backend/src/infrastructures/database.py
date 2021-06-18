from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


class Database(SQLAlchemy):
    def __init__(self) -> None:
        super().__init__()
        self.migrate = Migrate()

    def initialize(self, app: Flask) -> None:
        self.init_app(app)
        self.migrate.init_app(app, self)


db = Database()
