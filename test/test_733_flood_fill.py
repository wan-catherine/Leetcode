from unittest import TestCase
from problems.N733_Flood_Fill import Solution

class TestSolution(TestCase):
    def test_floodFill(self):
        res = Solution().floodFill([[1,1,1],[1,1,0],[1,0,1]], 1, 1, 2)
        self.assertListEqual([[2,2,2],[2,2,0],[2,0,1]], res)
