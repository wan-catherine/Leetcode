from unittest import TestCase
from problems.N767_Reorganize_String import Solution

class TestSolution(TestCase):
    def test_reorganizeString(self):
        self.assertEqual("aba", Solution().reorganizeString("aab"))

    def test_reorganizeString_1(self):
        self.assertEqual("", Solution().reorganizeString("aaab"))

    def test_reorganizeString_2(self):
        self.assertEqual("vlvov", Solution().reorganizeString("vvvlo"))

    def test_reorganizeString_3(self):
        self.assertEqual("brbsf", Solution().reorganizeString("bfrbs"))
