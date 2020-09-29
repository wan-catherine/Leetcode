from unittest import TestCase
from problems.N1124_Longest_Well_Performing_Interval import Solution

class TestSolution(TestCase):
    def test_longestWPI(self):
        self.assertEqual(3, Solution().longestWPI([9,9,6,0,6,6,9]))

    def test_longestWPI_1(self):
        self.assertEqual(1, Solution().longestWPI([6,6,9]))

    def test_longestWPI_2(self):
        self.assertEqual(3, Solution().longestWPI([6,9,9]))

    def test_longestWPI_3(self):
        self.assertEqual(3, Solution().longestWPI([9,6,9]))
