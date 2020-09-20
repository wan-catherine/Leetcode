from unittest import TestCase
from problems.N1590_Make_Sum_Divisible_By_P import Solution

class TestSolution(TestCase):
    def test_minSubarray(self):
        self.assertEqual(1, Solution().minSubarray(nums = [3,1,4,2], p = 6))

    def test_minSubarray_1(self):
        self.assertEqual(2, Solution().minSubarray(nums = [6,3,5,2], p = 9))

    def test_minSubarray_2(self):
        self.assertEqual(0, Solution().minSubarray(nums = [1,2,3], p = 3))

    def test_minSubarray_3(self):
        self.assertEqual(-1, Solution().minSubarray(nums = [1,2,3], p = 7))

    def test_minSubarray_4(self):
        self.assertEqual(0, Solution().minSubarray(nums = [1000000000,1000000000,1000000000], p = 3))
