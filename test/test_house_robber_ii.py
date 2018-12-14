from unittest import TestCase
from problems.HouseRobberII import Solution

class TestSolution(TestCase):
    def test_rob(self):
        solution = Solution()
        res = solution.rob([2,3,2])
        self.assertEqual(3, res)

    def test_rob_one(self):
        solution = Solution()
        res = solution.rob([1,2,3,1])
        self.assertEqual(4, res)

    def test_rob_two(self):
        solution = Solution()
        res = solution.rob([1,2])
        self.assertEqual(2, res)

    def test_rob_three(self):
        solution = Solution()
        res = solution.rob([1,2,1,1])
        self.assertEqual(3, res)

    def test_rob_four(self):
        solution = Solution()
        res = solution.rob([2,1,1,2])
        self.assertEqual(3, res)

    def test_rob_five(self):
        solution = Solution()
        res = solution.rob([1,1,1,2])
        self.assertEqual(3, res)

    def test_rob_six(self):
        solution = Solution()
        res = solution.rob([1,1,3,6,7,10,7,1,8,5,9,1,4,4,3])
        self.assertEqual(41, res)

