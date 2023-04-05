from unittest import TestCase
from problems.N1775_Equal_Sum_Arrays_With_Minimum_Number_Of_Operations import Solution

class TestSolution(TestCase):
    def test_minOperations(self):
        self.assertEqual(3, Solution().minOperations(nums1 = [1,2,3,4,5,6], nums2 = [1,1,2,2,2,2]))

    def test_minOperations_1(self):
        self.assertEqual(-1, Solution().minOperations(nums1 = [1,1,1,1,1,1,1], nums2 = [6]))

    def test_minOperations_2(self):
        self.assertEqual(3, Solution().minOperations(nums1 = [6,6], nums2 = [1]))
