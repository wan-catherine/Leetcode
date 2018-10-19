from unittest import TestCase
from problems.UniqueBinarySearchTrees import Solution

class TestSolution(TestCase):
    def test_numTrees(self):
        solution = Solution()
        res = solution.numTrees(3)
        self.assertEqual(res, 5)

    def test_numTrees_one(self):
        solution = Solution()
        res = solution.numTrees(4)
        self.assertEqual(res, 14)
