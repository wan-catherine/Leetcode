from unittest import TestCase
from problems.N2811_Check_If_It_Is_Possible_To_Split_Array import Solution

class TestSolution(TestCase):
    def test_can_split_array(self):
        self.assertTrue(Solution().canSplitArray(nums = [2, 2, 1], m = 4))

    def test_can_split_array_1(self):
        self.assertFalse(Solution().canSplitArray(nums = [2, 1, 3], m = 5 ))

    def test_can_split_array_2(self):
        self.assertTrue(Solution().canSplitArray(nums = [2, 3, 3, 2, 3], m = 6))
