from unittest import TestCase
from problems.N3439_Reschedule_Meetings_For_Maximum_Free_Time_I import Solution

class TestSolution(TestCase):
    def test_max_free_time(self):
        self.assertEquals(2, Solution().maxFreeTime(eventTime = 5, k = 1, startTime = [1,3], endTime = [2,5]))

    def test_max_free_time_1(self):
        self.assertEquals(6, Solution().maxFreeTime(eventTime = 10, k = 1, startTime = [0,2,9], endTime = [1,4,10]))

    def test_max_free_time_2(self):
        self.assertEquals(0, Solution().maxFreeTime(eventTime = 5, k = 2, startTime = [0,1,2,3,4], endTime = [1,2,3,4,5]))

    def test_max_free_time_3(self):
        self.assertEquals(18, Solution().maxFreeTime(eventTime = 21, k = 2, startTime = [18,20], endTime = [20,21]))

    def test_max_free_time_4(self):
        self.assertEquals(7, Solution().maxFreeTime(eventTime = 21, k = 1, startTime = [7,10,16], endTime = [10,14,18]))
