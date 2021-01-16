from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from appium_testing.appium_po.base_page import BasePage


class EditMessagePage(BasePage):
    def edit_name(self, name):
        name_value = (MobileBy.XPATH, '//*[contains(@text,"姓名")]/..//*[@resource-id="com.tencent.wework:id/au0"]')
        self.wait_for_click(name_value, 10)
        # self.driver.find_element(*name_value).send_keys('蚂蚁10')
        self.find_and_sendkeys(name_value, name)
        return self

    def edit_sex(self, sex):
        element_sex = (MobileBy.XPATH,
                       "//*[@text='性别']/..//*[@resource-id='com.tencent.wework:id/auu']")
        self.find_and_click(element_sex)
        if sex == "男":
            sex_value = (MobileBy.XPATH, '//*[@resource-id="com.tencent.wework:id/dqn"]')
            self.wait_for_click(sex_value, 10)
            self.find_and_click(sex_value)
        else:
            self_value1 = (MobileBy.XPATH, "//*[@text='女']")
            self.wait_for_click(self_value1, 10)
            self.find_and_click(self_value1)
        return self

    def edit_phone(self, phone_num):
        phone_value = (MobileBy.XPATH, '//*[@text="手机号"]')
        self.wait_for_click(phone_value, 10)
        self.find_and_sendkeys(phone_value, phone_num)
        return self

    def click_save(self):
        # self.driver.find_element(MobileBy.XPATH, '//*[@text="保存"]').click()
        save_value = (MobileBy.ID, "com.tencent.wework:id/gur")
        self.find_and_click(save_value)
        # self.find_and_click((MobileBy.ID, "com.tencent.wework:id/gur"))
        from appium_testing.appium_po.addmember_page import AddMemberPage
        return AddMemberPage(self.driver)
