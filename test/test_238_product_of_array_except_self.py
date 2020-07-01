from unittest import TestCase
from problems.N238_Product_Of_Array_Except_Self import Solution

class TestSolution(TestCase):
    def test_productExceptSelf(self):
        input = [1,2,3,4]
        output = [24,12,8,6]
        self.assertListEqual(output, Solution().productExceptSelf(input))
