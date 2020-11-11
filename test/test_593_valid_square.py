from unittest import TestCase
from problems.N593_Valid_Square import Solution

class TestSolution(TestCase):
    def test_validSquare(self):
        self.assertTrue(Solution().validSquare(p1 = [0,0], p2 = [1,1], p3 = [1,0], p4 = [0,1]))

    def test_validSquare_1(self):
        self.assertFalse(Solution().validSquare(p1 = [0,0], p2 = [0,0], p3 = [0,0], p4 = [0,0]))

    def test_validSquare_2(self):
        self.assertFalse(Solution().validSquare([0,1], [1,2], [0,2], [0,0]))

    def test_validSquare_3(self):
        self.assertFalse(Solution().validSquare([1,1], [0,1], [1,2], [0,0]))