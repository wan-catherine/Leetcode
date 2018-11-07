from unittest import TestCase
from problems.ValidPalindrome import Solution

class TestSolution(TestCase):
    def test_isPalindrome(self):
        solution = Solution()
        res = solution.isPalindrome("A man, a plan, a canal: Panama")
        self.assertEqual(True, res)

    def test_isPalindrome_one(self):
        solution = Solution()
        res = solution.isPalindrome("race a car")
        self.assertEqual(False, res)

    def test_isPalindrome_two(self):
        solution = Solution()
        res = solution.isPalindrome(".,")
        self.assertEqual(True, res)

    def test_isPalindrome_three(self):
        solution = Solution()
        res = solution.isPalindrome("0P")
        self.assertEqual(False, res)