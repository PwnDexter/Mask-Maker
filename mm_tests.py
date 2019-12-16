import unittest
from mask_maker import genMask, genMiddle, getCharset

class Testing(unittest.TestCase):
    def test_gte_5(self):
        maxLen = 10
        self.assertGreater(len(genMask(maxLen)), 5)

if __name__ == '__main__':
    unittest.main()
