from unittest import TestCase
from problems.N1400_Construct_K_Palindrome_Strings import Solution

class TestSolution(TestCase):
    def test_canConstruct(self):
        self.assertTrue(Solution().canConstruct(s = "annabelle", k = 2))

    def test_canConstruct_1(self):
        self.assertFalse(Solution().canConstruct(s = "leetcode", k = 3))

    def test_canConstruct_2(self):
        self.assertTrue(Solution().canConstruct(s = "true", k = 4))

    def test_canConstruct_3(self):
        self.assertTrue(Solution().canConstruct(s = "yzyzyzyzyzyzyzy", k = 2))

    def test_canConstruct_4(self):
        self.assertFalse(Solution().canConstruct(s = "cr", k = 7))

