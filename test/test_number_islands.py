from unittest import TestCase
from problems.NumberIslands import Solution

class TestSolution(TestCase):
    def test_numIslands(self):
        solution = Solution()
        input = [
            ["1","1","1","1","0"],
            ["1","1","0","1","0"],
            ["1","1","0","0","0"],
            ["0","0","0","0","0"]
        ]
        res = solution.numIslands(input)
        self.assertEqual(1, res)


