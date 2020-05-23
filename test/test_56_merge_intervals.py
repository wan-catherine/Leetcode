from unittest import TestCase
from problems.N56_Merge_Intervals import Solution

class TestSolution(TestCase):
    def test_merge(self):
        input = [[1,3],[2,6],[8,10],[15,18]]
        output = [[1,6],[8,10],[15,18]]
        self.assertListEqual(output, Solution().merge(input))

    def test_merge_1(self):
        input = [[1,4],[4,5]]
        output = [[1,5]]
        self.assertListEqual(output, Solution().merge(input))
