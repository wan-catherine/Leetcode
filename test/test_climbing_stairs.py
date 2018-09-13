from unittest import TestCase
from problems.ClimbingStairs import Solution

class TestSolution(TestCase):
    def test_climbStairs(self):
        solution = Solution()
        res = solution.climbStairs(3)
        self.assertEqual(3, res)

    def test_climbStairs_1(self):
        solution = Solution()
        res = solution.climbStairs(1)
        self.assertEqual(1, res)
