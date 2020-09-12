from unittest import TestCase
from problems.N413_Arithmetic_Slices import Solution

class TestSolution(TestCase):
    def test_numberOfArithmeticSlices(self):
        self.assertEqual(3, Solution().numberOfArithmeticSlices([1, 2, 3, 4]))

    def test_numberOfArithmeticSlices_1(self):
        self.assertEqual(10, Solution().numberOfArithmeticSlices([1,2,3,4,5,6]))
