from unittest import TestCase
from problems.N1465_Maximum_Area_Of_A_Piece_Of_Cake_After_Horizontal_And_Vertical_Cuts import Solution

class TestSolution(TestCase):
    def test_maxArea(self):
        h = 5
        w = 4
        horizontalCuts = [1, 2, 4]
        verticalCuts = [1, 3]
        self.assertEqual(4, Solution().maxArea(h, w, horizontalCuts, verticalCuts))

    def test_maxArea_1(self):
        h = 5
        w = 4
        horizontalCuts = [3, 1]
        verticalCuts = [1]
        self.assertEqual(6, Solution().maxArea(h, w, horizontalCuts, verticalCuts))

    def test_maxArea_2(self):
        h = 5
        w = 4
        horizontalCuts = [3]
        verticalCuts = [3]
        self.assertEqual(9, Solution().maxArea(h, w, horizontalCuts, verticalCuts))
