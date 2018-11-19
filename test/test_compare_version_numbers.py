from unittest import TestCase
from problems.CompareVersionNumbers import Solution

class TestSolution(TestCase):
    def test_compareVersion(self):
        solution = Solution()
        res = solution.compareVersion("0.1", "1.1")
        self.assertEqual(-1, res)

    def test_compareVersion_one(self):
        solution = Solution()
        res = solution.compareVersion("1.0.1", "1")
        self.assertEqual(1, res)

    def test_compareVersion_two(self):
        solution = Solution()
        res = solution.compareVersion("7.5.2.4", "7.5.3")
        self.assertEqual(-1, res)
