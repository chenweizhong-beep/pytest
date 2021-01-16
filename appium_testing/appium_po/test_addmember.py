import pytest
import yaml

from appium_testing.appium_po.app_page import AppPage

with open('./datas.yml', encoding='utf-8') as f:
    datas = yaml.safe_load(f)['add']
    name = datas['name']
    myid = datas['myid']


@pytest.fixture(params=name, ids=myid)
def add_member(request):
    data = request.param
    yield data


class TestAddMermber:
    def setup(self):
        self.app = AppPage()
        self.main = self.app.start().goto_main_page()

    def teardown(self):
        self.app.stop()

    def test_add_mermber(self, add_member):
        toast = self.main.click_addresslist().slip_click().add_hand_movement().edit_name(add_member[0]).edit_sex(
            add_member[1]).edit_phone(add_member[2]).click_save().get_toast()
        assert toast == '添加成功'
