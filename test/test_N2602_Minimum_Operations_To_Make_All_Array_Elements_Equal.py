from unittest import TestCase
from problems.N2602_Minimum_Operations_To_Make_All_Array_Elements_Equal import Solution

class TestSolution(TestCase):
    def test_min_operations(self):
        self.assertListEqual([14,10], Solution().minOperations(nums = [3,1,6,8], queries = [1,5]))

    def test_min_operations_1(self):
        self.assertListEqual([20], Solution().minOperations(nums = [2,9,6,3], queries = [10]))
