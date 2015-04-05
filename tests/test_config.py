import unittest

from config import read_config

class TestReadConfig(unittest.TestCase):
    def test_read_config(self):
        self.assertDictEqual(
            read_config("test_files/config1.ini"),
            {"use_gevent":True,"levenstein_min":1,"path":"qwe/"})
        self.assertDictEqual(
            read_config("test_files/config2.ini"),
            {"use_gevent":False,"levenstein_min":3,"path":"xml/"})

if __name__ == '__main__':
    unittest.main()
