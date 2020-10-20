from unittest import TestCase
from problems.N633_Sum_Of_Square_Numbers import Solution

class TestSolution(TestCase):
    def test_judgeSquareSum(self):
        self.assertTrue(Solution().judgeSquareSum(5))

    def test_judgeSquareSum_1(self):
        self.assertFalse(Solution().judgeSquareSum(3))

    def test_judgeSquareSum_2(self):
        self.assertTrue(Solution().judgeSquareSum(4))

    def test_judgeSquareSum_3(self):
        self.assertTrue(Solution().judgeSquareSum(2))

    def test_judgeSquareSum_4(self):
        self.assertTrue(Solution().judgeSquareSum(1))

