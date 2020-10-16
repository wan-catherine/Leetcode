from unittest import TestCase
from problems.N909_Snakes_And_Ladders import Solution

class TestSolution(TestCase):
    def test_snakesAndLadders(self):
        self.assertEqual(4, Solution().snakesAndLadders([
[-1,-1,-1,-1,-1,-1],
[-1,-1,-1,-1,-1,-1],
[-1,-1,-1,-1,-1,-1],
[-1,35,-1,-1,13,-1],
[-1,-1,-1,-1,-1,-1],
[-1,15,-1,-1,-1,-1]]))

    def test_snakesAndLadders_1(self):
        self.assertEqual(1, Solution().snakesAndLadders([[-1,-1],[-1,3]]))

    def test_snakesAndLadders_2(self):
        self.assertEqual(2, Solution().snakesAndLadders([[-1,4,-1],[6,2,6],[-1,3,-1]]))
