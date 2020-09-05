from unittest import TestCase
from problems.N756_Pyramid_Transition_Matrix import Solution

class TestSolution(TestCase):
    def test_pyramidTransition(self):
        self.assertTrue(Solution().pyramidTransition(bottom = "BCD", allowed = ["BCG", "CDE", "GEA", "FFF"]))

    def test_pyramidTransition_1(self):
        self.assertFalse(Solution().pyramidTransition(bottom = "AABA", allowed = ["AAA", "AAB", "ABA", "ABB", "BAC"]))
