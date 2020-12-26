
from selenium.webdriver.common.by import By

from selenium_testing.selenium_po.page.base_page import BasePage
from selenium_testing.selenium_po.page.contact_page import ContactPage


class AddMemberPage(BasePage):
    _ele_name = (By.ID, "username")
    _ele_iname = (By.ID, "memberAdd_english_name")
    _ele_id = (By.ID, "memberAdd_acctid")
    _ele_phone = (By.ID, "memberAdd_phone")
    _ele_mail = (By.ID, "memberAdd_mail")

    def add_member(self, name, iname, id, phone, mail):
        self.find(*self._ele_name).send_keys(name)
        self.find(*self._ele_iname).send_keys(iname)
        self.find(*self._ele_id).send_keys(id)
        self.find(*self._ele_phone).send_keys(phone)
        self.find(*self._ele_mail).send_keys(mail)
        self.find(By.CSS_SELECTOR, ".js_btn_save").click()
        return ContactPage(self.driver)
