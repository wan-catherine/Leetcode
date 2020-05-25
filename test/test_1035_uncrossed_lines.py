from unittest import TestCase
from problems.N1035_Uncrossed_Lines import Solution

class TestSolution(TestCase):
    def test_maxUncrossedLines(self):
        A = [1, 4, 2]
        B = [1, 2, 4]
        self.assertEqual(2, Solution().maxUncrossedLines(A, B))

    def test_maxUncrossedLines_1(self):
        A = [2, 5, 1, 2, 5]
        B = [10, 5, 2, 1, 5, 2]
        self.assertEqual(3, Solution().maxUncrossedLines(A, B))

    def test_maxUncrossedLines_2(self):
        A = [1, 3, 7, 1, 7, 5]
        B = [1, 9, 2, 5, 1]
        self.assertEqual(2, Solution().maxUncrossedLines(A, B))
