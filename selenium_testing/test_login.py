from time import sleep

import yaml
from selenium import webdriver

# 先打开复用模式 chrome --remote-debugging-port=9222
from selenium.webdriver.common.by import By


def test_get_cookie():
    opt = webdriver.ChromeOptions()
    opt.debugger_address = "127.0.0.1:9222"
    driver = webdriver.Chrome(options=opt)
    driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
    driver.implicitly_wait(10)
    cookies = driver.get_cookies()
    with open('data.yml', 'w', encoding='utf-8') as f:
        yaml.safe_dump(cookies, f)


class TestLogin:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

    def teardown(self):
        self.driver.quit()

    def test_login(self):
        self.driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx")
        with open('data.yml', encoding='utf-8') as f:
            datas = yaml.safe_load(f)
        for cookie in datas:
            self.driver.add_cookie(cookie)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_xpath('//*[@id="_hmt_click"]/div[1]/div[4]/div[2]/a[1]/div/span[2]').click()
        self.driver.find_element_by_id('username').send_keys("吴芳")
        self.driver.find_element_by_id("memberAdd_english_name").send_keys('芳芳')
        self.driver.find_element_by_id("memberAdd_acctid").send_keys("1842375247")
        self.driver.find_element_by_name("gender").click()
        self.driver.find_element_by_id("memberAdd_phone").send_keys("15894142031")
        self.driver.find_element_by_id("memberAdd_telephone").send_keys("0999-3339020")
        self.driver.find_element_by_id("memberAdd_mail").send_keys("1842375247@qq.com")
        self.driver.find_element_by_id("memberEdit_address").send_keys("澳大利亚")
        self.driver.find_element_by_id("memberAdd_title").send_keys("执行官")
        self.driver.find_element_by_name("sendInvite").click()
        self.driver.find_element_by_link_text("保存").click()
        sleep(3)