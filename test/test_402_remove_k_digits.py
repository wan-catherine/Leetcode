from unittest import TestCase
from problems.N402_Remove_K_Digits import Solution

class TestSolution(TestCase):
    def test_removeKdigits(self):
        self.assertEqual("1219", Solution().removeKdigits("1432219", 3))

    def test_removeKdigits_1(self):
        self.assertEqual("200", Solution().removeKdigits("10200", 1))

    def test_removeKdigits_2(self):
        self.assertEqual("0", Solution().removeKdigits("10", 2))

    def test_removeKdigits_3(self):
        self.assertEqual("0", Solution().removeKdigits("1234567890",9))

    def test_removeKdigits_4(self):
        self.assertEqual("0", Solution().removeKdigits("9",1))
