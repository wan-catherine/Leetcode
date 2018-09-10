from unittest import TestCase
from problems.RotateImage import Solution

class TestSolution(TestCase):
    def test_rotate(self):
        solution = Solution()
        input = [
  [1,2,3],
  [4,5,6],
  [7,8,9]
]
        solution.rotate(input)
        expected = [
  [7,4,1],
  [8,5,2],
  [9,6,3]
]
        self.assertEqual(input, expected)


    def test_rotate_four(self):
        solution = Solution()
        input = [
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
]
        solution.rotate(input)
        expected = [
  [15,13, 2, 5],
  [14, 3, 4, 1],
  [12, 6, 8, 9],
  [16, 7,10,11]
]
        self.assertEqual(input, expected)