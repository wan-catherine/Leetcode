from unittest import TestCase
from problems.N782_Transform_To_Chessboard import Solution

class TestSolution(TestCase):
    def test_moves_to_chessboard(self):
        self.assertEqual(2, Solution().movesToChessboard([[0,1,1,0],[0,1,1,0],[1,0,0,1],[1,0,0,1]]))

    def test_moves_to_chessboard_1(self):
        self.assertEqual(0, Solution().movesToChessboard([[0,1],[1,0]]))

    def test_moves_to_chessboard_2(self):
        self.assertEqual(-1, Solution().movesToChessboard([[1,0],[1,0]]))

    def test_moves_to_chessboard_3(self):
        self.assertEqual(2, Solution().movesToChessboard([[1,1,0],[0,0,1],[0,0,1]]))
