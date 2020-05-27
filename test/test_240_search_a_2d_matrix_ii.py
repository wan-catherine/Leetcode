from unittest import TestCase
from problems.N240_Search_A_2D_Matrix_II import Solution

class TestSolution(TestCase):
    def test_searchMatrix(self):
        input = [
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
        self.assertEqual(True, Solution().searchMatrix(input, 5))
        self.assertEqual(False, Solution().searchMatrix(input, 20))

    def test_searchMatrix_1(self):
        self.assertEqual(False, Solution().searchMatrix([[]], 20))
