"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""
import time

import yaml
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver


class BasePage:
    _Base_URL = ""

    def __init__(self, base_driver = None):
        if base_driver is None:
            self.driver = webdriver.Chrome()
            self.driver.implicitly_wait(3)
        else:
            self.driver:WebDriver = base_driver
        if self._Base_URL:
            self.__add_cookies()

    def find(self, by, locator=None):
        if locator:
            return self.driver.find_element(by, locator)
        else:
            return self.driver.find_element(*by)

    def quit(self):
        return self.driver.quit()

    def back_to_home_page(self):
        return self.driver.get(self._Base_URL)



    def __add_cookies(self):
        # 1. 访问企业微信主页面
        self.driver.get(self._Base_URL)
        # 2. 定义cookie，cookie信息从已经写入的cookie文件中获取
        cookie = yaml.safe_load(open("../data/cookie.yaml"))
        # 3. 植入cookie
        for c in cookie:
            self.driver.add_cookie(c)
        time.sleep(3)
        # 4.再次访问企业微信页面，发现无需扫码自动登录，而且可以多次使用
        self.driver.get(self._Base_URL)

    def execute_js(self, scripts):
        return self.driver.execute_script(scripts)


