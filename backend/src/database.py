from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


class Database(SQLAlchemy):
    def __init__(self):
        super().__init__()

    def initialize(self, app):
        self.init_app(app)
        Migrate(app, self)


database = Database()
