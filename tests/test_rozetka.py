import unittest
from rozetka import *
from site_ import *

class TestFindCountPagesRozetka(unittest.TestCase):
    path="test_files/"

    def test_find_count_pages_rozetka(self):
        self.assertEqual(57, find_count_pages_rozetka(Site(self.path + "rozetka_test1.html","rozetka.com.ua")))
        self.assertEqual(1, find_count_pages_rozetka(Site(self.path + "rozetka_test2.html","rozetka.com.ua")))
        self.assertEqual(3, find_count_pages_rozetka(Site(self.path + "rozetka_test3.html","rozetka.com.ua")))

if __name__ == '__main__':
    unittest.main()
