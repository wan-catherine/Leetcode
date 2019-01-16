from unittest import TestCase
from problems.AddDigits import Solution

class TestSolution(TestCase):
    def test_addDigits(self):
        solution = Solution()
        res = solution.addDigits(38)
        self.assertEqual(res, 2)
