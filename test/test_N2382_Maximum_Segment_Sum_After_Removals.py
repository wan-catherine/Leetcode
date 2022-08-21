from unittest import TestCase
from problems.N2382_Maximum_Segment_Sum_After_Removals import Solution

class TestSolution(TestCase):
    def test_maximum_segment_sum(self):
        self.assertListEqual([14,7,2,2,0], Solution().maximumSegmentSum(nums = [1,2,5,6,1], removeQueries = [0,3,2,4,1]))

    def test_maximum_segment_sum_1(self):
        self.assertListEqual([16,5,3,0], Solution().maximumSegmentSum(nums = [3,2,11,1], removeQueries = [3,2,1,0]))

    def test_maximum_segment_sum_2(self):
        self.assertListEqual([3013,2583,2583,2583,2583,2583,1900,822,822,822,340,0], Solution().maximumSegmentSum([500,822,202,707,298,484,311,680,901,319,343,340], [6,4,0,5,2,3,10,8,7,9,1,11]))
