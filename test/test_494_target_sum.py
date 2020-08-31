from unittest import TestCase
from problems.N494_Target_Sum import Solution

class TestSolution(TestCase):
    def test_findTargetSumWays(self):
        self.assertEqual(5, Solution().findTargetSumWays([1, 1, 1, 1, 1], 3))

    def test_findTargetSumWays_1(self):
        self.assertEqual(12870, Solution().findTargetSumWays([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1], 0))

    def test_findTargetSumWays_2(self):
        self.assertEqual(1048576, Solution().findTargetSumWays([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], 0))