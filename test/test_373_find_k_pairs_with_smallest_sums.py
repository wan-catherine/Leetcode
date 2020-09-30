from unittest import TestCase
from problems.N373_Find_K_Pairs_With_Smallest_Sums import Solution

class TestSolution(TestCase):
    def test_kSmallestPairs(self):
        self.assertListEqual([[1,2],[1,4],[1,6]], Solution().kSmallestPairs(nums1 = [1,7,11], nums2 = [2,4,6], k = 3))

    def test_kSmallestPairs_1(self):
        self.assertListEqual([1,1],[1,1], Solution().kSmallestPairs(nums1 = [1,1,2], nums2 = [1,2,3], k = 2))

    def test_kSmallestPairs_2(self):
        self.assertListEqual([1,3],[2,3], Solution().kSmallestPairs(nums1 = [1,2], nums2 = [3], k = 3))
