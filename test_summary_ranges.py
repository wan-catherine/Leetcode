from unittest import TestCase
from problems.SummaryRanges import Solution

class TestSolution(TestCase):
    def test_summaryRanges(self):
        solution = Solution()
        res = solution.summaryRanges([0,1,2,4,5,7])
        self.assertEqual(res, ["0->2","4->5","7"])

    def test_summaryRanges_one(self):
        solution = Solution()
        res = solution.summaryRanges([0,2,3,4,6,8,9])
        self.assertEqual(res, ["0","2->4","6","8->9"])
