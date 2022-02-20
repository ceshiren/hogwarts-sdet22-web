"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""
from page_object.contact_page import ContactPage


class AddMemberPage:
    def add_member(self):
        """
        添加成员功能
        ，添加成功后返回通讯录页面
        """
        return ContactPage()
