from unittest import TestCase
from problems.N410_Split_Array_Largest_Sum import Solution

class TestSolution(TestCase):
    def test_splitArray(self):
        self.assertEqual(18, Solution().splitArray(nums = [7,2,5,10,8], m = 2))

    def test_splitArray_1(self):
        self.assertEqual(9, Solution().splitArray(nums = [1,2,3,4,5], m = 2))

    def test_splitArray_2(self):
        self.assertEqual(4, Solution().splitArray(nums = [1,4,4], m = 3))
