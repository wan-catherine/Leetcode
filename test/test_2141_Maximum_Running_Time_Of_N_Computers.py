from unittest import TestCase
from problems.N2141_Maximum_Running_Time_Of_N_Computers import Solution

class TestSolution(TestCase):
    def test_max_run_time(self):
        self.assertEqual(2, Solution().maxRunTime(n = 2, batteries = [1,1,1,1]))

    def test_max_run_time_1(self):
        self.assertEqual(4, Solution().maxRunTime(n = 2, batteries = [3,3,3]))