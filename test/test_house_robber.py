from unittest import TestCase
from problems.HouseRobber import Solution

class TestSolution(TestCase):
    def test_rob(self):
        solution = Solution()
        res = solution.rob([1,2,3,1])
        self.assertEqual(4, res)

    def test_rob_one(self):
        solution = Solution()
        res = solution.rob([2,7,9,3,1])
        self.assertEqual(12, res)