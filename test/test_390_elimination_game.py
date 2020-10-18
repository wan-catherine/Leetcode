from unittest import TestCase
from problems.N390_Elimination_Game import Solution

class TestSolution(TestCase):
    def test_lastRemaining(self):
        self.assertEqual(6, Solution().lastRemaining(9))
