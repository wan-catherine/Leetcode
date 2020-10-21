from unittest import TestCase
from problems.N799_Champagne_Tower import Solution

class TestSolution(TestCase):
    def test_champagneTower(self):
        self.assertEqual(0.0, Solution().champagneTower(1,1,1))

    def test_champagneTower_1(self):
        self.assertEqual(0.5, Solution().champagneTower(2,1,1))

    def test_champagneTower_2(self):
        self.assertEqual(1.0, Solution().champagneTower(poured = 100000009, query_row = 33, query_glass = 17))
