from unittest import TestCase
from problems.N773_Sliding_Puzzle import Solution

class TestSolution(TestCase):
    def test_sliding_puzzle(self):
        self.assertEqual(1, Solution().slidingPuzzle([[1,2,3],[4,0,5]]))

    def test_sliding_puzzle_1(self):
        self.assertEqual(-1, Solution().slidingPuzzle([[1,2,3],[5,4,0]]))

    def test_sliding_puzzle_2(self):
        self.assertEqual(5, Solution().slidingPuzzle([[4,1,2],[5,0,3]]))

    def test_sliding_puzzle_3(self):
        self.assertEqual(14, Solution().slidingPuzzle([[3,2,4],[1,5,0]]))
