from flask import Flask
from flask_testing import TestCase

from main import app
from container import injector

from tests.fixtures.seed import seed

from configs.app_config import TestAppConfig
from configs.database_config import TestDatabaseConfig

from infrastructures.database import Database


class TestCaseImpl(TestCase):
    def create_app(self) -> Flask:
        app.config.from_object(TestAppConfig)
        app.config.from_object(TestDatabaseConfig)
        return app

    def setUp(self) -> None:
        self.client = self.app.test_client()
        self.db = injector.get(Database)

        self.db.create_all()
        self.db.session.commit()
        seed(self.db)

    def tearDown(self) -> None:
        self.db.session.remove()
        self.db.drop_all()
