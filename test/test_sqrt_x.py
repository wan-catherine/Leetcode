from unittest import TestCase
from problems.SqrtX import Solution

class TestSolution(TestCase):
    def test_mySqrt(self):
        solution = Solution()
        res = solution.mySqrt(4)
        self.assertEqual(res, 2)

    def test_mySqrt_8(self):
        solution = Solution()
        res = solution.mySqrt(8)
        self.assertEqual(res, 2)
