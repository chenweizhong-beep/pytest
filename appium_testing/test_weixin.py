import allure
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


@allure.feature('添加企业微信成员')
class TestWeixin():
    def setup(self):
        caps = {}
        caps['platformName'] = 'Android'
        caps['deviceName'] = '127.0.0.1:7555'
        caps['platformVersion'] = '6.0'
        caps['appPackage'] = 'com.tencent.wework'
        caps['appActivity'] = '.launch.WwMainActivity'
        caps['noReset'] = 'true'
        caps['unicodeKeyBoard'] = 'true'
        caps['resetKeyBoard'] = 'true'
        # caps['settings[waitForIdleTimeout]'] = 0  # 消除动态页面等待时间
        caps['automationName'] = 'uiautomator2'
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', caps)

    def teardown(self):

        self.driver.quit()

    # @pytest.mark.parametrize('name, phonenumber', data, ids=name)
    @allure.feature('添加功能')
    def test_weixin(self, add_names):
        with allure.step('点击通讯录'):
            self.driver.find_element(MobileBy.XPATH, '//*[@text="通讯录"]').click()
        self.driver.find_element_by_android_uiautomator('new UiScrollable(new UiSelector().'
                                                        'scrollable(true).instance(0)).'
                                                        'scrollIntoView(new UiSelector().text("添加成员").'
                                                        'instance(0));').click()
        # sleep(2)
        search_value = (MobileBy.XPATH, '//*[@text="手动输入添加"]')
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(search_value))
        self.driver.find_element(*search_value).click()
        # sleep(5)
        name_value = (MobileBy.XPATH, '//*[contains(@text,"姓名")]/..//*[@resource-id="com.tencent.wework:id/au0"]')
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(name_value))
        self.driver.find_element(*name_value).send_keys(add_names[0])
        self.driver.find_element(MobileBy.XPATH,
                                 "//*[@text='性别']/..//*[@resource-id='com.tencent.wework:id/auu']").click()
        sex_value = (MobileBy.XPATH, '//*[@resource-id="com.tencent.wework:id/dqn"]')
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(sex_value))
        self.driver.find_element(*sex_value).click()
        phone_value = (MobileBy.XPATH, '//*[@text="手机号"]')
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(phone_value))
        self.driver.find_element(*phone_value).send_keys(add_names[1])
        with allure.step('点击保存按钮'):
            self.driver.find_element(MobileBy.XPATH, '//*[@text="保存"]').click()
        toast_value = (By.XPATH, "//*[@class='android.widget.Toast']")
        WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located(toast_value))
        toast_value_1 = self.driver.find_element(*toast_value).text
        print(toast_value_1)
        assert toast_value_1 == '添加成功'
