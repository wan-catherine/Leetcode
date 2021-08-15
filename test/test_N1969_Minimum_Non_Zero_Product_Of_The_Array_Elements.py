from unittest import TestCase
from problems.N1969_Minimum_Non_Zero_Product_Of_The_Array_Elements import Solution

class TestSolution(TestCase):
    def test_min_non_zero_product(self):
        self.assertEqual(1, Solution().minNonZeroProduct(1))

    def test_min_non_zero_product_1(self):
        self.assertEqual(6, Solution().minNonZeroProduct(2))

    def test_min_non_zero_product_2(self):
        self.assertEqual(1512, Solution().minNonZeroProduct(3))

