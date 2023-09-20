from unittest import TestCase
from problems.N2745_Construct_The_Longest_New_String import Solution

class TestSolution(TestCase):
    def test_longest_string(self):
        self.assertEquals(12, Solution().longestString(x = 2, y = 5, z = 1))

    def test_longest_string_1(self):
        self.assertEquals(14, Solution().longestString(x = 3, y = 2, z = 2))