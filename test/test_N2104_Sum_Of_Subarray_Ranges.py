from unittest import TestCase
from problems.N2104_Sum_Of_Subarray_Ranges import Solution

class TestSolution(TestCase):
    def test_sub_array_ranges(self):
        self.assertEqual(4, Solution().subArrayRanges([1,2,3]))

    def test_sub_array_ranges_1(self):
        self.assertEqual(4, Solution().subArrayRanges([1,3,3]))

    def test_sub_array_ranges_2(self):
        self.assertEqual(59, Solution().subArrayRanges([4,-2,-3,4,1]))
