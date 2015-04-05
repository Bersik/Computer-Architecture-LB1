import unittest
import os

import itbox
from site_ import Site
from product import Product


class TestParse(unittest.TestCase):
    def test_parse(self):
        a = itbox.parse(
                link=Site("file://" +
                          os.path.abspath("test_files/itbox_test1.html"),
                          "itbox"))[0]
        b = Product("ASUS R515MA (R515MA-BING-SX568B)","itbox",'7099',"(R515MA-BING-SX568B)")
        self.assertEqual(a.name,b.name)
        self.assertEqual(a.id,b.id)
        self.assertEqual(a.sites,b.sites)

if __name__ == '__main__':
    unittest.main()
