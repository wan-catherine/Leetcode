from unittest import TestCase
from problems.N1067_Digit_Count_In_Range import Solution

class TestSolution(TestCase):
    def test_digits_count(self):
        self.assertEqual(6, Solution().digitsCount(d = 1, low = 1, high = 13))

    def test_digits_count_1(self):
        self.assertEqual(35, Solution().digitsCount(d = 3, low = 100, high = 250))

    def test_digits_count_2(self):
        self.assertEqual(1, Solution().digitsCount(0, 1, 10))

    def test_digits_count_3(self):
        self.assertEqual(223, Solution().digitsCount(0, 625, 1250))

    def test_digits_count_4(self):
        self.assertEqual(339, Solution().digitsCount(0, 1080, 2160))

    def test_digits_count_5(self):
        self.assertEqual(2, Solution().digitsCount(0, 1, 20))

    def test_digits_count_6(self):
        self.assertEqual(1504, Solution().digitsCount(0, 5000, 10000))

    def test_digits_count_7(self):
        self.assertEqual(148888897, Solution().digitsCount(0, 1, 200000000))

