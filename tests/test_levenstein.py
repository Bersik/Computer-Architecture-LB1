import unittest
from levenstein import levenstein

class TestLevenstein(unittest.TestCase):
    def test_levenstein(self):
        self.assertEqual(3, levenstein("asd", "wqr"))
        self.assertEqual(1, levenstein("Acer Aspire E5-731-P7U9 (NX.MP8EU.006) ", "Acer Aspire E5-731-P7U9 (NX.MP8EU.006)"))
        self.assertEqual(4, levenstein("", "Acer"))
        self.assertEqual(0, levenstein("Acer", "Acer"))
        self.assertEqual(0, levenstein("", ""))

if __name__ == '__main__':
    unittest.main()
