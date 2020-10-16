from unittest import TestCase
from problems.N223_Rectangle_Area import Solution

class TestSolution(TestCase):
    def test_computeArea(self):
        self.assertEqual(45, Solution().computeArea(A = -3, B = 0, C = 3, D = 4, E = 0, F = -1, G = 9, H = 2))

    def test_computeArea_1(self):
        self.assertEqual(17, Solution().computeArea(-2,-2,2,2,3,3,4,4))

    def test_computeArea_2(self):
        self.assertEqual(19, Solution().computeArea(-2,-2,2,2,1,-3,3,-1))
