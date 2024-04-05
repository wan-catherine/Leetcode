from unittest import TestCase
from problems.N2193_Minimum_Number_Of_Moves_To_Make_Palindrome import Solution

class TestSolution(TestCase):
    def test_min_moves_to_make_palindrome(self):
        self.assertEqual(2, Solution().minMovesToMakePalindrome("aabb"))

    def test_min_moves_to_make_palindrome_1(self):
        self.assertEqual(2, Solution().minMovesToMakePalindrome("letelt"))
