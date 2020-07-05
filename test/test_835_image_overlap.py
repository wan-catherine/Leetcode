from unittest import TestCase
from problems.N835_Image_Overlap import Solution

class TestSolution(TestCase):
    def test_largestOverlap(self):
        A = [[1, 1, 0],
             [0, 1, 0],
             [0, 1, 0]]
        B = [[0, 0, 0],
             [0, 1, 1],
             [0, 0, 1]]
        self.assertEqual(3, Solution().largestOverlap(A, B))
