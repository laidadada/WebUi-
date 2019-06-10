# -*- encoding:utf-8 -*-
from utils.driver.pageobject import PageObject
from pageobject.urls import INDEX_PAGE_URL


class IndexPage(PageObject):
    url = INDEX_PAGE_URL
    page_flag_xpath = "//div[@class='col-md-8']/div[1]/div[1]"
    page_flag_keyword = u'最新签到用户'