
from selenium.webdriver.common.by import By

from selenium_testing.selenium_po.page.add_member_page import AddMemberPage
from selenium_testing.selenium_po.page.base_page import BasePage
from selenium_testing.selenium_po.page.contact_page import ContactPage


class MainPage(BasePage):
    _base_url = "https://work.weixin.qq.com/wework_admin/frame#index"

    def goto_cantact(self):
        self.find(By.ID, "menu_contacts").click()
        return ContactPage(self.driver)

    def goto_add_member_page(self):
        self.find(By.CSS_SELECTOR, ".index_service_cnt_item  .ww_indexImg_AddMember").click()
        return AddMemberPage(self.driver)
