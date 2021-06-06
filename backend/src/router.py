from .apis.helloWorld import HelloWorld
from .apis.user import User
from .apis.user_list import UserList


class Router:
    def __init__(self, api):
        self.api = api

    def set(self):
        self.api.add_resource(HelloWorld, "/api/hello")
        self.api.add_resource(User, "/api/users/<id>")
        self.api.add_resource(UserList, "/api/users")
