from unittest import TestCase
from problems.N810_Chalkboard_XOR_Game import Solution

class TestSolution(TestCase):
    def test_xor_game(self):
        self.assertFalse(Solution().xorGame(nums = [1, 1, 2]))
