from unittest import TestCase
from problems.N1139_Largest_1_bordered_Square import Solution

class TestSolution(TestCase):
    def test_largest1BorderedSquare(self):
        self.assertEqual(9, Solution().largest1BorderedSquare([[1,1,1],[1,0,1],[1,1,1]]))

    def test_largest1BorderedSquare_1(self):
        self.assertEqual(1, Solution().largest1BorderedSquare([[1,1,0,0]]))

    def test_largest1BorderedSquare_2(self):
        self.assertEqual(4, Solution().largest1BorderedSquare([[1,1,1],[1,1,0],[1,1,1],[0,1,1],[1,1,1]]))

    def test_largest1BorderedSquare_3(self):
        self.assertEqual(16, Solution().largest1BorderedSquare([[0,1,1,1,1,0],[1,1,0,1,1,0],[1,1,0,1,0,1],[1,1,0,1,1,1],[1,1,0,1,1,1],[1,1,1,1,1,1],[1,0,1,1,1,1],[0,0,1,1,1,1],[1,1,1,1,1,1]]))