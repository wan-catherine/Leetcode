from unittest import TestCase
from problems.N329_Longest_Increasing_Path_In_A_Matrix import Solution

class TestSolution(TestCase):
    def test_longestIncreasingPath(self):
        self.assertEqual(4, Solution().longestIncreasingPath(matrix =
[
  [9,9,4],
  [6,6,8],
  [2,1,1]
] ))

    def test_longestIncreasingPath_1(self):
        self.assertEqual(4, Solution().longestIncreasingPath(matrix =
[
  [3,4,5],
  [3,2,6],
  [2,2,1]
] ))
