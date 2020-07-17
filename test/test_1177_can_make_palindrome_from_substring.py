from unittest import TestCase
from problems.N1177_Can_Make_Palindrome_From_Substring import Solution

class TestSolution(TestCase):
    def test_canMakePaliQueries(self):
        s = "abcda"
        queries = [[3, 3, 0], [1, 2, 0], [0, 3, 1], [0, 3, 2], [0, 4, 1]]
        output = [True,False,False,True,True]
        self.assertListEqual(output, Solution().canMakePaliQueries(s, queries))
