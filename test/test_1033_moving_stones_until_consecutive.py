from unittest import TestCase
from problems.N1033_Moving_Stones_Until_Consecutive import Solution

class TestSolution(TestCase):
    def test_numMovesStones(self):
        self.assertListEqual([1,2], Solution().numMovesStones(1,2,5))

    def test_numMovesStones_1(self):
        self.assertListEqual([0,0], Solution().numMovesStones(4,3,2))

    def test_numMovesStones_2(self):
        self.assertListEqual([1,2], Solution().numMovesStones(3,5,1))
