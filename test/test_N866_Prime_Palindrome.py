from unittest import TestCase
from problems.N866_Prime_Palindrome import Solution

class TestSolution(TestCase):
    def test_prime_palindrome(self):
        self.assertEqual(7, Solution().primePalindrome(6))

    def test_prime_palindrome_1(self):
        self.assertEqual(11, Solution().primePalindrome(8))

    def test_prime_palindrome_2(self):
        self.assertEqual(101, Solution().primePalindrome(13))

    def test_prime_palindrome_3(self):
        self.assertEqual(100030001, Solution().primePalindrome(102))

    def test_prime_palindrome_4(self):
        self.assertEqual(103, Solution().primePalindrome(9989900))
