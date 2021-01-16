from appium_testing.appium_po.addmember_page import AddMemberPage
from appium_testing.appium_po.base_page import BasePage


class AddressListPage(BasePage):
    def slip_click(self):
        # self.driver.find_element_by_android_uiautomator('new UiScrollable(new UiSelector().'
        #                                                 'scrollable(true).instance(0)).'
        #                                                 'scrollIntoView(new UiSelector().text("添加成员").'
        #                                                 'instance(0));').click()
        self.find_by_sroll_click('添加成员')
        return AddMemberPage(self.driver)