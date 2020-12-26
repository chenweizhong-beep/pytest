import time
from selenium.webdriver.common.by import By

from selenium_testing.selenium_po.page.base_page import BasePage


class ContactPage(BasePage):
    def click_add_member(self):
        from selenium_testing.selenium_po.page.add_member_page import AddMemberPage
        ele = (By.CSS_SELECTOR, ".ww_operationBar .js_add_member")
        # WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(ele))
        self.wait_for_click(ele, 10)
        while True:
            self.find(By.CSS_SELECTOR, ".ww_operationBar .js_add_member").click()
            element = self.finds(By.ID, "username")
            if len(element) > 0:
                break
        return AddMemberPage(self.driver)

    def get_member(self):
        time.sleep(1)
        name_list = []
        elements = self.finds(By.CSS_SELECTOR, ".member_colRight_memberTable_td:nth-child(2)")
        for value in elements:
            print(value.get_attribute("title"))
            name_list.append(value.get_attribute("title"))
        return name_list
