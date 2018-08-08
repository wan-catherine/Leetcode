from unittest import TestCase
from problems.LongestSubstringWithoutRepeatingCharacters import Solution

class TestSolution(TestCase):
    def test_length_longest_substring_with_same_characters(self):
        solution = Solution()
        res = solution.lengthOfLongestSubstring("bb")
        self.assertEquals(1, res)

    def test_length_longest_substring_with_different_characters(self):
        solution = Solution()
        res = solution.lengthOfLongestSubstring("abcabcbb")
        self.assertEquals(3, res)

    def test_length_longest_substring_with_no_repeating_characters(self):
        solution = Solution()
        res = solution.lengthOfLongestSubstring("abcdefg")
        self.assertEquals(7, res)

    def test_length_longest_substring_with_some_repeating_characters(self):
        solution = Solution()
        res = solution.lengthOfLongestSubstring("pwwkew")
        self.assertEquals(3, res)

    def test_length_longest_substring_with_some_repeating_at_end(self):
        solution = Solution()
        res = solution.lengthOfLongestSubstring("abpww")
        self.assertEquals(4, res)

    def test_length_longest_substring_by_zero_string(self):
        solution = Solution()
        res = solution.lengthOfLongestSubstring("")
        self.assertEquals(0, res)

    def test_length_longest_substring_with_some_repeating_at_start(self):
        solution = Solution()
        res = solution.lengthOfLongestSubstring("wwabcd")
        self.assertEquals(5, res)

    def test_length_longest_substring_by_one_string(self):
        solution = Solution()
        res = solution.lengthOfLongestSubstring(" ")
        self.assertEquals(1, res)