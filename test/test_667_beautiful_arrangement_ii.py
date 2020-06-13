from unittest import TestCase
from problems.N667_Beautiful_Arrangement_II import Solution

class TestSolution(TestCase):
    def test_constructArray(self):
        self.assertListEqual([1,2,3], Solution().constructArray(3, 1))

    def test_constructArray_1(self):
        self.assertListEqual([1,3,2], Solution().constructArray(3, 2))

    def test_constructArray_2(self):
        self.assertListEqual([1,5,2,4,3], Solution().constructArray(5, 4))
