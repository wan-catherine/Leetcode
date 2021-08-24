from unittest import TestCase
from problems.N1960_Maximum_Product_Of_The_Length_Of_Two_Palindromic_Substrings import Solution

class TestSolution(TestCase):
    def test_max_product(self):
        self.assertEqual(9, Solution().maxProduct(s = "ababbb"))

    def test_max_product_1(self):
        self.assertEqual(9, Solution().maxProduct(s = "zaaaxbbby"))
