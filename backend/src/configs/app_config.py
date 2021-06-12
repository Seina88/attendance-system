import os
from dotenv import load_dotenv
load_dotenv()


class MainAppConfig:
    host = os.getenv("API_HOST", "localhost")
    port = os.getenv("API_PORT", 5000)


class TestAppConfig:
    TESTING = True
