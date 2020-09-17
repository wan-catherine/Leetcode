from unittest import TestCase
from problems.N764_Largest_Plus_Sign import Solution

class TestSolution(TestCase):
    def test_orderOfLargestPlusSign(self):
        self.assertEqual(2, Solution().orderOfLargestPlusSign(N = 5, mines = [[4, 2]]))

    def test_orderOfLargestPlusSign_1(self):
        self.assertEqual(1, Solution().orderOfLargestPlusSign(N = 2, mines = []))

    def test_orderOfLargestPlusSign_2(self):
        self.assertEqual(0, Solution().orderOfLargestPlusSign(N = 1, mines = [[0, 0]]))

    def test_orderOfLargestPlusSign_3(self):
        self.assertEqual(1, Solution().orderOfLargestPlusSign(2, [[0,1],[1,0],[1,1]]))

    def test_orderOfLargestPlusSign_4(self):
        self.assertEqual(1, Solution().orderOfLargestPlusSign(2, [[0,0],[1,1]]))

    def test_orderOfLargestPlusSign_5(self):
        self.assertEqual(2, Solution().orderOfLargestPlusSign(3, [[0,0]]))
