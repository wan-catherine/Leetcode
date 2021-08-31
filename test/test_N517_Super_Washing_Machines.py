from unittest import TestCase
from problems.N517_Super_Washing_Machines import Solution

class TestSolution(TestCase):
    def test_find_min_moves(self):
        self.assertEqual(3, Solution().findMinMoves([1,0,5]))

    def test_find_min_moves_1(self):
        self.assertEqual(2, Solution().findMinMoves([0,3,0]))

    def test_find_min_moves_2(self):
        self.assertEqual(-1, Solution().findMinMoves([0,2,0]))