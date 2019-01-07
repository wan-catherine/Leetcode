from unittest import TestCase
from problems.TopKFrequentElements import Solution

class TestSolution(TestCase):
    def test_topKFrequent(self):
        solution = Solution()
        res = solution.topKFrequent([1,1,1,2,2,3], 2)
        self.assertEqual(res, [1,2])

    def test_topKFrequent_one(self):
        solution = Solution()
        res = solution.topKFrequent([1], 1)
        self.assertEqual(res, [1])
