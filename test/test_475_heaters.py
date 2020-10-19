from unittest import TestCase
from problems.N475_Heaters import Solution

class TestSolution(TestCase):
    def test_findRadius(self):
        self.assertEqual(1, Solution().findRadius(houses = [1,2,3], heaters = [2]))

    def test_findRadius_1(self):
        self.assertEqual(1, Solution().findRadius(houses = [1,2,3,4], heaters = [1,4]))

    def test_findRadius_2(self):
        self.assertEqual(3, Solution().findRadius(houses = [1,5], heaters = [2]))