import os
from dotenv import load_dotenv
load_dotenv()


class Config:
    host = os.getenv("API_HOST") or "localhost"
    port = os.getenv("API_PORT") or 5000
