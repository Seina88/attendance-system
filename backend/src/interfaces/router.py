from flask_restful import Api

from interfaces.user.get_user import GetUser
from interfaces.user.create_user import CreateUser
from interfaces.user.update_user import UpdateUser
from interfaces.session.get_session import GetSession
from interfaces.session.create_session import CreateSession


class Router:
    def __init__(self, api: Api) -> None:
        api.add_resource(GetUser, "/api/users/<id>")
        api.add_resource(CreateUser, "/api/users")
        api.add_resource(UpdateUser, "/api/users/<id>")
        api.add_resource(GetSession, "/api/session")
        api.add_resource(CreateSession, "/api/login")
