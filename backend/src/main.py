from flask import Flask
from flask_restful import Resource, Api
from flask_cors import CORS
from src.config import Config
from src.database import init_db
from src.apis import hoge


def create_app():
    app = Flask(__name__)
    api = Api(app)
    CORS(app)
    app.config.from_object(Config)
    init_db(app)
    api.add_resource(hoge.HogeListAPI, '/hoges')
    api.add_resource(hoge.HogeAPI, '/hoges/<id>')
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
