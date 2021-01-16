from appium.webdriver.common.mobileby import MobileBy
from appium_testing.appium_po.base_page import BasePage
from appium_testing.appium_po.editmessage_page import EditMessagePage


class AddMemberPage(BasePage):
    def add_hand_movement(self):
        search_value = (MobileBy.XPATH, '//*[@text="手动输入添加"]')
        self.wait_for_click(search_value, 10)
        self.find_and_click(search_value)
        return EditMessagePage(self.driver)

    def get_toast(self):
        toast_value = (MobileBy.XPATH, "//*[@class='android.widget.Toast']")
        # WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located(toast_value))
        # print(self.driver.page_source)
        # toast_value_1 = self.driver.find_element(*toast_value).text
        # # mytoast = (MobileBy.XPATH, "//*[@class='android.widget.Toast']")
        # # self.find_and_get_toast(mytoast)
        self.wait_for_click_1(toast_value, 10)
        tosttext = self.find_and_get_toast(toast_value)
        print(tosttext)
        return tosttext
