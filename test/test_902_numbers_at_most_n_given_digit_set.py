from unittest import TestCase
from problems.N902_Numbers_At_Most_N_Given_Digit_Set import Solution

class TestSolution(TestCase):
    def test_atMostNGivenDigitSet(self):
        self.assertEqual(20, Solution().atMostNGivenDigitSet(digits = ["1","3","5","7"], n = 100))

    def test_atMostNGivenDigitSet_1(self):
        self.assertEqual(29523, Solution().atMostNGivenDigitSet(digits = ["1","4","9"], n = 1000000000))

    def test_atMostNGivenDigitSet_2(self):
        self.assertEqual(1, Solution().atMostNGivenDigitSet(digits = ["7"], n = 8))

    def test_atMostNGivenDigitSet_3(self):
        self.assertEqual(18, Solution().atMostNGivenDigitSet(["3","4","5","6"], 64))

    def test_atMostNGivenDigitSet_4(self):
        self.assertEqual(1, Solution().atMostNGivenDigitSet(["1","2","3","4","5","6","7","9"], 1))
