from unittest import TestCase
from problems.N446_Arithmetic_Slices_ii_Subsequence import Solution

class TestSolution(TestCase):
    def test_number_of_arithmetic_slices(self):
        self.assertEqual(7, Solution().numberOfArithmeticSlices([2,4,6,8,10]))

    def test_number_of_arithmetic_slices_1(self):
        self.assertEqual(16, Solution().numberOfArithmeticSlices([7,7,7,7,7]))
