"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""
import time

from selenium.webdriver.common.by import By

from page_object.wechat_page import WechatPage


class ContactPage(WechatPage):
    _Base_URL = "https://work.weixin.qq.com/wework_admin/frame#contacts"
    def get_name_list(self):
        eles = self.driver.find_elements(By.CSS_SELECTOR, ".member_colRight_memberTable_td:nth-child(2)")
        name_list = [ele.text for ele in eles]
        return name_list

    def delete_all_members(self):
        time.sleep(3)
        self.find(By.CSS_SELECTOR, ".js_title input").click()
        # self.find(By.CSS_SELECTOR, ".js_delete").click()
        self.execute_js('document.querySelector(".js_delete").click()')
        self.find(By.CSS_SELECTOR, "[d_ck='submit']").click()
        return self
