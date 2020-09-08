from unittest import TestCase
from problems.N241_Different_Ways_To_Add_Parentheses import Solution

class TestSolution(TestCase):
    def test_diffWaysToCompute(self):
        self.assertListEqual([0, 2], Solution().diffWaysToCompute("2-1-1"))

    def test_diffWaysToCompute_1(self):
        self.assertListEqual([-34, -14, -10, -10, 10], Solution().diffWaysToCompute("2*3-4*5"))
