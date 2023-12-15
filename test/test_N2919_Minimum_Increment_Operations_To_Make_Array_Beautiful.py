from unittest import TestCase
from problems.N2919_Minimum_Increment_Operations_To_Make_Array_Beautiful import Solution

class TestSolution(TestCase):
    def test_min_increment_operations(self):
        self.assertEquals(3, Solution().minIncrementOperations(nums = [2,3,0,0,2], k = 4))

    def test_min_increment_operations_1(self):
        self.assertEquals(2, Solution().minIncrementOperations(nums = [0,1,3,3], k = 5))

    def test_min_increment_operations_2(self):
        self.assertEquals(0, Solution().minIncrementOperations(nums = [1,1,2], k = 1))