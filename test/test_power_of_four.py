from unittest import TestCase
from problems.PowerFour import Solution

class TestSolution(TestCase):
    def test_isPowerOfFour(self):
        solution = Solution()
        res = solution.isPowerOfFour(16)
        self.assertEqual(res, True)

    def test_isPowerOfFour_one(self):
        solution = Solution()
        res = solution.isPowerOfFour(5)
        self.assertEqual(res, False)

