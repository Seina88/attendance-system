from .app import app
from .configs.app_config import AppConfig


if __name__ == "__main__":
    app.run(host=AppConfig.host, port=AppConfig.port, debug=True)
