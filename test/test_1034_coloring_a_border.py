from unittest import TestCase
from problems.N1034_Coloring_A_Border import Solution

class TestSolution(TestCase):
    def test_colorBorder(self):
        self.assertListEqual([[3, 3], [3, 2]], Solution().colorBorder(grid = [[1,1],[1,2]], r0 = 0, c0 = 0, color = 3))

    def test_colorBorder_1(self):
        self.assertListEqual([[1, 3, 3], [2, 3, 3]], Solution().colorBorder(grid = [[1,2,2],[2,3,2]], r0 = 0, c0 = 1, color = 3))

    def test_colorBorder_2(self):
        self.assertListEqual([[2, 2, 2], [2, 1, 2], [2, 2, 2]], Solution().colorBorder(grid = [[1,1,1],[1,1,1],[1,1,1]], r0 = 1, c0 = 1, color = 2))

