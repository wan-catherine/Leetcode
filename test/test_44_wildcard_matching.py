from unittest import TestCase
from problems.N44_Wildcard_Matching import Solution

class TestSolution(TestCase):
    def test_isMatch(self):
        self.assertFalse(Solution().isMatch(s = "aa", p = "a"))

    def test_isMatch_1(self):
        self.assertTrue(Solution().isMatch(s = "aa", p = "*"))

    def test_isMatch_2(self):
        self.assertFalse(Solution().isMatch(s = "cb", p = "?a"))

    def test_isMatch_3(self):
        self.assertTrue(Solution().isMatch(s = "adceb", p = "*a*b"))

    def test_isMatch_4(self):
        self.assertFalse(Solution().isMatch(s = "acdcb", p = "a*c?b"))

