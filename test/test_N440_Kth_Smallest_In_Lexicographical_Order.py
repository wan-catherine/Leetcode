from unittest import TestCase
from problems.N440_Kth_Smallest_In_Lexicographical_Order import Solution

class TestSolution(TestCase):
    def test_find_kth_number(self):
        self.assertEquals(10, Solution().findKthNumber(13, 2))

    def test_find_kth_number_1(self):
        self.assertEquals(1, Solution().findKthNumber(1, 1))

