from unittest import TestCase
from problems.N377_Combination_Sum_IV import Solution

class TestSolution(TestCase):
    def test_combinationSum4(self):
        self.assertEqual(7, Solution().combinationSum4([1, 2, 3], 4))