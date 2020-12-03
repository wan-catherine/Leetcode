from unittest import TestCase
from problems.N629_K_Inverse_Pairs_Array import Solution

class TestSolution(TestCase):
    def test_kInversePairs(self):
        self.assertEqual(1, Solution().kInversePairs(n = 3, k = 0))

    def test_kInversePairs_1(self):
        self.assertEqual(2, Solution().kInversePairs(n = 3, k = 1))
