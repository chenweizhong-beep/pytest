
from request_testing.request_po_1.appapi_1 import AppApi1


class WeWork1(AppApi1):
    def __init__(self, secret):
        self.access_token = self.get_access_token(secret)

    def get_access_token(self, secret):
        req = {
            "url": "https://qyapi.weixin.qq.com/cgi-bin/gettoken",
            "params": {
                "corpid": "wwe053b4cf05614835",
                "corpsecret": secret
            },
            "method": "GET"

        }
        r = self.send_req(req)
        self.access_token = r.json()["access_token"]
        return self.access_token
