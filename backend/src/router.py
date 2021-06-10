from interfaces.user.get_user import GetUser
from interfaces.user.create_user import CreateUser
from interfaces.login import Login


class Router:
    def __init__(self, api):
        self.api = api

    def set(self):
        self.api.add_resource(GetUser, "/api/users/<id>")
        self.api.add_resource(CreateUser, "/api/users/create")
        self.api.add_resource(Login, "/api/login")
