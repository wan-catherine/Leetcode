from unittest import TestCase
from problems.N1690_Stone_Game_VII import Solution

class TestSolution(TestCase):
    def test_stoneGameVII(self):
        self.assertEqual(6, Solution().stoneGameVII([5,3,1,4,2]))

    def test_stoneGameVII_1(self):
        self.assertEqual(122, Solution().stoneGameVII([7,90,5,1,100,10,10,2]))