from unittest import TestCase
from .Longest_Subarray_Of_1_After_Deleting_One_Element import Solution

class TestSolution(TestCase):
    def test_longestSubarray(self):
        self.assertEqual(3, Solution().longestSubarray([1,1,0,1]))

    def test_longestSubarray_1(self):
        self.assertEqual(5, Solution().longestSubarray([0,1,1,1,0,1,1,0,1]))

    def test_longestSubarray_2(self):
        self.assertEqual(2, Solution().longestSubarray([1,1,1]))

    def test_longestSubarray_3(self):
        self.assertEqual(4, Solution().longestSubarray([1,1,0,0,1,1,1,0,1]))

    def test_longestSubarray_4(self):
        self.assertEqual(0, Solution().longestSubarray([0,0,0]))

    def test_longestSubarray_5(self):
        self.assertEqual(1, Solution().longestSubarray([1,0,0,0,0]))

    def test_longestSubarray_6(self):
        self.assertEqual(2, Solution().longestSubarray([0,0,1,1]))

    def test_longestSubarray_7(self):
        self.assertEqual(14, Solution().longestSubarray([1,0,0,1,1,1,1,1,0,0,0,0,0,0,1,1,1,0,1,1,1,1,1,0,1,1,1,1,1,1,1,1,0,1,1,0,0,0,1,1,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,1,1,1,1,0,1,1]))

