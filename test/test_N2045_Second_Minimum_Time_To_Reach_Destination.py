from unittest import TestCase
from problems.N2045_Second_Minimum_Time_To_Reach_Destination import Solution

class TestSolution(TestCase):
    def test_second_minimum(self):
        self.assertEqual(13, Solution().secondMinimum(n = 5, edges = [[1,2],[1,3],[1,4],[3,4],[4,5]], time = 3, change = 5))

    def test_second_minimum_1(self):
        self.assertEqual(11, Solution().secondMinimum(n = 2, edges = [[1,2]], time = 3, change = 2))

