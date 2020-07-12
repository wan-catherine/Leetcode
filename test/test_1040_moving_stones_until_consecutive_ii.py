from unittest import TestCase
from problems.N1040_Moving_Stones_Until_Consecutive_II import Solution

class TestSolution(TestCase):
    def test_numMovesStonesII(self):
        self.assertListEqual([1,2], Solution().numMovesStonesII([7,4,9]))

    def test_numMovesStonesII_1(self):
        self.assertListEqual([2,3], Solution().numMovesStonesII([6,5,4,3,10]))

    def test_numMovesStonesII_2(self):
        self.assertListEqual([0,0], Solution().numMovesStonesII([100,101,104,102,103]))