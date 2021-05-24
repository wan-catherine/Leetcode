from unittest import TestCase
from problems.N1871_Jump_Game_VII import Solution

class TestSolution(TestCase):
    def test_can_reach(self):
        self.assertTrue(Solution().canReach(s = "011010", minJump = 2, maxJump = 3))

    def test_can_reach_1(self):
        self.assertFalse(Solution().canReach(s = "01101110", minJump = 2, maxJump = 3))

    def test_can_reach_2(self):
        self.assertFalse(Solution().canReach("0101111011110011001110", 1, 2))
