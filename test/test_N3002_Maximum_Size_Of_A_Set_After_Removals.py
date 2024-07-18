from unittest import TestCase
from problems.N3002_Maximum_Size_Of_A_Set_After_Removals import Solution

class TestSolution(TestCase):
    def test_maximum_set_size(self):
        self.assertEquals(2, Solution().maximumSetSize(nums1 = [1,2,1,2], nums2 = [1,1,1,1]))

    def test_maximum_set_size_1(self):
        self.assertEquals(5, Solution().maximumSetSize(nums1 = [1,2,3,4,5,6], nums2 = [2,3,2,3,2,3]))

    def test_maximum_set_size_2(self):
        self.assertEquals(6, Solution().maximumSetSize(nums1 = [1,1,2,2,3,3], nums2 = [4,4,5,5,6,6]))

    def test_maximum_set_size_3(self):
        self.assertEquals(2, Solution().maximumSetSize(nums1 = [8,9], nums2 = [4,3]))

    def test_maximum_set_size_4(self):
        self.assertEquals(9, Solution().maximumSetSize(nums1 = [7,1,5,4,2,5,7,2,10,9], nums2 = [8,2,4,1,4,5,9,9,6,6]))

    def test_maximum_set_size_5(self):
        self.assertEquals(4, Solution().maximumSetSize(nums1 = [10,8,7,9], nums2 = [7,9,9,5]))

    def test_maximum_set_size_6(self):
        self.assertEquals(9, Solution().maximumSetSize(nums1 = [3,1,2,3,7,10,10,6,3,10], nums2 = [9,7,1,9,5,3,2,4,5,5]))


