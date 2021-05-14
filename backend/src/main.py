from flask import Flask, make_response, jsonify
from config import Config

app = Flask(__name__)


@app.route("/", methods=["GET"])
def hello():
    response = {
        "message": "Hello, World!"
    }
    return make_response(jsonify(response))


if __name__ == "__main__":
    app.run(host=Config.api_host, port=Config.api_port)
