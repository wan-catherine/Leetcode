from unittest import TestCase
from problems.N1447_Simplified_Fractions import Solution

class TestSolution(TestCase):
    def test_simplifiedFractions(self):
        self.assertListEqual(["1/2"], Solution().simplifiedFractions(2))

    def test_simplifiedFractions_1(self):
        self.assertListEqual(["1/2","1/3","2/3"], Solution().simplifiedFractions(3))

    def test_simplifiedFractions_2(self):
        self.assertListEqual(["1/2","1/3","1/4","2/3","3/4"], Solution().simplifiedFractions(4))

    def test_simplifiedFractions_3(self):
        self.assertListEqual([], Solution().simplifiedFractions(1))