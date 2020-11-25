from unittest import TestCase
from problems.N1015_Smallest_Integer_Divisible_By_K import Solution

class TestSolution(TestCase):
    def test_smallestRepunitDivByK(self):
        self.assertEqual(1, Solution().smallestRepunitDivByK(1))

    def test_smallestRepunitDivByK_1(self):
        self.assertEqual(-1, Solution().smallestRepunitDivByK(2))

    def test_smallestRepunitDivByK_2(self):
        self.assertEqual(3, Solution().smallestRepunitDivByK(3))
