from unittest import TestCase
from problems.N910_Smallest_Range_II import Solution

class TestSolution(TestCase):
    def test_smallestRangeII(self):
        self.assertEqual(0, Solution().smallestRangeII(A = [1], K = 0))

    def test_smallestRangeII_1(self):
        self.assertEqual(6, Solution().smallestRangeII(A = [0,10], K = 2))

    def test_smallestRangeII_2(self):
        self.assertEqual(3, Solution().smallestRangeII(A = [1,3,6], K = 3))