import requests
from jsonpath import jsonpath


class AppApi1():
    def send_req(self, req):
        return requests.request(**req)

    def jsonpath_data(self, obj, expr):
        return jsonpath(obj, expr)
