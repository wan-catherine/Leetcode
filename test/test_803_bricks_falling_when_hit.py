from unittest import TestCase
from problems.N803_Bricks_Falling_When_Hit import Solution

class TestSolution(TestCase):
    def test_hitBricks(self):
        self.assertListEqual([2], Solution().hitBricks(grid = [[1,0,0,0],[1,1,1,0]], hits = [[1,0]]))

    def test_hitBricks_1(self):
        self.assertListEqual([0, 0], Solution().hitBricks(grid = [[1,0,0,0],[1,1,0,0]], hits = [[1,1],[1,0]]))

    def test_hitBricks_2(self):
        self.assertListEqual([1,0,1,0,0], Solution().hitBricks([[1],[1],[1],[1],[1]], [[3,0],[4,0],[1,0],[2,0],[0,0]]))
