from appium import webdriver

from appium_testing.appium_po.base_page import BasePage
from appium_testing.appium_po.main_page import MainPage


class AppPage(BasePage):
    def start(self):
        if self.driver == None:

            caps = {}
            caps['platformName'] = 'Android'
            caps['deviceName'] = '127.0.0.1:7555'
            caps['platformVersion'] = '6.0'
            caps['appPackage'] = 'com.tencent.wework'
            caps['appActivity'] = '.launch.WwMainActivity'
            caps['noReset'] = 'true'
            # caps['unicodeKeyBoard'] = 'true'
            # caps['resetKeyBoard'] = 'true'
            # caps['settings[waitForIdleTimeout]'] = 0  # 消除动态页面等待时间
            # caps['automationName'] = 'uiautomator2'
            self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', caps)
        else:
            self.driver.launch_app()
        return self

    def stop(self):
        self.driver.quit()

    def restart(self):
        self.driver.close_app()
        self.driver.launch_app()

    def goto_main_page(self):
        return MainPage(self.driver)
