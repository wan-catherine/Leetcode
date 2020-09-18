from unittest import TestCase
from problems.N837_New_21_Game import Solution

class TestSolution(TestCase):
    def test_new21Game(self):
        self.assertEqual(1.0, Solution().new21Game(N = 10, K = 1, W = 10))

    def test_new21Game_1(self):
        self.assertEqual(0.6, Solution().new21Game(N = 6, K = 1, W = 10))

    def test_new21Game_2(self):
        self.assertEqual(0.73278, Solution().new21Game(N = 21, K = 17, W = 10))
