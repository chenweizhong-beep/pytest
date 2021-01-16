from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver: WebDriver = None):
        self.driver = driver

    def find(self, locator):
        return self.driver.find_element(*locator)

    def find_and_click(self, locator):
        self.find(locator).click()

    def find_and_sendkeys(self, locator, text):
        self.find(locator).send_keys(text)

    def find_by_sroll_click(self, text):
        ele = (MobileBy.ANDROID_UIAUTOMATOR,
               'new UiScrollable(new UiSelector().'
               'scrollable(true).instance(0)).'
               'scrollIntoView(new UiSelector().'
               f'text("{text}").instance(0));')
        self.find_and_click(ele)

    def find_and_get_toast(self, locator):
        return self.find(locator).text

    def wait_for_click(self, locator, timeout):
        element: WebDriver = WebDriverWait(self.driver, timeout).until \
            (expected_conditions.element_to_be_clickable(locator))
        return element

    def wait_for_click_1(self, locator, timeout):
        element: WebDriver = WebDriverWait(self.driver, timeout).until(
            expected_conditions.presence_of_element_located(locator))
        return element
