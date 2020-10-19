from unittest import TestCase
from problems.N433_Minimum_Genetic_Mutation import Solution

class TestSolution(TestCase):
    def test_minMutation(self):
        self.assertEqual(1, Solution().minMutation("AACCGGTT", "AACCGGTA", ["AACCGGTA"]))

    def test_minMutation_1(self):
        self.assertEqual(2, Solution().minMutation("AACCGGTT", "AAACGGTA", ["AACCGGTA", "AACCGCTA", "AAACGGTA"]))

    def test_minMutation_2(self):
        self.assertEqual(3, Solution().minMutation("AAAAACCC", "AACCCCCC", ["AAAACCCC", "AAACCCCC", "AACCCCCC"]))

    def test_minMutation_3(self):
        self.assertEqual(4, Solution().minMutation("AACCGGTT", "AAACGGTA", ["AACCGATT","AACCGATA","AAACGATA","AAACGGTA"]))
