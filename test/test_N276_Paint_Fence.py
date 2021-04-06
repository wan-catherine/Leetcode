from unittest import TestCase
from problems.N276_Paint_Fence import Solution

class TestSolution(TestCase):
    def test_num_ways(self):
        self.assertEqual(6, Solution().numWays(n = 3, k = 2))

    def test_num_ways_1(self):
        self.assertEqual(1, Solution().numWays(n = 1, k = 1))

    def test_num_ways_2(self):
        self.assertEqual(42, Solution().numWays(n = 7, k = 2))