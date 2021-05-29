from flask_restful import Resource


class HelloWorld(Resource):
    def get(self):
        return {"message": "Hello World by get"}

    def post(self):
        return {"message": "Hello World by post"}

    def put(self):
        return {"message": "Hello World by put"}

    def delete(self):
        return {"message": "Hello World by delete"}
