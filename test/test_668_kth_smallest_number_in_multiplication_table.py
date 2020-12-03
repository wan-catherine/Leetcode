from unittest import TestCase
from problems.N668_Kth_Smallest_Number_In_Multiplication_Table import Solution

class TestSolution(TestCase):
    def test_findKthNumber(self):
        self.assertEqual(3, Solution().findKthNumber(m = 3, n = 3, k = 5))

    def test_findKthNumber_1(self):
        self.assertEqual(6, Solution().findKthNumber(m = 2, n = 3, k = 6))
