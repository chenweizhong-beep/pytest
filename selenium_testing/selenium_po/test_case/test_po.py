import pytest

from selenium_testing.selenium_po.page.main_page import MainPage


class TestPo:
    def setup(self):
        self.main = MainPage()

    def teardown(self):
        pass

    # @pytest.mark.skip
    @pytest.mark.parametrize("name,iname,id,phone,mail", [("test02", "test02", "002", "15310232145", "123@qq.com")])
    def test_po(self, name, iname, id, phone, mail):
        namelist = self.main.goto_cantact().click_add_member(). \
            add_member(name, iname, id, phone, mail).get_member()
        print(namelist)
        assert name in namelist

    # @pytest.mark.skip
    @pytest.mark.parametrize("name,iname,id,phone,mail", [("test03", "test03", "003", "15310232146", "1234@qq.com")])
    def test_po_01(self, name, iname, id, phone, mail):
        namelist = self.main.goto_add_member_page().add_member(name, iname, id, phone, mail).get_member()
        print(namelist)
        assert name in namelist
