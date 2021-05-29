import os
from dotenv import load_dotenv
load_dotenv()


class Config:
    host = os.getenv("API_HOST") or "localhost"
    port = os.getenv("API_PORT") or 5000

    # SQLAlchemy
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://{user}:{password}@{host}/{database}?charset=utf8".format(
        **{
            "user": os.getenv("DB_USER"),
            "password": os.getenv("DB_PASSWORD"),
            "host": os.getenv("DB_HOST"),
            "database": os.getenv("DB_DATABASE"),
        })
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False
