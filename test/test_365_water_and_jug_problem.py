from unittest import TestCase
from problems.N365_Water_And_Jug_Problem import Solution

class TestSolution(TestCase):
    def test_canMeasureWater(self):
        self.assertTrue(Solution().canMeasureWater(x = 3, y = 5, z = 4))

    def test_canMeasureWater_1(self):
        self.assertFalse(Solution().canMeasureWater(x = 2, y = 6, z = 5))

    def test_canMeasureWater_2(self):
        self.assertTrue(Solution().canMeasureWater(34, 5, 6))
