from unittest import TestCase
from problems.N913_Cat_And_Mouse import Solution

class TestSolution(TestCase):
    def test_catMouseGame(self):
        self.assertEqual(0, Solution().catMouseGame([[2,5],[3],[0,4,5],[1,4,5],[2,3],[0,2,3]]))

    def test_catMouseGame_1(self):
        self.assertEqual(1, Solution().catMouseGame([[1,3],[0],[3],[0,2]]))

    def test_catMouseGame_2(self):
        self.assertEqual(1, Solution().catMouseGame([[2,3],[3,4],[0,4],[0,1],[1,2]]))
