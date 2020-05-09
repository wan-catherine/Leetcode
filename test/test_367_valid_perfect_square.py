from unittest import TestCase
from problems.N367_Valid_Perfect_Square import Solution

class TestSolution(TestCase):
    def test_isPerfectSquare(self):
        self.assertEqual(True, Solution().isPerfectSquare(16))

    def test_isPerfectSquare_1(self):
        self.assertEqual(False, Solution().isPerfectSquare(14))
