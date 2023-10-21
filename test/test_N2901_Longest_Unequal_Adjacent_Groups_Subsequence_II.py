from unittest import TestCase
from problems.N2901_Longest_Unequal_Adjacent_Groups_Subsequence_II import Solution

class TestSolution(TestCase):
    def test_get_words_in_longest_subsequence(self):
        self.assertListEqual(['bab', 'dab'], Solution().getWordsInLongestSubsequence(n = 3, words = ["bab","dab","cab"], groups = [1,2,2]))

    def test_get_words_in_longest_subsequence_1(self):
        self.assertListEqual(["a","b","c","d"], Solution().getWordsInLongestSubsequence(n = 4, words = ["a","b","c","d"], groups = [1,2,3,4]))

    def test_get_words_in_longest_subsequence_2(self):
        self.assertListEqual(["aaa","ada"], Solution().getWordsInLongestSubsequence(n = 3, words = ["bdb","aaa","ada"], groups = [2,1,3]))

    def test_get_words_in_longest_subsequence_3(self):
        self.assertListEqual(["cdb","cdd","cda"], Solution().getWordsInLongestSubsequence(n = 9, words = ["cdb","cdd","cd","dcc","cca","cda","ca","cc","bcc"], groups = [8,5,9,5,2,7,4,7,3]))
