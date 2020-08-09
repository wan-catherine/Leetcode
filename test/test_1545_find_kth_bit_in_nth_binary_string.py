from unittest import TestCase
from problems.N1545_Find_Kth_Bit_In_Nth_Binary_String import Solution

class TestSolution(TestCase):
    def test_findKthBit(self):
        self.assertEqual("0", Solution().findKthBit(n = 3, k = 1))

    def test_findKthBit_1(self):
        self.assertEqual("1", Solution().findKthBit(n = 4, k = 11))

    def test_findKthBit_2(self):
        self.assertEqual("0", Solution().findKthBit(n = 1, k = 1))

    def test_findKthBit_3(self):
        self.assertEqual("1", Solution().findKthBit(n = 2, k = 3))

    def test_findKthBit_4(self):
        self.assertEqual("1", Solution().findKthBit(n = 3, k = 2))
