from unittest import TestCase
from problems.N2948_Make_Lexicographically_Smallest_Array_By_Swapping_Elements import Solution

class TestSolution(TestCase):
    def test_lexicographically_smallest_array(self):
        self.assertListEqual([1,3,5,8,9], Solution().lexicographicallySmallestArray(nums = [1,5,3,9,8], limit = 2))

    def test_lexicographically_smallest_array_1(self):
        self.assertListEqual([1,6,7,18,1,2], Solution().lexicographicallySmallestArray(nums = [1,7,6,18,2,1], limit = 3))

    def test_lexicographically_smallest_array_2(self):
        self.assertListEqual([1,7,28,19,10], Solution().lexicographicallySmallestArray(nums = [1,7,28,19,10], limit = 3))
