from unittest import TestCase
from problems.N1575_Count_All_Possible_Routes import Solution

class TestSolution(TestCase):
    def test_countRoutes(self):
        self.assertEqual(4, Solution().countRoutes(locations = [2,3,6,8,4], start = 1, finish = 3, fuel = 5))

    def test_countRoutes_1(self):
        self.assertEqual(5, Solution().countRoutes(locations = [4,3,1], start = 1, finish = 0, fuel = 6))

    def test_countRoutes_2(self):
        self.assertEqual(0, Solution().countRoutes(locations = [5,2,1], start = 0, finish = 2, fuel = 3))

    def test_countRoutes_3(self):
        self.assertEqual(2, Solution().countRoutes(locations = [2,1,5], start = 0, finish = 0, fuel = 3))

    def test_countRoutes_4(self):
        self.assertEqual(615088286, Solution().countRoutes(locations = [1,2,3], start = 0, finish = 2, fuel = 40))
