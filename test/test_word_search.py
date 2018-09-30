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

    def test_exist_special(self):
        solution = Solution()
        # board = [["C","A","A"],["A","A","A"],["B","C","D"]]
        board = [["C", "A", "A"], ["A", "A", "A"], ["B", "C", "D"]]
        res = solution.exist(board,"AAB")
        self.assertEqual(True, res)

    def test_exist_difficult(self):
        solution = Solution()
        board = [["a","a","a"],["a","b","b"],["a","b","b"],["b","b","b"],["b","b","b"],["a","a","a"],["b","b","b"],["a","b","b"],["a","a","b"],["a","b","a"]]
        res = solution.exist(board,"aabaaaabbb")
        self.assertEqual(False, res)

    def test_exist_new(self):
        solution = Solution()
        board = [["A","B","C","E"],["S","F","E","S"],["A","D","E","E"]]
        res = solution.exist(board, "ABCESEEEFS")
        self.assertEqual(True, res)

    def test_exist_output(self):
        solution = Solution()
        board = [["a","a","a","a"],["a","a","a","a"],["a","a","a","a"],["a","a","a","a"],["a","a","a","b"]]
        res = solution.exist(board, "aaaaaaaaaaaaaaaaaaaa")
        self.assertEqual(False, res)

    def test_exist_one(self):
        solution = Solution()
        res = solution.exist([["a"]], "b")
        self.assertEqual(False, res)