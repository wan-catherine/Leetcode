from unittest import TestCase
from problems.N916_Word_Subsets import Solution

class TestSolution(TestCase):
    def test_wordSubsets(self):
        A = ["amazon", "apple", "facebook", "google", "leetcode"]
        B = ["e", "o"]
        self.assertListEqual(["facebook","google","leetcode"], Solution().wordSubsets(A,B))

    def test_wordSubsets_1(self):
        A = ["amazon", "apple", "facebook", "google", "leetcode"]
        B = ["l", "e"]
        self.assertListEqual(["apple","google","leetcode"], Solution().wordSubsets(A,B))

    def test_wordSubsets_2(self):
        A = ["amazon", "apple", "facebook", "google", "leetcode"]
        B = ["e", "oo"]
        self.assertListEqual(["facebook","google"], Solution().wordSubsets(A,B))

    def test_wordSubsets_3(self):
        A = ["amazon", "apple", "facebook", "google", "leetcode"]
        B = ["lo", "eo"]
        self.assertListEqual(["google","leetcode"], Solution().wordSubsets(A,B))

    def test_wordSubsets_4(self):
        A = ["amazon", "apple", "facebook", "google", "leetcode"]
        B = ["ec", "oc", "ceo"]
        self.assertListEqual(["facebook","leetcode"], Solution().wordSubsets(A,B))
