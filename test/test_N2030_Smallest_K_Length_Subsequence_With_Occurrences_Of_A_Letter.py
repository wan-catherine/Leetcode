from unittest import TestCase
from problems.N2030_Smallest_K_Length_Subsequence_With_Occurrences_Of_A_Letter import Solution

class TestSolution(TestCase):
    def test_smallest_subsequence(self):
        self.assertEqual("eet", Solution().smallestSubsequence(s = "leet", k = 3, letter = "e", repetition = 1))

    def test_smallest_subsequence_1(self):
        self.assertEqual("ecde", Solution().smallestSubsequence(s = "leetcode", k = 4, letter = "e", repetition = 2))

    def test_smallest_subsequence_2(self):
        self.assertEqual("bb", Solution().smallestSubsequence(s = "bb", k = 2, letter = "b", repetition = 2))

    def test_smallest_subsequence_3(self):
        self.assertEqual("abb", Solution().smallestSubsequence("aaabbbcccddd", 3, "b", 2))
