import unittest
from site_ import Site

class TestSite(unittest.TestCase):
    def test___init__(self):
        url = "url"
        name = "name"
        site = Site(url,name)
        self.assertEquals(site.url, url)
        self.assertEquals(site.name, name)

if __name__ == '__main__':
    unittest.main()
