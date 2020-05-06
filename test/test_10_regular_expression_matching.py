from unittest import TestCase
from problems.N10_Regular_Expression_Matching import Solution

class TestSolution(TestCase):
    def test_isMatch(self):
        self.assertEqual(False, Solution().isMatch("aa", "a"))

    def test_isMatch_1(self):
        self.assertEqual(True, Solution().isMatch("aa", "a*"))

    def test_isMatch_2(self):
        self.assertEqual(True, Solution().isMatch("aab", "c*a*b"))

    def test_isMatch_3(self):
        self.assertEqual(False, Solution().isMatch("aa", "a"))

    def test_isMatch_4(self):
        self.assertEqual(False, Solution().isMatch("mississippi", "mis*is*p*."))

    def test_isMatch_5(self):
        self.assertEqual(True, Solution().isMatch("ab", ".*"))

    def test_isMatch_6(self):
        self.assertEqual(True, Solution().isMatch("aaa", "ab*a*c*a"))

    def test_isMatch_7(self):
        self.assertEqual(False, Solution().isMatch("aab", "b.*"))
