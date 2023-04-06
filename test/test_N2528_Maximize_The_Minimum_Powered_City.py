from unittest import TestCase
from problems.N2528_Maximize_The_Minimum_Powered_City import Solution

class TestSolution(TestCase):
    def test_max_power(self):
        self.assertEqual(5, Solution().maxPower(stations = [1,2,4,5,0], r = 1, k = 2))

    def test_max_power_1(self):
        self.assertEqual(4, Solution().maxPower(stations = [4,4,4,4], r = 0, k = 3))

    def test_max_power_2(self):
        self.assertEqual(7, Solution().maxPower(stations = [4,2], r = 1, k = 1))
