from unittest import TestCase
from problems.N3440_Reschedule_Meetings_For_Maximum_Free_Time_II import Solution

class TestSolution(TestCase):
    def test_max_free_time(self):
        self.assertEquals(2, Solution().maxFreeTime(eventTime = 5, startTime = [1,3], endTime = [2,5]))

    def test_max_free_time_1(self):
        self.assertEquals(7, Solution().maxFreeTime(eventTime = 10, startTime = [0,7,9], endTime = [1,8,10]))

    def test_max_free_time_2(self):
        self.assertEquals(6, Solution().maxFreeTime(eventTime = 10, startTime = [0,3,7,9], endTime = [1,4,8,10]))

    def test_max_free_time_3(self):
        self.assertEquals(0, Solution().maxFreeTime(eventTime = 5, startTime = [0,1,2,3,4], endTime = [1,2,3,4,5]))
