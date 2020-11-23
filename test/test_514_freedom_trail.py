from unittest import TestCase
from problems.N514_Freedom_Trail import Solution

class TestSolution(TestCase):
    def test_findRotateSteps(self):
        self.assertEqual(4, Solution().findRotateSteps(ring = "godding", key = "gd"))

    def test_findRotateSteps_1(self):
        self.assertEqual(17, Solution().findRotateSteps("ababcab", "acbaacba"))
