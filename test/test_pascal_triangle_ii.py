from unittest import TestCase
from problems.PascalTriangleII import Solution

class TestSolution(TestCase):
    def test_getRow(self):
        solution = Solution()
        res = solution.getRow(3)
        self.assertEqual(res, [1,3,3,1])
