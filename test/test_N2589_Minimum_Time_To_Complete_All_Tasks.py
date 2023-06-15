from unittest import TestCase
from problems.N2589_Minimum_Time_To_Complete_All_Tasks import Solution

class TestSolution(TestCase):
    def test_find_minimum_time(self):
        self.assertEqual(2, Solution().findMinimumTime([[2,3,1],[4,5,1],[1,5,2]]))

    def test_find_minimum_time_1(self):
        self.assertEqual(4, Solution().findMinimumTime([[1,3,2],[2,5,3],[5,6,2]]))

    def test_find_minimum_time_2(self):
        self.assertEqual(5, Solution().findMinimumTime([[1,18,5],[3,15,1]]))
