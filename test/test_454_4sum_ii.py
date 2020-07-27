from unittest import TestCase
from problems.N454_4Sum_II import Solution

class TestSolution(TestCase):
    def test_fourSumCount(self):
        A = [1, 2]
        B = [-2, -1]
        C = [-1, 2]
        D = [0, 2]
        self.assertEqual(2, Solution().fourSumCount(A, B, C, D))

    def test_fourSumCount_1(self):
        A = [0, 1, -1]
        B = [-1, 1, 0]
        C = [0, 0, 1]
        D = [-1, 1, 1]
        self.assertEqual(17, Solution().fourSumCount(A, B, C, D))
