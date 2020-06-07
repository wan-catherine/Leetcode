from unittest import TestCase
from problems.N327_Count_Of_Range_Sum import Solution

class TestSolution(TestCase):
    def test_countRangeSum(self):
        self.assertEqual(3, Solution().countRangeSum([-2,5,-1], -2, 2))
