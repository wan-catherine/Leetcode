from unittest import TestCase
from problems.N2915_Length_Of_The_Longest_Subsequence_That_Sums_To_Target import Solution

class TestSolution(TestCase):
    def test_length_of_longest_subsequence(self):
        self.assertEquals(3, Solution().lengthOfLongestSubsequence(nums = [1,2,3,4,5], target = 9))

    def test_length_of_longest_subsequence_1(self):
        self.assertEquals(4, Solution().lengthOfLongestSubsequence(nums = [4,1,3,2,1,5], target = 7))

    def test_length_of_longest_subsequence_2(self):
        self.assertEquals(-1, Solution().lengthOfLongestSubsequence(nums = [1,1,5,4,5], target = 3))
