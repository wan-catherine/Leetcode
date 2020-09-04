from unittest import TestCase
from problems.N1156_Swap_For_Longest_Repeated_Character_Substring import Solution

class TestSolution(TestCase):
    def test_maxRepOpt1(self):
        self.assertEqual(3, Solution().maxRepOpt1("ababa"))

    def test_maxRepOpt1_1(self):
        self.assertEqual(6, Solution().maxRepOpt1("aaabaaa"))

    def test_maxRepOpt1_2(self):
        self.assertEqual(4, Solution().maxRepOpt1("aaabbaaa"))

    def test_maxRepOpt1_3(self):
        self.assertEqual(5, Solution().maxRepOpt1("aaaaa"))

    def test_maxRepOpt1_4(self):
        self.assertEqual(1, Solution().maxRepOpt1("abcdef"))
