"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""
import logging
import time

import yaml
from selenium import webdriver

# 1. 为什么会出现重复打开页面，重复实例化driver 的问题
# 答案： 其他的页面子类继承与basepage，一旦子类实例化。那么就会执行父类的构造函数
# 子类实例化自己，那么父类的构造函数就会执行几次，就会打开几次浏览器
# 解决方案：那如果无法解决构造函数要执行多次的问题，那么就考虑在父类的构造函数里面
# 添加判断，避免driver 的重复实例化。定义一个base_driver 的形参
# base_driver 代表，如果没有类在实例化的时候接收到参数，那么就实例化driver
# 如果有接收到参数，那么就传递driver，保证driver 一直存在
from selenium.webdriver.chrome.webdriver import WebDriver


class BasePage:
    """
    封装一些和业务无关的重复代码
    是某些操作的底层
    """
    def __init__(self, base_driver=None):
        if base_driver is None:
            # 实例化
            self.driver = webdriver.Chrome()
            # 添加隐式等待的配置
            self.driver.implicitly_wait(3)

        else:
            self.driver:WebDriver = base_driver


    def find(self, by, locator=None):
        """
        有可能传入 的是一个元祖(a, b)
        也有可能是传入两个参数
        :param by:
        :param locator:
        :return:
        """
        print(f"元素的定位方式为{by}， 元素的定位表达式为{locator}")
        if locator is None:
            # 如果传入元祖，那么给元祖做解包，分别传入到函数中
            return self.driver.find_element(*by)
        else:
            # 如果传入两个参数，则正常使用。
            return self.driver.find_element(by, locator)
