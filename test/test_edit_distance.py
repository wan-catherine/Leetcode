from unittest import TestCase
from problems.EditDistance import Solution

class TestSolution(TestCase):
    def test_minDistance(self):
        solution = Solution()
        res = solution.minDistance("horse", "ros")
        self.assertEqual(res, 3)

    def test_minDistance_one(self):
        solution = Solution()
        res = solution.minDistance("intention", "execution")
        self.assertEqual(res, 5)

    def test_minDistance_two(self):
        solution = Solution()
        res = solution.minDistance("zoologicoarchaeologist", "zoogeologist")
        self.assertEqual(res, 10)

    def test_minDistance_three(self):
        solution = Solution()
        res = solution.minDistance("pneumonoultramicroscopicsilicovolcanoconiosis", "ultramicroscopically")
        self.assertEqual(res, 27)
