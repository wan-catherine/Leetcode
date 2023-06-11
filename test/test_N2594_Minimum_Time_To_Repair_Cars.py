from unittest import TestCase
from problems.N2594_Minimum_Time_To_Repair_Cars import Solution

class TestSolution(TestCase):
    def test_repair_cars(self):
        self.assertEqual(16, Solution().repairCars(ranks = [4,2,3,1], cars = 10))

    def test_repair_cars_1(self):
        self.assertEqual(16, Solution().repairCars(ranks = [5,1,8], cars = 6))

    def test_repair_cars_2(self):
        self.assertEqual(75, Solution().repairCars([3,3,1,2,1,1,3,2,1], 58))
