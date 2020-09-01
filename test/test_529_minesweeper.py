from unittest import TestCase
from problems.N529_Minesweeper import Solution

class TestSolution(TestCase):
    def test_updateBoard(self):
        board = [['E', 'E', 'E', 'E', 'E'],
 ['E', 'E', 'M', 'E', 'E'],
 ['E', 'E', 'E', 'E', 'E'],
 ['E', 'E', 'E', 'E', 'E']]
        click = [3,0]
        output = [['B', '1', 'E', '1', 'B'],
 ['B', '1', 'M', '1', 'B'],
 ['B', '1', '1', '1', 'B'],
 ['B', 'B', 'B', 'B', 'B']]
        res = Solution().updateBoard(board, click)
        for index , li in enumerate(res):
            self.assertListEqual(output[index], li)

    def test_updateBoard_1(self):
        board = [['B', '1', 'E', '1', 'B'],
 ['B', '1', 'M', '1', 'B'],
 ['B', '1', '1', '1', 'B'],
 ['B', 'B', 'B', 'B', 'B']]
        click = [1, 2]
        output = [['B', '1', 'E', '1', 'B'],
 ['B', '1', 'X', '1', 'B'],
 ['B', '1', '1', '1', 'B'],
 ['B', 'B', 'B', 'B', 'B']]

        res = Solution().updateBoard(board, click)
        for index, li in enumerate(res):
            self.assertListEqual(output[index], li)
