from unittest import TestCase
from problems.N2332_The_Latest_Time_To_Catch_A_Bus import Solution

class TestSolution(TestCase):
    def test_latest_time_catch_the_bus(self):
        self.assertEqual(16, Solution().latestTimeCatchTheBus(buses = [10,20], passengers = [2,17,18,19], capacity = 2))

    def test_latest_time_catch_the_bus_1(self):
        self.assertEqual(20, Solution().latestTimeCatchTheBus(buses = [20,30,10], passengers = [19,13,26,4,25,11,21], capacity = 2))
