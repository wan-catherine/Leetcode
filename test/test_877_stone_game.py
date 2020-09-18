from unittest import TestCase
from problems.N877_Stone_Game import Solution

class TestSolution(TestCase):
    def test_stoneGame(self):
        self.assertTrue(Solution().stoneGame([5,3,4,5]))
