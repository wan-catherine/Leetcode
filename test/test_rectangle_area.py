from unittest import TestCase
from problems.RectangleArea import Solution

class TestSolution(TestCase):
    def test_computeArea(self):
        solution = Solution()
        res = solution.computeArea(-3, 0, 3, 4, 0, -1, 9, 2)
        self.assertEqual(45, res)
