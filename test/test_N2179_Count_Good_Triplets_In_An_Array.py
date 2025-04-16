from unittest import TestCase
from problems.N2179_Count_Good_Triplets_In_An_Array import Solution

class TestSolution(TestCase):
    def test_good_triplets(self):
        self.assertEquals(1, Solution().goodTriplets(nums1 = [2,0,1,3], nums2 = [0,1,2,3]))

    def test_good_triplets_1(self):
        self.assertEquals(4, Solution().goodTriplets(nums1 = [4,0,1,3,2], nums2 = [4,1,0,2,3]))
