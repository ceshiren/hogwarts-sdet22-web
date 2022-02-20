"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""
from page_object.main_page import MainPageObject


class TestAddMember:

    def test_add_member(self):
        main = MainPageObject()
         # 1. 点击添加成员，跳转到添加成员页面
         # 2. add member 的操作
        # 3. 获取通讯录页面的成员列表（实际结果）
        mem_list = main.\
            goto_add_member_page().\
            add_member().\
            get_member_list()
        # 4 断言 实际结果也就是成员列表 是否符合预期
        assert "" in mem_list