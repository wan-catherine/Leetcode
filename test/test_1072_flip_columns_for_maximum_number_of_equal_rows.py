from unittest import TestCase
from problems.N1072_Flip_Columns_For_Maximum_Number_Of_Equal_Rows import Solution

class TestSolution(TestCase):
    def test_maxEqualRowsAfterFlips(self):
        matrix = [[0,1],[1,1]]
        self.assertEqual(1, Solution().maxEqualRowsAfterFlips(matrix))

    def test_maxEqualRowsAfterFlips_1(self):
        matrix = [[0,1],[1,0]]
        self.assertEqual(2, Solution().maxEqualRowsAfterFlips(matrix))

    def test_maxEqualRowsAfterFlips_2(self):
        matrix = [[0,0,0],[0,0,1],[1,1,0]]
        self.assertEqual(2, Solution().maxEqualRowsAfterFlips(matrix))
