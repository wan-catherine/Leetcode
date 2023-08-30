from unittest import TestCase
from problems.N2809_Minimum_Time_To_Make_Array_Sum_At_Most_X import Solution

class TestSolution(TestCase):
    def test_minimum_time(self):
        self.assertEquals(3, Solution().minimumTime(nums1 = [1,2,3], nums2 = [1,2,3], x = 4))

    def test_minimum_time_1(self):
        self.assertEquals(-1, Solution().minimumTime(nums1 = [1,2,3], nums2 = [3,3,3], x = 4))
