from unittest import TestCase
from problems.N711_Number_Of_Distinct_Island_II import Solution

class TestSolution(TestCase):
    def test_num_distinct_islands2(self):
        self.assertEqual(1, Solution().numDistinctIslands2([[1,1,0,0,0],[1,0,0,0,0],[0,0,0,0,1],[0,0,0,1,1]]))

    def test_num_distinct_islands2_1(self):
        self.assertEqual(1, Solution().numDistinctIslands2([[1,1,0,0,0],[1,1,0,0,0],[0,0,0,1,1],[0,0,0,1,1]]))
