from unittest import TestCase
from problems.N524_Longest_Word_In_Dictionary_Through_Deleting import Solution

class TestSolution(TestCase):
    def test_findLongestWord(self):
        self.assertEqual("apple", Solution().findLongestWord(s = "abpcplea", d = ["ale","apple","monkey","plea"]))

    def test_findLongestWord_1(self):
        self.assertEqual("a", Solution().findLongestWord(s = "abpcplea", d = ["a","b","c"]))

    def test_findLongestWord_2(self):
        s = "wordgoodgoodgoodbestword"
        d = ["word", "good", "best", "good"]
        self.assertEqual("best", Solution().findLongestWord(s, d))