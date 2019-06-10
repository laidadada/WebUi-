# -*- encoding:utf-8 -*-

from utils.driver.webdriver import driver
from utils.logs import debug
class PageObject():

    url = None
    page_flag_xpath = None
    page_flag_keyword = None

    def __init__(self):
        self.driver = driver
        debug("PageObject -> %s 获取当前driver的实例：" % str(self.__class__))

    def open_and_check(self):
        debug("PageObject -> %s打开并检测制定url页面")
        self.driver.get(self.url)

        return self.check_if_page_opened()


    def check_if_page_opened(self):
        flag_element = self.driver.find_element_by_xpath(self.page_flag_xpath)
        if flag_element.text == self.page_flag_keyword:
            return True
        else:
            return False
