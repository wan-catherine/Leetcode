from unittest import TestCase
from problems.N2835_Minimum_Operations_To_Form_Subsequence_With_Target_Sum import Solution

class TestSolution(TestCase):
    def test_min_operations(self):
        self.assertEquals(1, Solution().minOperations(nums = [1,2,8], target = 7))

    def test_min_operations_1(self):
        self.assertEquals(2, Solution().minOperations(nums = [1,32,1,2], target = 12))

    def test_min_operations_2(self):
        self.assertEquals(-1, Solution().minOperations(nums = [1,32,1], target = 35))

    def test_min_operations_3(self):
        self.assertEquals(3, Solution().minOperations(nums = [8,64,128], target = 5))
