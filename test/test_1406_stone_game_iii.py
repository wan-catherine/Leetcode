from unittest import TestCase
from problems.N1406_Stone_Game_III import Solution

class TestSolution(TestCase):
    def test_stoneGameIII(self):
        self.assertEqual("Bob", Solution().stoneGameIII([1,2,3,7]))

    def test_stoneGameIII_1(self):
        self.assertEqual("Alice", Solution().stoneGameIII([1,2,3,-9]))

    def test_stoneGameIII_2(self):
        self.assertEqual("Tie", Solution().stoneGameIII([1,2,3,6]))

    def test_stoneGameIII_3(self):
        self.assertEqual("Alice", Solution().stoneGameIII([1,2,3,-1,-2,-3,7]))

    def test_stoneGameIII_4(self):
        self.assertEqual("Tie", Solution().stoneGameIII([-1,-2,-3]))