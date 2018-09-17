from unittest import TestCase
from problems.UniquePaths import Solution

class TestSolution(TestCase):
    def test_uniquePaths(self):
        solution = Solution()
        res = solution.uniquePaths(3,2)
        self.assertEqual(res, 3)

    def test_uniquePaths_7(self):
        solution = Solution()
        res = solution.uniquePaths(7,3)
        self.assertEqual(res, 28)
