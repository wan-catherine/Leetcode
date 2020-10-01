from unittest import TestCase
from problems.N861_Score_After_Flipping_Matrix import Solution

class TestSolution(TestCase):
    def test_matrixScore(self):
        self.assertEqual(39, Solution().matrixScore([[0,0,1,1],[1,0,1,0],[1,1,0,0]]))
