from unittest import TestCase
from problems.N1092_Shortest_Common_Supersequence import Solution

class TestSolution(TestCase):
    def test_shortest_common_supersequence(self):
        self.assertEquals("cabac", Solution().shortestCommonSupersequence(str1 = "abac", str2 = "cab"))

    def test_shortest_common_supersequence_1(self):
        self.assertEquals("aaaaaaaa", Solution().shortestCommonSupersequence(str1 = "aaaaaaaa", str2 = "aaaaaaaa"))
