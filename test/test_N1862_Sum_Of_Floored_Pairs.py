from unittest import TestCase
from problems.N1862_Sum_Of_Floored_Pairs import Solution

class TestSolution(TestCase):
    def test_sum_of_floored_pairs(self):
        self.assertEqual(10, Solution().sumOfFlooredPairs([2,5,9]))

    def test_sum_of_floored_pairs_1(self):
        self.assertEqual(49, Solution().sumOfFlooredPairs([7,7,7,7,7,7,7]))
