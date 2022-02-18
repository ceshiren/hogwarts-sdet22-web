"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""
from page_object.main_page import MainPage


class WechatPage:
    """
    企业微信业务相关
    1. 登录
    2. 回到子页面首页
    3.
    """
    _contact_url = ""
    # _Base_URL = ""
    #
    #
    # def __init__(self):
    #    if self._Base_URL:
    #         self.__add_cookies()
    #
    def goto_default_page(self):
        """
        访问子类的url
        :return:
        """
        self.driver.get(self._Base_URL)

    def goto_main(self):
        self.driver.get(MainPage.get_base_url())


    #
    # def __add_cookies(self):
    #     # 1. 访问企业微信主页面
    #     self.driver.get(self._Base_URL)
    #     # 2. 定义cookie，cookie信息从已经写入的cookie文件中获取
    #     cookie = yaml.safe_load(open("../data/cookie.yaml"))
    #     # 3. 植入cookie
    #     for c in cookie:
    #         self.driver.add_cookie(c)
    #     time.sleep(3)
    #     # 4.再次访问企业微信页面，发现无需扫码自动登录，而且可以多次使用
    #     self.driver.get(self._Base_URL)
    #


