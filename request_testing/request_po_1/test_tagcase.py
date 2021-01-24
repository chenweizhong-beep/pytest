import allure
import pytest
import yaml

from request_testing.request_po_1.tag import Tag


@allure.feature("标签管理接口测试")
class TestTagCase:
    def setup(self):
        with open("./conf.yml", encoding="utf-8") as f:
            data = yaml.safe_load(f)
            secret = data["corpsecret"]
        self.tag = Tag(secret=secret)

    # @pytest.mark.parametrize("tagname, tagid", [("UI", 12)])
    @allure.story("创建标签接口")
    @pytest.mark.run(order=1)
    def test_creat_tag(self, creat_tag):
        r = self.tag.creat_tag(creat_tag[0], creat_tag[1])
        if len(creat_tag[0]) > 32:
            assert r["errcode"] == 40058
        else:
            assert r["errmsg"] == "created"

    # @pytest.mark.parametrize("tagid,tagname", [(12, "SSSSS")])
    @allure.story("更新标签名字接口&查询标签列表接口")
    @pytest.mark.run(order=2)
    def test_update_tag(self, update_tag):
        r = self.tag.update_tag(update_tag[1], update_tag[0])
        r1 = self.tag.get_tag_list()
        # taglist = jsonpath(r1, "$..taglist[?(@.tagid==12)].tagname")
        taglist = self.tag.jsonpath_data(r1, f"$..taglist[?(@.tagid=={update_tag[1]})].tagname")
        assert r["errcode"] == 0
        assert update_tag[0] in taglist

    # @pytest.mark.parametrize("tagid", [(12)])
    @allure.story("删除标签接口")
    @pytest.mark.run(order=6)
    def test_deletde_tag(self, deleted_tag):
        r = self.tag.deleted_tag(deleted_tag[0])
        assert r["errcode"] == 0

    # @pytest.mark.parametrize("tagid, userlist, partylist", [(12, ["ChenDaGe"], [1]),(12, ["ChenErGe"], [2])])
    @allure.story("增加标签成员接口")
    @pytest.mark.run(order=3)
    def test_creat_tag_member(self, creat_member):
        r = self.tag.creat_tag_member(creat_member[0], creat_member[1], creat_member[2])
        print(r)
        assert r["errcode"] == 0

    # @pytest.mark.parametrize("tagid", [(12)])
    @allure.story("获取标签成员接口")
    @pytest.mark.run(order=4)
    def test_get_member_list(self, get_member):
        r = self.tag.get_tag_member(get_member[0])
        assert r["errmsg"] == "ok"
        print(r)

    # @pytest.mark.parametrize("tagid, userlist, partylist", [(12, ["ChenDaGe"], [1]), (12, ["ChenErGe"], [2])])
    @allure.story("删除标签成员接口")
    @pytest.mark.run(order=5)
    def test_deleted_member(self, deleted_member):
        r = self.tag.deleted_tag_member(deleted_member[0], deleted_member[1], deleted_member[2])
        print(r)
        assert r["errmsg"] == "deleted"
