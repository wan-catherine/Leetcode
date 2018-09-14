from unittest import TestCase
from problems.MergeIntervals import Solution, Interval

class TestSolution(TestCase):
    def test_merge(self):
        solution = Solution()
        res = solution.merge([Interval(1,3),Interval(2,6),Interval(8,10),Interval(15,18)])
        self.assertTrue(3,len(res))

    def test_merge_1(self):
        solution = Solution()
        res = solution.merge([Interval(1,4),Interval(4,6)])
        self.assertTrue(1,len(res))

    def test_merge_2(self):
        solution = Solution()
        res = solution.merge([Interval(1,4),Interval(2,3)])
        self.assertTrue(1,len(res))

    def test_merge_3(self):
        solution = Solution()
        res = solution.merge([Interval(1,4),Interval(1,4)])
        self.assertTrue(1,len(res))

