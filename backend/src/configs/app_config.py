import os
from dotenv import load_dotenv
load_dotenv()


class AppConfig:
    host = os.getenv("API_HOST", "localhost")
    port = os.getenv("API_PORT", 5000)

    SECRET_KEY = os.getenv("SECRET_KEY", os.urandom(20))
    SESSION_TYPE = os.getenv("SESSION_TYPE", "redis")
