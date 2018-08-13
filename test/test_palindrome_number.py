from unittest import TestCase
from problems.PalindromeNumber import Solution

class TestSolution(TestCase):
    def test_palindrome_with_positive_number(self):
        solution = Solution()
        res = solution.isPalindrome(121)
        self.assertEquals(True, res)

    def test_palindrome_with_negative_number(self):
        solution = Solution()
        res = solution.isPalindrome(-121)
        self.assertEquals(False, res)

    def test_palindrome_with_positive_non_palindrome_number(self):
        solution = Solution()
        res = solution.isPalindrome(10)
        self.assertEquals(False, res)

    def test_palindrome_with_positive_long_non_palindrome_number(self):
        solution = Solution()
        res = solution.isPalindrome(1234564321)
        self.assertEquals(False, res)
