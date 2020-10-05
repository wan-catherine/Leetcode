from unittest import TestCase
from problems.N1387_Sort_Integers_By_The_Power_Value import Solution

class TestSolution(TestCase):
    def test_getKth(self):
        self.assertEqual(13, Solution().getKth(lo = 12, hi = 15, k = 2))

    def test_getKth_1(self):
        self.assertEqual(1, Solution().getKth(lo = 1, hi = 1, k = 1))

    def test_getKth_2(self):
        self.assertEqual(7, Solution().getKth(lo = 7, hi = 11, k = 4))

    def test_getKth_3(self):
        self.assertEqual(13, Solution().getKth(lo = 10, hi = 20, k = 5))

    def test_getKth_4(self):
        self.assertEqual(570, Solution().getKth(lo = 1, hi = 1000, k = 777))