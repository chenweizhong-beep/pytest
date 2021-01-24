
from request_testing.request_po_1.wework_1 import WeWork1


class Tag(WeWork1):
    # 创建标签接口
    def creat_tag(self, tagname, tagid):
        req = {
            "url": "https://qyapi.weixin.qq.com/cgi-bin/tag/create",
            "json": {
                "tagname": tagname,
                "tagid": tagid
            },
            "params": {
                "access_token": self.access_token
            },
            "method": "POST"
        }
        r = self.send_req(req)
        return r.json()

    # 更新标签名字接口
    def update_tag(self, tagid, tagname):
        req = {
            "url": "https://qyapi.weixin.qq.com/cgi-bin/tag/update",
            "params": {
                "access_token": self.access_token
            },
            "json": {
                "tagid": tagid,
                "tagname": tagname
            },
            "method": "POST"
        }
        r = self.send_req(req)
        return r.json()

    # 删除标签接口
    def deleted_tag(self, tagid):
        req = {
            "url": "https://qyapi.weixin.qq.com/cgi-bin/tag/delete",
            "params": {
                "access_token": self.access_token,
                "tagid": tagid
            },
            "method": "GET"
        }
        r = self.send_req(req)
        return r.json()

    # 获取标签列表接口
    def get_tag_list(self):
        req = {
            "url": "https://qyapi.weixin.qq.com/cgi-bin/tag/list",
            "params": {
                "access_token": self.access_token,
            },
            "method": "GET"
        }
        r = self.send_req(req)
        return r.json()

    # 增加标签成员接口
    def creat_tag_member(self, tagid, userlist, partylist):
        req = {
            "url": "https://qyapi.weixin.qq.com/cgi-bin/tag/addtagusers",
            "params": {
                "access_token": self.access_token,
            },
            "json": {
                "tagid": tagid,
                "userlist": userlist,
                "partylist": partylist
            },
            "method": "POST"
        }
        r = self.send_req(req)
        return r.json()

    # 删除标签成员接口
    def deleted_tag_member(self, tagid, userlist, partylist):
        req = {
            "url": "https://qyapi.weixin.qq.com/cgi-bin/tag/deltagusers",
            "params": {
                "access_token": self.access_token,
            },
            "json": {
                "tagid": tagid,
                "userlist": userlist,
                "partylist": partylist
            },
            "method": "POST"
        }
        r = self.send_req(req)
        return r.json()

    # 获取标签成员接口
    def get_tag_member(self, tagid):
        req = {
            "url": "https://qyapi.weixin.qq.com/cgi-bin/tag/get",
            "params": {
                "access_token": self.access_token,
                "tagid": tagid
            },
            "method": "GET"
        }
        r = self.send_req(req)
        return r.json()
