from unittest import TestCase
from problems.N1277_Count_Square_Submatrices_With_All_Ones import Solution

class TestSolution(TestCase):
    def test_countSquares(self):
        matrix =[
            [0, 1, 1, 1],
            [1, 1, 1, 1],
            [0, 1, 1, 1]
        ]
        self.assertEqual(15, Solution().countSquares(matrix))

    def test_countSquares_1(self):
        matrix =[
            [1, 0, 1],
            [1, 1, 0],
            [1, 1, 0]
        ]
        self.assertEqual(7, Solution().countSquares(matrix))
