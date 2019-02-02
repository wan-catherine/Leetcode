from unittest import TestCase
from problems.GuessNumberHigherLower import Solution

class TestSolution(TestCase):
    def test_guessNumber(self):
        solution = Solution()
        res = solution.guessNumber()
