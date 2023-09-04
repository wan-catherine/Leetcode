from unittest import TestCase
from problems.N2791_Count_Paths_That_Can_Form_A_Palindrome_In_A_Tree import Solution

class TestSolution(TestCase):
    def test_count_palindrome_paths(self):
        self.assertEquals(8, Solution().countPalindromePaths(parent = [-1,0,0,1,1,2], s = "acaabc"))

    def test_count_palindrome_paths_1(self):
        self.assertEquals(10, Solution().countPalindromePaths(parent = [-1,0,0,0,0], s = "aaaaa"))


