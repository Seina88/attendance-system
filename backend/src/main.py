from flask import Flask
from flask_restful import Resource, Api
from flask_cors import CORS
from config import Config


def create_app():
    app = Flask(__name__)
    api = Api(app)
    CORS(app)
    return app, api


app, api = create_app()


@app.route("/", methods=["GET"])
def root():
    return "root"


class HelloWorld(Resource):
    def get(self):
        return {"message": "Hello World by get"}

    def post(self):
        return {"message": "Hello World by post"}

    def put(self):
        return {"message": "Hello World by put"}

    def delete(self):
        return {"message": "Hello World by delete"}


api.add_resource(HelloWorld, "/api/hello")


if __name__ == "__main__":
    app.run(host=Config.host, port=Config.port)
