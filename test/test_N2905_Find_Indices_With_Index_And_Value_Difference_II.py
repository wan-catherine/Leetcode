from unittest import TestCase
from problems.N2905_Find_Indices_With_Index_And_Value_Difference_II import Solution

class TestSolution(TestCase):
    def test_find_indices(self):
        self.assertListEqual([0,3], Solution().findIndices(nums = [5,1,4,1], indexDifference = 2, valueDifference = 4))

    def test_find_indices_1(self):
        self.assertListEqual([0,0], Solution().findIndices(nums = [2,1], indexDifference = 0, valueDifference = 0))

    def test_find_indices_2(self):
        self.assertListEqual([-1,-1], Solution().findIndices(nums = [1,2,3], indexDifference = 2, valueDifference = 4))
