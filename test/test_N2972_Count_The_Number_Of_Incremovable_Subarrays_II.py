from unittest import TestCase
from problems.N2972_Count_The_Number_Of_Incremovable_Subarrays_II import Solution

class TestSolution(TestCase):
    def test_incremovable_subarray_count(self):
        self.assertEqual(10, Solution().incremovableSubarrayCount([1,2,3,4]))

    def test_incremovable_subarray_count_1(self):
        self.assertEqual(7, Solution().incremovableSubarrayCount([6,5,7,8]))

    def test_incremovable_subarray_count_2(self):
        self.assertEqual(3, Solution().incremovableSubarrayCount([8,7,6,6]))
