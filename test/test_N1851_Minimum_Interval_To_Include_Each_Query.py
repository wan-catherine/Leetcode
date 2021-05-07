from unittest import TestCase
from problems.N1851_Minimum_Interval_To_Include_Each_Query import Solution

class TestSolution(TestCase):
    def test_min_interval(self):
        self.assertListEqual([3,3,1,4], Solution().minInterval(intervals = [[1,4],[2,4],[3,6],[4,4]], queries = [2,3,4,5]))

    def test_min_interval_1(self):
        self.assertListEqual([2,-1,4,6], Solution().minInterval(intervals = [[2,3],[2,5],[1,8],[20,25]], queries = [2,19,5,22]))
