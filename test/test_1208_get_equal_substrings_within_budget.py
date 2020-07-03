from unittest import TestCase
from problems.N1208_Get_Equal_Substrings_Within_Budget import Solution

class TestSolution(TestCase):
    def test_equalSubstring(self):
        self.assertEqual(3, Solution().equalSubstring("abcd", "bcdf", 3))

    def test_equalSubstring_1(self):
        self.assertEqual(1, Solution().equalSubstring("abcd", "cdef", 3))

    def test_equalSubstring_2(self):
        self.assertEqual(1, Solution().equalSubstring("abcd", "acde", 0))

    def test_equalSubstring_3(self):
        self.assertEqual(2, Solution().equalSubstring("krrgw", "zjxss", 19))

    def test_equalSubstring_4(self):
        self.assertEqual(4, Solution().equalSubstring("krpgjbjjznpzdfy", "nxargkbydxmsgby", 14))

