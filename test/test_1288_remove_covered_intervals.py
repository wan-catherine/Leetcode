from unittest import TestCase
from problems.N1288_Remove_Covered_Intervals import Solution

class TestSolution(TestCase):
    def test_removeCoveredIntervals(self):
        self.assertEqual(2, Solution().removeCoveredIntervals([[1,4],[3,6],[2,8]]))

    def test_removeCoveredIntervals_1(self):
        self.assertEqual(1, Solution().removeCoveredIntervals([[1,4],[2,3]]))

    def test_removeCoveredIntervals_2(self):
        self.assertEqual(2, Solution().removeCoveredIntervals([[0,10],[5,12]]))

    def test_removeCoveredIntervals_3(self):
        self.assertEqual(2, Solution().removeCoveredIntervals([[3,10],[4,10],[5,11]]))

    def test_removeCoveredIntervals_4(self):
        self.assertEqual(1, Solution().removeCoveredIntervals([[1,2],[1,4],[3,4]]))

