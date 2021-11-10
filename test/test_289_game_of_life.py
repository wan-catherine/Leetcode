from unittest import TestCase
from problems.N289_Game_Of_Life import Solution

class TestSolution(TestCase):
    def test_gameOfLife(self):
        input = [
  [0,1,0],
  [0,0,1],
  [1,1,1],
  [0,0,0]
]
        output = [
  [0,0,0],
  [1,0,1],
  [0,1,1],
  [0,1,0]
]
        self.assertListEqual(output, Solution().gameOfLife(input))

    def test_gameOfLife_(self):
        input = [[1,1],[1,0]]
        output = [[1,1],[1,1]]
        self.assertListEqual(output, Solution().gameOfLife(input))
