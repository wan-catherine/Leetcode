from unittest import TestCase
from problems.N2565_Subsequence_With_The_Minimum_Score import Solution

class TestSolution(TestCase):
    def test_minimum_score(self):
        self.assertEquals(1, Solution().minimumScore(s = "abacaba", t = "bzaa"))

    def test_minimum_score_1(self):
        self.assertEquals(3, Solution().minimumScore(s = "cde", t = "xyz"))
