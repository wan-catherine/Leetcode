from unittest import TestCase
from problems.N1723_Find_Minimum_Time_To_Finish_All_Jobs import Solution

class TestSolution(TestCase):
    def test_minimumTimeRequired(self):
        self.assertEqual(3, Solution().minimumTimeRequired(jobs = [3,2,3], k = 3))

    def test_minimumTimeRequired_1(self):
        self.assertEqual(11, Solution().minimumTimeRequired(jobs = [1,2,4,7,8], k = 2))
