from unittest import TestCase
from problems.N1437_Check_If_All_1_Are_At_Least_Length_K_Places_Away import Solution

class TestSolution(TestCase):
    def test_kLengthApart(self):
        nums = [1, 0, 0, 0, 1, 0, 0, 1]
        k = 2
        self.assertTrue(Solution().kLengthApart(nums, k))

    def test_kLengthApart_1(self):
        nums = [1,0,0,1,0,1]
        k = 2
        self.assertFalse(Solution().kLengthApart(nums, k))

    def test_kLengthApart_2(self):
        nums = [1,1,1,1,1]
        k = 0
        self.assertTrue(Solution().kLengthApart(nums, k))

    def test_kLengthApart_3(self):
        nums = [0,1,0,1]
        k = 1
        self.assertTrue(Solution().kLengthApart(nums, k))
