from unittest import TestCase
from problems.N174_Dungeon_Game import Solution

class TestSolution(TestCase):
    def test_calculateMinimumHP(self):
        input = [[-2,-3,3],[-5,-10,1], [10,30,-5]]
        self.assertEqual(7, Solution().calculateMinimumHP(input))

    def test_calculateMinimumHP_1(self):
        input = [[1,-3,3],[0,-2,0],[-3,-3,-3]]
        self.assertEqual(3, Solution().calculateMinimumHP(input))
