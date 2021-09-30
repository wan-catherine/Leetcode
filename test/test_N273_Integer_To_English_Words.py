from unittest import TestCase
from problems.N273_Integer_To_English_Words import Solution

class TestSolution(TestCase):
    def test_number_to_words(self):
        self.assertEqual("One Hundred Twenty Three", Solution().numberToWords(123))

    def test_number_to_words_1(self):
        self.assertEqual("Twelve Thousand Three Hundred Forty Five", Solution().numberToWords(12345))

    def test_number_to_words_2(self):
        self.assertEqual("One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven", Solution().numberToWords(1234567))

    def test_number_to_words_3(self):
        self.assertEqual("One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven Thousand Eight Hundred Ninety One", Solution().numberToWords(1234567891))
