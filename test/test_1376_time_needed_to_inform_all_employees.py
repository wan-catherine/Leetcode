from unittest import TestCase
from problems.N1376_Time_Needed_To_Inform_All_Employees import Solution

class TestSolution(TestCase):
    def test_numOfMinutes(self):
        self.assertEqual(0, Solution().numOfMinutes(n = 1, headID = 0, manager = [-1], informTime = [0]))

    def test_numOfMinutes_1(self):
        self.assertEqual(1, Solution().numOfMinutes(n = 6, headID = 2, manager = [2,2,-1,2,2,2], informTime = [0,0,1,0,0,0]))

    def test_numOfMinutes_2(self):
        self.assertEqual(21, Solution().numOfMinutes(n = 7, headID = 6, manager = [1,2,3,4,5,6,-1], informTime = [0,6,5,4,3,2,1]))

    def test_numOfMinutes_3(self):
        self.assertEqual(3, Solution().numOfMinutes(n = 15, headID = 0, manager = [-1,0,0,1,1,2,2,3,3,4,4,5,5,6,6], informTime = [1,1,1,1,1,1,1,0,0,0,0,0,0,0,0]))

    def test_numOfMinutes_4(self):
        self.assertEqual(1076, Solution().numOfMinutes(n = 4, headID = 2, manager = [3,3,-1,2], informTime = [0,0,162,914]))
