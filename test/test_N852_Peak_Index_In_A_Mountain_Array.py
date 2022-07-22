from unittest import TestCase
from problems.N852_Peak_Index_In_A_Mountain_Array import Solution

class TestSolution(TestCase):
    def test_peak_index_in_mountain_array(self):
        self.assertEqual(1, Solution().peakIndexInMountainArray([0,1,0]))

    def test_peak_index_in_mountain_array_1(self):
        self.assertEqual(1, Solution().peakIndexInMountainArray([0,2,1,0]))

    def test_peak_index_in_mountain_array_2(self):
        self.assertEqual(1, Solution().peakIndexInMountainArray([0,10,5,2]))
