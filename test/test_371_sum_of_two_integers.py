from unittest import TestCase
from problems.N371_Sum_Of_Two_Integers import Solution

class TestSolution(TestCase):
    def test_getSum(self):
        self.assertEqual(3, Solution().getSum(1, 2))

    def test_getSum_0(self):
        self.assertEqual(5, Solution().getSum(2, 3))

    def test_getSum_1(self):
        self.assertEqual(1, Solution().getSum(-2, 3))

    def test_getSum_2(self):
        self.assertEqual(-20, Solution().getSum(-12, -8))