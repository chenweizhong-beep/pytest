from appium.webdriver.common.mobileby import MobileBy

from appium_testing.appium_po.addresslist_page import AddressListPage
from appium_testing.appium_po.base_page import BasePage


class MainPage(BasePage):
    def click_addresslist(self):
        ele = (MobileBy.XPATH, '//*[@text="通讯录"]')
        self.wait_for_click(ele, 10)
        self.find_and_click(ele)
        # self.driver.find_element(MobileBy.XPATH, '//*[@text="通讯录"]').click()
        return AddressListPage(self.driver)
