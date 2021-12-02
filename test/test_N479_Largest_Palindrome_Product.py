from unittest import TestCase
from problems.N479_Largest_Palindrome_Product import Solution

class TestSolution(TestCase):
    def test_largest_palindrome(self):
        self.assertEqual(987, Solution().largestPalindrome(2))

    def test_largest_palindrome_1(self):
        self.assertEqual(9, Solution().largestPalindrome(1))
