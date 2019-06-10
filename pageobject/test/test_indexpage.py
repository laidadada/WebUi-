import unittest
from pageobject.indexpage import IndexPage

class TestIndexPage(unittest.TestCase):

    def test_open_indexpage(self):
        indexpage = IndexPage()
        self.assertTrue(indexpage.open_and_check())


if __name__ == '__main__':
    unittest.main()
