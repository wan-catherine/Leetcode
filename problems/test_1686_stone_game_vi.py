from unittest import TestCase
from problems.N1686_Stone_Game_VI import Solution

class TestSolution(TestCase):
    def test_stoneGameVI(self):
        self.assertEqual(1, Solution().stoneGameVI(aliceValues = [1,3], bobValues = [2,1]))

    def test_stoneGameVI_1(self):
        self.assertEqual(0, Solution().stoneGameVI(aliceValues = [1,2], bobValues = [3,1]))

    def test_stoneGameVI_2(self):
        self.assertEqual(-1, Solution().stoneGameVI(aliceValues = [2,4,3], bobValues = [1,6,7]))
