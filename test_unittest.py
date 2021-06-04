import unittest
import sys
from tmp import reverse

class testCaseCube1(unittest.TestCase):
    def test_rev(self):
        self.assertEqual(reverse.rev("this is a test"),"test a is this")

if __name__ == '__main__':
    unittest.main()
