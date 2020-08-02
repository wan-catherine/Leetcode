from unittest import TestCase
from problems.N1537_Get_The_Maximum_Score import Solution

class TestSolution(TestCase):
    def test_maxSum(self):
        self.assertEqual(30, Solution().maxSum(nums1 = [2,4,5,8,10], nums2 = [4,6,8,9]))

    def test_maxSum_1(self):
        self.assertEqual(109, Solution().maxSum(nums1 = [1,3,5,7,9], nums2 = [3,5,100]))

    def test_maxSum_2(self):
        self.assertEqual(40, Solution().maxSum(nums1 = [1,2,3,4,5], nums2 = [6,7,8,9,10]))

    def test_maxSum_3(self):
        self.assertEqual(61, Solution().maxSum(nums1 = [1,4,5,8,9,11,19], nums2 = [2,3,4,11,12]))

    def test_maxSum_4(self):
        self.assertEqual(137, Solution().maxSum(nums1 =  [1, 5, 9, 15, 22, 28], nums2 = [7, 11, 15, 17, 25, 29, 33]))
