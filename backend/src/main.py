from flask import Flask, make_response, jsonify


app = Flask(__name__)


@app.route("/", methods=["GET"])
def hello():
    response = {
        "message": "Hello, World!"
    }
    return make_response(jsonify(response))
