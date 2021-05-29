from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


class Database:
    def __init__(self):
        self.sqlAlchemy = SQLAlchemy()

    def initialize(self, app):
        self.sqlAlchemy.init_app(app)
        Migrate(app, self.sqlAlchemy)
