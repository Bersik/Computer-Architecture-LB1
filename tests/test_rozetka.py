import unittest
from rozetka import *
from site_ import *

class TestFindCountPagesRozetka(unittest.TestCase):
    path="test_files/"

    def test_find_count_pages_rozetka(self):
        self.assertEqual(57, find_count_pages_rozetka(Site(self.path + "rozetka_test1.html","rozetka.com.ua")))
        self.assertEqual(1, find_count_pages_rozetka(Site(self.path + "rozetka_test2.html","rozetka.com.ua")))
        self.assertEqual(3, find_count_pages_rozetka(Site(self.path + "rozetka_test3.html","rozetka.com.ua")))

class TestGetLinksFromLink(unittest.TestCase):
    def test_get_links_from_link(self):
        # self.assertEqual(expected, get_links_from_link(link))
        assert False # TODO: implement your test here

class TestGetLinks(unittest.TestCase):
    def test_get_links(self):
        # self.assertEqual(expected, get_links(links))
        assert False # TODO: implement your test here

class TestGetLinksGevent(unittest.TestCase):
    def test_get_links_gevent(self):
        # self.assertEqual(expected, get_links_gevent(links))
        assert False # TODO: implement your test here

if __name__ == '__main__':
    unittest.main()
