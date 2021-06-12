from flask_testing import TestCase

from main import main
from app import app

from configs.app_config import TestAppConfig
from configs.database_config import TestDatabaseConfig

from infrastructures.database import db


class MainTestCase(TestCase):
    def create_app(self) -> None:
        main(app, db, TestAppConfig, TestDatabaseConfig)
        return app

    def setUp(self) -> None:

        self.client = app.test_client()

        db.create_all()
        db.session.commit()

    def tearDown(self) -> None:
        db.session.remove()
        db.drop_all()
