import unittest

from utils.driver.pageobject import PageObject


class TestPageObjec(unittest.TestCase):

    def test_int_pageobject(self):
        url = "http://www.baidu.com"
        PageObject().open_and_check(url)



if __name__ == '__main__':
    unittest.main()
