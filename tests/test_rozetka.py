import unittest
import os

from rozetka import *
from site_ import *

class TestRozetka(unittest.TestCase):
    path=os.path.dirname(os.path.abspath(__file__))+"/test_files/"
    file_test1 ="file://" + path +"rozetka_test_1.html"
    file_test2 ="file://" + path+"rozetka_test_2.html"
    file_test3 ="file://" + path+"rozetka_test_3.html"
    def test_find_count_pages_rozetka(self):
        self.assertEqual(57, find_count_pages_rozetka(Site(self.file_test1, "rozetka")))
        self.assertEqual(2, find_count_pages_rozetka(Site(self.file_test2, "rozetka")))
        self.assertEqual(1, find_count_pages_rozetka(Site(self.file_test3, "rozetka")))

    def test_get_links_from_link(self):
        links = get_links_from_link(Site(self.file_test2,"rozetka"))
        self.assertEqual(links[0], Site(self.file_test2[:-1]+";page=1/","rozetka"))
        self.assertEqual(links[1], Site(self.file_test2[:-1]+";page=2/","rozetka"))

    def test_get_links_gevent(self):
        links = get_links_gevent([Site(self.file_test1,"rozetka"),Site(self.file_test2,"rozetka")])
        self.assertEqual(len(links),59)
        self.assertEqual(links[-1], Site(self.file_test2[:-1]+";page=2/","rozetka"))
        self.assertEqual(links[-3], Site(self.file_test1[:-1]+";page=57/","rozetka"))

    def test_get_links(self):
        links = get_links([Site(self.file_test1,"rozetka"),Site(self.file_test2,"rozetka")])
        self.assertEqual(len(links),59)
        self.assertEqual(links[-1], Site(self.file_test2[:-1]+";page=2/","rozetka"))
        self.assertEqual(links[-3], Site(self.file_test1[:-1]+";page=57/","rozetka"))

    def test_parse(self):
        a = parse(
                link=Site(self.file_test3,
                          "rozetka"))[0]
        b = Product("Dell Inspiron 3147 (I31P45NIW-25)","rozetka",'14760',"(I31P45NIW-25)")
        self.assertEqual(a,b)

if __name__ == '__main__':
    unittest.main()
