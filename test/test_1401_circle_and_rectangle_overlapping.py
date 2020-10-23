from unittest import TestCase
from problems.N1401_Circle_And_Rectangle_Overlapping import Solution

class TestSolution(TestCase):
    def test_checkOverlap(self):
        self.assertTrue(Solution().checkOverlap(radius = 1, x_center = 0, y_center = 0, x1 = 1, y1 = -1, x2 = 3, y2 = 1))

    def test_checkOverlap_1(self):
        self.assertTrue(Solution().checkOverlap(radius = 1, x_center = 0, y_center = 0, x1 = -1, y1 = 0, x2 = 0, y2 = 1))

    def test_checkOverlap_2(self):
        self.assertTrue(Solution().checkOverlap(radius = 1, x_center = 1, y_center = 1, x1 = -3, y1 = -3, x2 = 3, y2 = 3))

    def test_checkOverlap_3(self):
        self.assertFalse(Solution().checkOverlap(radius = 1, x_center = 1, y_center = 1, x1 = 1, y1 = -3, x2 = 2, y2 = -1))

    def test_checkOverlap_4(self):
        self.assertTrue(Solution().checkOverlap(radius = 2, x_center = 102, y_center = 50, x1 = 0, y1 = 0, x2 = 100, y2 = 100))