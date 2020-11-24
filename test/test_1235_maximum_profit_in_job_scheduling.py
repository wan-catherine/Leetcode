from unittest import TestCase
from problems.N1235_Maximum_Profit_In_Job_Scheduling import Solution

class TestSolution(TestCase):
    def test_jobScheduling(self):
        self.assertEqual(120, Solution().jobScheduling(startTime = [1,2,3,3], endTime = [3,4,5,6], profit = [50,10,40,70]))

    def test_jobScheduling_1(self):
        self.assertEqual(150, Solution().jobScheduling(startTime = [1,2,3,4,6], endTime = [3,5,10,6,9], profit = [20,20,100,70,60]))

    def test_jobScheduling_2(self):
        self.assertEqual(6, Solution().jobScheduling(startTime = [1,1,1], endTime = [2,3,4], profit = [5,6,4]))
