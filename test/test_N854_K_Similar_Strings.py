from unittest import TestCase
from problems.N854_K_Similar_Strings import Solution

class TestSolution(TestCase):
    def test_k_similarity(self):
        self.assertEqual(1, Solution().kSimilarity(s1 = "ab", s2 = "ba"))

    def test_k_similarity_1(self):
        self.assertEqual(2, Solution().kSimilarity(s1 = "abc", s2 = "bca"))
