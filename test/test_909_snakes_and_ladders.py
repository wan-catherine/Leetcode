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

    def test_snakesAndLadders_3(self):
        self.assertEqual(4, Solution().snakesAndLadders([[-1,-1,-1,46,47,-1,-1,-1],[51,-1,-1,63,-1,31,21,-1],[-1,-1,26,-1,-1,38,-1,-1],[-1,-1,11,-1,14,23,56,57],[11,-1,-1,-1,49,36,-1,48],[-1,-1,-1,33,56,-1,57,21],[-1,-1,-1,-1,-1,-1,2,-1],[-1,-1,-1,8,3,-1,6,56]]))
