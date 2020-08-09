from unittest import TestCase
from problems.N1542_Find_Longest_Awesome_Substring import Solution

class TestSolution(TestCase):
    def test_longestAwesome(self):
        self.assertEqual(5, Solution().longestAwesome("3242415"))

    def test_longestAwesome_1(self):
        self.assertEqual(1, Solution().longestAwesome("12345678"))

    def test_longestAwesome_2(self):
        self.assertEqual(6, Solution().longestAwesome("213123"))

    def test_longestAwesome_3(self):
        self.assertEqual(2, Solution().longestAwesome("00"))
