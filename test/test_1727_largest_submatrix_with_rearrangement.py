from unittest import TestCase
from problems.N1727_Largest_Submatrix_With_Rearrangements import Solution

class TestSolution(TestCase):
    def test_largestSubmatrix(self):
        self.assertEqual(4, Solution().largestSubmatrix([[0,0,1],[1,1,1],[1,0,1]]))

    def test_largestSubmatrix_1(self):
        self.assertEqual(3, Solution().largestSubmatrix([[1,0,1,0,1]]))

    def test_largestSubmatrix_2(self):
        self.assertEqual(2, Solution().largestSubmatrix([[1,1,0],[1,0,1]]))

    def test_largestSubmatrix_3(self):
        self.assertEqual(0, Solution().largestSubmatrix([[0,0],[0,0]]))
