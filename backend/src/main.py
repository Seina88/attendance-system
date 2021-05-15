from flask import Flask, make_response, jsonify
from flask_cors import CORS
from config import Config


app = Flask(__name__)
CORS(app)


@app.route("/", methods=["GET"])
def root():
    return "root"


@app.route("/api/hello", methods=["GET"])
def hello():
    response = {
        "message": "Hello World!"
    }
    return make_response(jsonify(response))


if __name__ == "__main__":
    app.run(host=Config.host, port=Config.port)
