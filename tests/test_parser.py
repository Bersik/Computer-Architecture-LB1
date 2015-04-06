import unittest
import os

from parser_ import *
from site_ import *
from product import *


class TestGetFullLinks(unittest.TestCase):
    path = os.path.dirname(os.path.abspath(__file__)) + "/test_files/"
    site1 = Site("file://" + path + "rozetka_test_1.html", "rozetka")
    site2 = Site("file://" + path + "itbox_test1.html", "itbox")
    site3 = Site("file://" + path + "rozetka_test_3.html", "rozetka")

    def test_get_full_links(self):
        links = get_full_links([self.site1, self.site2])
        self.assertEquals(len(links), 58)
        self.assertEquals(links[0], self.site2)

    def test_parse_products(self):
        prod = parse_products([self.site3])
        b = Product("Dell Inspiron 3147 (I31P45NIW-25)","rozetka",'14760',"(I31P45NIW-25)")
        self.assertEqual(prod[0],b)

    def test_parse_products_gevent(self):
        prod = parse_products_gevent([self.site3])
        b = Product("Dell Inspiron 3147 (I31P45NIW-25)","rozetka",'14760',"(I31P45NIW-25)")
        self.assertEqual(prod[0],b)

    def test_parse_link(self):
        prod1 = parse_link(self.site3)
        prod2 = parse_link(self.site2)
        b = Product("Dell Inspiron 3147 (I31P45NIW-25)","rozetka",'14760',"(I31P45NIW-25)")
        c = Product("ASUS R515MA (R515MA-BING-SX568B)","itbox",'7099',"(R515MA-BING-SX568B)")
        self.assertEqual(prod1[0], b)
        self.assertEqual(prod2[0], c)

    def test_search_list_duplicates(self):
        a = Product("Dell Inspiron 3147 (I31P45NIW-25)","rozetka",'14760',"(I31P45NIW-25)")
        b = Product("Dell Inspiron 3147 (I31P45NIW-25) Black","itbox",'13560',"(I31P45NIW-25)")
        c = Product("Dell Inspiron 3147 I31P45NIW-25","itbox",'13560', None)
        d = Product("Dell Inspiron 3147 I31P45NIW-28 Black","itbox",'13560', None)
        self.assertEquals(search_list_duplicates([a], b), 0)
        self.assertEquals(search_list_duplicates([a], c), 0)
        self.assertEquals(search_list_duplicates([a], d), None)

    def test_append_list_levenstein(self):
        prod1 = Product("Dell Inspiron 3147 (I31P45NIW-25)","rozetka",'14760',"(I31P45NIW-25)")
        prod2 = Product("Lenovo IdeaPad Z580A (59-326612)","rozetka",'18560',"(59-326612")
        prod3 = Product("Lenovo Z510 (59402573) Dark Chocolate","itbox",'13560', "(59402573)")
        prod4 = Product("LG L70 White D325","itbox",'3560', None)
        prod5 = Product("Lenovo IdeaPad Z580A (59-326612) Black","itbox",'16560',"(59-326612")
        lst1 = [prod1, prod2]
        lst2 = [prod3, prod4, prod5]
        res = [prod1, prod2, prod3, prod4]
        res[1].sites["itbox"] = "16560"
        res2 = append_list_levenstein(lst1, lst2)
        self.assertEqual(res, res2)

if __name__ == '__main__':
    unittest.main()
