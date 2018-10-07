from unittest import TestCase
from problems.LargestRectangleHistogram import Solution

class TestSolution(TestCase):
    def test_largestRectangleArea(self):
        solution = Solution()
        res = solution.largestRectangleArea([2,1,5,6,2,3])
        self.assertEqual(10, res)
