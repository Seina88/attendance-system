import os
from dotenv import load_dotenv
load_dotenv()


class AppConfig:
    host = os.getenv("API_HOST", "localhost")
    port = os.getenv("API_PORT", 5000)
