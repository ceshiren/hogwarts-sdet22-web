"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""
from page_object.main_page import MainPage


class TestAddMember:

    def setup_class(self):
        # 数据清理
        # 用例执行之前的数据清理
        self.main = MainPage()

    def teardown_class(self):
        self.main.driver.quit()

    def setup(self):
        self.add_member = self.main.goto_add_member()

    def teardown(self):
        # 返回首页
        self.main.back_to_home_page()

    def test_add_member(self):
        # 添加成员正向用例
        self.add_member.add_member().get_name_list()
        assert True

    def test_add_member_cancel(self):
        # 取消添加成员
        self.add_member.cancel_add_member().get_name_list()
        assert True
