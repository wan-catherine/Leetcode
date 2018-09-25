from unittest import TestCase
from problems.Search2DMatrix import Solution

class TestSolution(TestCase):
    def test_searchMatrix(self):
        solution = Solution()
        input = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
        res = solution.searchMatrix(input, 13)
        self.assertEqual(res, False)


    def test_searchMatrix_1(self):
        solution = Solution()
        input = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
        res = solution.searchMatrix(input, 3)
        self.assertEqual(res, True)

    def test_searchMatrix_null(self):
        solution = Solution()
        res = solution.searchMatrix([[]], 1)
        self.assertEqual(res, False)
