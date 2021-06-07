from .apis.user import User
from .apis.user_list import UserList
from .apis.login import Login


class Router:
    def __init__(self, api):
        self.api = api

    def set(self):
        self.api.add_resource(User, "/api/users/<id>")
        self.api.add_resource(UserList, "/api/users")
        self.api.add_resource(Login, "/api/login")
