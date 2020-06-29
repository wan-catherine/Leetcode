from unittest import TestCase
from problems.UniquePathsII import Solution

class TestSolution(TestCase):
    def test_uniquePathsWithObstacles(self):
        solution = Solution()
        input = [
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
        res = solution.uniquePathsWithObstacles(input)
        self.assertEqual(2, res)

    def test_uniquePathsWithObstacles_1(self):
        input = [[1]]
        res = Solution().uniquePathsWithObstacles(input)
        self.assertEqual(0, res)
