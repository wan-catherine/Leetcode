from unittest import TestCase
from problems.N97_Interleaving_String import Solution

class TestSolution(TestCase):
    def test_isInterleave(self):
        self.assertTrue(Solution().isInterleave(s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"))

    def test_isInterleave_1(self):
        self.assertFalse(Solution().isInterleave(s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"))

    def test_isInterleave_2(self):
        self.assertTrue(Solution().isInterleave(s1 = "", s2 = "", s3 = ""))

    def test_isInterleave_3(self):
        self.assertTrue(Solution().isInterleave("aabc", "abad", "aabadabc"))
