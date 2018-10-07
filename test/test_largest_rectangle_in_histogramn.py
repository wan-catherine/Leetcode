from unittest import TestCase
from problems.LargestRectangleHistogram import Solution

class TestSolution(TestCase):
    def test_largestRectangleArea(self):
        solution = Solution()
        res = solution.largestRectangleArea([2,1,5,6,2,3])
        self.assertEqual(10, res)

    def test_largestRectangleArea_zero(self):
        solution = Solution()
        res = solution.largestRectangleArea([0])
        self.assertEqual(0, res)

    def test_largestRectangleArea_special(self):
        solution = Solution()
        res = solution.largestRectangleArea([2,1,2])
        self.assertEqual(3, res)

    def test_largestRectangleArea_1(self):
        solution = Solution()
        res = solution.largestRectangleArea([4,2,0,3,2,5])
        self.assertEqual(6, res)
