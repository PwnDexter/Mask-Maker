import unittest
from mask_maker import genMask, genMiddle, getCharset

class Testing(unittest.TestCase):
    def test_mask_len_gte_5(self):
        maxLen = 10
        self.assertGreater(len(genMask(maxLen)), 5)
    
    def test_gen_middle_length(self):
        num_charsets = 5
        middle = genMiddle(num_charsets)
        self.assertEqual(len(middle), num_charsets * 2)  # Each charset is 2 characters.

if __name__ == '__main__':
    unittest.main()
