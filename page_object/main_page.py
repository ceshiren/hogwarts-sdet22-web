"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""
from page_object.add_member_page import AddMemberPage
from page_object.contact_page import ContactPage


class MainPageObject:
    # 跳转通讯录页面的功能
    def goto_contact_page(self):
        return ContactPage()

    # 跳转添加成员页面的功能
    def goto_add_member_page(self):
        return AddMemberPage()

