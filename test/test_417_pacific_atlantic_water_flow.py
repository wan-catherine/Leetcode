from unittest import TestCase
from problems.N417_Pacific_Atlantic_Water_Flow import Solution

class TestSolution(TestCase):
    def test_pacificAtlantic(self):
        matrix = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
        self.assertListEqual([[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]], Solution().pacificAtlantic(matrix))

    def test_pacificAtlantic_1(self):
        matrix = [[1,2,3],[8,9,4],[7,6,5]]
        self.assertListEqual([[0,2],[1,0],[1,1],[1,2],[2,0],[2,1],[2,2]], Solution().pacificAtlantic(matrix))
