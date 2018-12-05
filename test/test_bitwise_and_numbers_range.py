from unittest import TestCase
from problems.BitwiseAndNumbersRange import Solution

class TestSolution(TestCase):
    def test_rangeBitwiseAnd(self):
        solution = Solution()
        res = solution.rangeBitwiseAnd(5,7)
        self.assertEqual(4, res)

    def test_rangeBitwiseAnd_one(self):
        solution = Solution()
        res = solution.rangeBitwiseAnd(0,1)
        self.assertEqual(0, res)
