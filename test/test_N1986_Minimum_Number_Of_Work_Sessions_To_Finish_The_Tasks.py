from unittest import TestCase
from problems.N1986_Minimum_Number_Of_Work_Sessions_To_Finish_The_Tasks import Solution

class TestSolution(TestCase):
    def test_min_sessions(self):
        self.assertEqual(2, Solution().minSessions(tasks = [1,2,3], sessionTime = 3))

    def test_min_sessions_1(self):
        self.assertEqual(2, Solution().minSessions(tasks = [3,1,3,1,1], sessionTime = 8))

    def test_min_sessions_2(self):
        self.assertEqual(1, Solution().minSessions(tasks = [1,2,3,4,5], sessionTime = 15))
