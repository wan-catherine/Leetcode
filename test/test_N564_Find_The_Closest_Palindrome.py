from unittest import TestCase
from problems.N564_Find_The_Closest_Palindrome import Solution

class TestSolution(TestCase):
    def test_nearest_palindromic(self):
        self.assertEqual("121", Solution().nearestPalindromic("123"))

    def test_nearest_palindromic_1(self):
        self.assertEqual("0", Solution().nearestPalindromic("1"))

    def test_nearest_palindromic_2(self):
        self.assertEqual("1221", Solution().nearestPalindromic("1213"))

    def test_nearest_palindromic_3(self):
        self.assertEqual("77", Solution().nearestPalindromic("88"))
