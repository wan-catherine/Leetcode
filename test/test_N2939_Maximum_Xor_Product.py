from unittest import TestCase
from problems.N2939_Maximum_Xor_Product import Solution

class TestSolution(TestCase):
    def test_maximum_xor_product(self):
        self.assertEquals(98, Solution().maximumXorProduct(a = 12, b = 5, n = 4))

    def test_maximum_xor_product_1(self):
        self.assertEquals(930, Solution().maximumXorProduct(a = 6, b = 7 , n = 5))

    def test_maximum_xor_product_2(self):
        self.assertEquals(12, Solution().maximumXorProduct(a = 1, b = 6, n = 3))

    def test_maximum_xor_product_3(self):
        self.assertEquals(2, Solution().maximumXorProduct(a = 0, b = 3, n = 1))
