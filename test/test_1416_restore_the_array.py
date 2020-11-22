from unittest import TestCase
from problems.N1416_Restore_The_Array import Solution

class TestSolution(TestCase):
    def test_numberOfArrays(self):
        self.assertEqual(1, Solution().numberOfArrays(s = "1000", k = 10000))

    def test_numberOfArrays_1(self):
        self.assertEqual(0, Solution().numberOfArrays(s = "1000", k = 10))

    def test_numberOfArrays_2(self):
        self.assertEqual(8, Solution().numberOfArrays(s = "1317", k = 2000))

    def test_numberOfArrays_3(self):
        self.assertEqual(1, Solution().numberOfArrays(s = "2020", k = 30))

    def test_numberOfArrays_4(self):
        self.assertEqual(34, Solution().numberOfArrays(s = "1234567890", k = 90))

    def test_numberOfArrays_5(self):
        self.assertEqual(10, Solution().numberOfArrays("8111197616", 16))

    def test_numberOfArrays_6(self):
        self.assertEqual(829496214, Solution().numberOfArrays("48486250454844645287030712560644579294181", 989))
