from unittest import TestCase
from problems.N392_Is_Subsequence import Solution

class TestSolution(TestCase):
    def test_isSubsequence(self):
        s = "abc"
        t = "ahbgdc"
        self.assertTrue(Solution().isSubsequence(s, t))

    def test_isSubsequence_1(self):
        s = "axc"
        t = "ahbgdc"
        self.assertFalse(Solution().isSubsequence(s, t))