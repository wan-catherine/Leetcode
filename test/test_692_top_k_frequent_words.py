from unittest import TestCase
from problems.N692_Top_K_Frequent_Words import Solution

class TestSolution(TestCase):
    def test_topKFrequent(self):
        input = ["i", "love", "leetcode", "i", "love", "coding"]
        k = 2
        self.assertListEqual(["i", "love"], Solution().topKFrequent(input, k))

    def test_topKFrequent_1(self):
        input = ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"]
        k = 4
        self.assertListEqual(["the", "is", "sunny", "day"], Solution().topKFrequent(input, k))

    def test_topKFrequent_2(self):
        input = ["i", "love", "leetcode", "i", "love", "coding"]
        k = 1
        self.assertListEqual(["i"], Solution().topKFrequent(input, k))
