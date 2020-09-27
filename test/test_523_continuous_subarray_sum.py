from unittest import TestCase
from problems.N523_Continuous_Subarray_Sum import Solution

class TestSolution(TestCase):
    def test_checkSubarraySum(self):
        self.assertTrue(Solution().checkSubarraySum([23, 2, 4, 6, 7],  k=6))

    def test_checkSubarraySum_1(self):
        self.assertTrue(Solution().checkSubarraySum([23, 2, 6, 4, 7],  k=6))

    def test_checkSubarraySum_2(self):
        self.assertFalse(Solution().checkSubarraySum([23, 2, 6, 4, 7],  k=0))

    def test_checkSubarraySum_3(self):
        self.assertTrue(Solution().checkSubarraySum([0, 0],  k=0))

    def test_checkSubarraySum_4(self):
        self.assertFalse(Solution().checkSubarraySum([0,1,0], 0))

    def test_checkSubarraySum_5(self):
        self.assertFalse(Solution().checkSubarraySum([1,0], 2))

    def test_checkSubarraySum_6(self):
        self.assertTrue(Solution().checkSubarraySum([5,0,0], 0))

    def test_checkSubarraySum_7(self):
        self.assertFalse(Solution().checkSubarraySum([23,6,9], 6))

    def test_checkSubarraySum_8(self):
        self.assertTrue(Solution().checkSubarraySum([0, 0], -1))

    def test_checkSubarraySum_9(self):
        self.assertTrue(Solution().checkSubarraySum([1,1], -1))

    def test_checkSubarraySum_10(self):
        self.assertTrue(Solution().checkSubarraySum([1,1], 2))

    def test_checkSubarraySum_11(self):
        self.assertTrue(Solution().checkSubarraySum([1,2,3], 5))
