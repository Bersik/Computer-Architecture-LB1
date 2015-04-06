import unittest
from url_work import *
from urllib2 import URLError

class TestGetHtml(unittest.TestCase):
    def test_get_html(self):
        with self.assertRaises(URLError):
            get_html("https://weregfdgfdg.com/")
        with self.assertRaises(ValueError):
            get_html("werewr")

if __name__ == '__main__':
    unittest.main()
