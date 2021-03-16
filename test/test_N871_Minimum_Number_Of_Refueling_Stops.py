from unittest import TestCase
from problems.N871_Minimum_Number_Of_Refueling_Stops import Solution

class TestSolution(TestCase):
    def test_min_refuel_stops(self):
        self.assertEqual(0, Solution().minRefuelStops(target = 1, startFuel = 1, stations = []))

    def test_min_refuel_stops_1(self):
        self.assertEqual(-1, Solution().minRefuelStops(target = 100, startFuel = 1, stations = [[10,100]]))

    def test_min_refuel_stops_2(self):
        self.assertEqual(2, Solution().minRefuelStops(target = 100, startFuel = 10, stations = [[10,60],[20,30],[30,30],[60,40]]))

    def test_min_refuel_stops_3(self):
        self.assertEqual(1, Solution().minRefuelStops(100, 50, [[25,25],[50,50]]))