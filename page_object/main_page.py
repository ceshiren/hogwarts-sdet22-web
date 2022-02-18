"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""
from selenium.webdriver.common.by import By

from page_object.add_member_page import AddMemberPage
from page_object.base_page import BasePage


class MainPage(BasePage):
    _Base_URL = "https://work.weixin.qq.com/wework_admin/frame#index"
    _GOTO_ADD_MEMBER = ".ww_indexImg_AddMember"

    def goto_add_member(self):
        self.driver.find_element(By.CSS_SELECTOR, self._GOTO_ADD_MEMBER).click()
        return AddMemberPage(self.driver)

    @classmethod
    def get_base_url(cls):
        return cls._Base_URL