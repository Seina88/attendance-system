import os
from dotenv import load_dotenv
load_dotenv(override=True)


class Config:
    api_host = os.getenv("API_HOST") or "120.0.0.1"
    api_port = os.getenv("API_PORT") or 5000
