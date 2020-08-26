from unittest import TestCase
from problems.N816_Ambiguous_Coordinates import Solution

class TestSolution(TestCase):
    def test_ambiguousCoordinates(self):
        self.assertListEqual(["(1, 23)", "(12, 3)", "(1.2, 3)", "(1, 2.3)"], Solution().ambiguousCoordinates("(123)"))

    def test_ambiguousCoordinates_1(self):
        self.assertListEqual(["(0.001, 1)", "(0, 0.011)"], Solution().ambiguousCoordinates("(00011)"))

    def test_ambiguousCoordinates_2(self):
        self.assertListEqual(["(0, 123)", "(0, 12.3)", "(0, 1.23)", "(0.1, 23)", "(0.1, 2.3)", "(0.12, 3)"], Solution().ambiguousCoordinates("(0123)"))

    def test_ambiguousCoordinates_3(self):
        self.assertListEqual(["(10, 0)"], Solution().ambiguousCoordinates("(100)"))
