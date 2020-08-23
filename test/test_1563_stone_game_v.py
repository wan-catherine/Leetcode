from unittest import TestCase
from problems.N1563_Stone_Game_V import Solution

class TestSolution(TestCase):
    def test_stoneGameV(self):
        self.assertEqual(18, Solution().stoneGameV([6,2,3,4,5,5]))

    def test_stoneGameV_1(self):
        self.assertEqual(28, Solution().stoneGameV([7,7,7,7,7,7,7]))

    def test_stoneGameV_2(self):
        self.assertEqual(0, Solution().stoneGameV([4]))

    def test_stoneGameV_3(self):
        self.assertEqual(304, Solution().stoneGameV([68,75,25,50,34,29,77,1,2,69]))

    def test_stoneGameV_4(self):
        self.assertEqual(3, Solution().stoneGameV([1,1,2]))
