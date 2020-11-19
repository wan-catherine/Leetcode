from unittest import TestCase
from problems.N1659_Maximize_Grid_Happiness import Solution

class TestSolution(TestCase):
    def test_getMaxGridHappiness(self):
        self.assertEqual(240, Solution().getMaxGridHappiness(m = 2, n = 3, introvertsCount = 1, extrovertsCount = 2))

    def test_getMaxGridHappiness_1(self):
        self.assertEqual(260, Solution().getMaxGridHappiness(m = 3, n = 1, introvertsCount = 2, extrovertsCount = 1))

    def test_getMaxGridHappiness_2(self):
        self.assertEqual(240, Solution().getMaxGridHappiness(m = 2, n = 2, introvertsCount = 4, extrovertsCount = 0))