from unittest import TestCase
from problems.WordSearch import Solution

class TestSolution(TestCase):
    def test_exist(self):
        solution = Solution()
        board = [
            ['A', 'B', 'C', 'E'],
            ['S', 'F', 'C', 'S'],
            ['A', 'D', 'E', 'E']
        ]
        res = solution.exist(board, "ABCCED")
        res2=solution.exist(board, "SEE")
        res3 = solution.exist(board, "ABCB")
        self.assertEqual(res, True)
        self.assertEqual(res2, True)
        self.assertEqual(res3, False)

    def test_exist(self):
        solution = Solution()
        board = [["C","A","A"],["A","A","A"],["B","C","D"]]
        res = solution.exist(board,"AAB")
        self.assertEqual(True, res)
