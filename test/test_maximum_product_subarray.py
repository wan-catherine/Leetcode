from unittest import TestCase
from problems.MaximumProductSubarray import Solution

class TestSolution(TestCase):
    def test_maxProduct(self):
        solution = Solution()
        res = solution.maxProduct([2,3,-2,4])
        self.assertEqual(6, res)

    def test_maxProduct_one(self):
        solution = Solution()
        res = solution.maxProduct([-2,0,-1])
        self.assertEqual(0, res)

    def test_maxProduct_two(self):
        solution = Solution()
        res = solution.maxProduct([-2])
        self.assertEqual(-2, res)

    def test_maxProduct_three(self):
        solution = Solution()
        res = solution.maxProduct([-4, -3])
        self.assertEqual(12, res)

    def test_maxProduct_four(self):
        solution = Solution()
        res = solution.maxProduct([-4,-3,-2])
        self.assertEqual(12, res)

    def test_maxProduct_five(self):
        solution = Solution()
        res = solution.maxProduct([6,3,-10,0,2])
        self.assertEqual(18, res)

    def test_maxProduct_six(self):
        solution = Solution()
        res = solution.maxProduct([3,-2,2,0,-2,0])
        self.assertEqual(3, res)

    def test_maxProduct_seven(self):
        solution = Solution()
        res = solution.maxProduct([0,-2,0])
        self.assertEqual(0, res)
