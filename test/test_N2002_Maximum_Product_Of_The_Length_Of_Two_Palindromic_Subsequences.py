from unittest import TestCase
from problems.N2002_Maximum_Product_Of_The_Length_Of_Two_Palindromic_Subsequences import Solution

class TestSolution(TestCase):
    def test_max_product(self):
        self.assertEqual(9, Solution().maxProduct("leetcodecom"))

    def test_max_product_1(self):
        self.assertEqual(1, Solution().maxProduct("bb"))

    def test_max_product_2(self):
        self.assertEqual(25, Solution().maxProduct("accbcaxxcxx"))
