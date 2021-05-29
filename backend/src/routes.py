from .apis.hoge import HogeListAPI, HogeAPI
from .apis.helloWorld import HelloWorld


class Router:
    def __init__(self, api):
        self.api = api

    def set(self):
        self.api.add_resource(HogeListAPI, "/hoges")
        self.api.add_resource(HogeAPI, "/hoges/<id>")
        self.api.add_resource(HelloWorld, "/api/hello")
