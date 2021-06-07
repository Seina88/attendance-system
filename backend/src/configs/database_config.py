import os
from dotenv import load_dotenv
load_dotenv()


class DatabaseConfig:
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://{user}:{password}@{host}/{database}?charset=utf8".format(
        **{
            "user": os.getenv("DB_USER", "root"),
            "password": os.getenv("DB_PASSWORD"),
            "host": os.getenv("DB_HOST", "database"),
            "database": os.getenv("DB_DATABASE", "attendance_system"),
        })
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False


class TestDatabaseConfig:
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://{user}:{password}@{host}/{database}?charset=utf8".format(
        **{
            "user": os.getenv("DB_USER", "root"),
            "password": os.getenv("DB_PASSWORD"),
            "host": os.getenv("DB_HOST", "database"),
            "database": os.getenv("DB_DATABASE_TEST", "test"),
        })
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False
