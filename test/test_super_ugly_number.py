from unittest import TestCase
from problems.SuperUglyNumber import Solution

class TestSolution(TestCase):
    def test_nthSuperUglyNumber(self):
        solution = Solution()
        res = solution.nthSuperUglyNumber(12, [2,7,13,19])
        self.assertEqual(res, 32)
