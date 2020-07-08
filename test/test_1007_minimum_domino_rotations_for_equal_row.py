from unittest import TestCase
from problems.N1007_Minimum_Domino_Rotations_For_Equal_Row import Solution

class TestSolution(TestCase):
    def test_minDominoRotations(self):
        A = [2, 1, 2, 4, 2, 2]
        B = [5, 2, 6, 2, 3, 2]
        self.assertEqual(2, Solution().minDominoRotations(A, B))

    def test_minDominoRotations_1(self):
        A = [3, 5, 1, 2, 3]
        B = [3, 6, 3, 3, 4]
        self.assertEqual(-1, Solution().minDominoRotations(A, B))
