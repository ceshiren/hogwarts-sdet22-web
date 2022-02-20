"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""
from selenium.webdriver.common.by import By

from page_object.contact_page import ContactPage
from page_object.wechat_page import WechatPage


class AddMemberPage(WechatPage):

    def add_member(self):
        self.find(By.ID, "username").send_keys("timo11")
        self.find(By.ID, "memberAdd_acctid").send_keys("111233")
        self.find(By.ID, "memberAdd_phone").send_keys("13030001111")
        self.find(By.CSS_SELECTOR, ".js_btn_save").click()
        return ContactPage(self.driver)

    def cancel_add_member(self):
        self.driver.find_element(By.CSS_SELECTOR, ".js_btn_cancel").click()
        return ContactPage(self.driver)