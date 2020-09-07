from unittest import TestCase
from problems.N1358_Number_Of_Substrings_Containing_All_Three_Characters import Solution

class TestSolution(TestCase):
    def test_numberOfSubstrings(self):
        self.assertEqual(10, Solution().numberOfSubstrings("abcabc"))

    def test_numberOfSubstrings_1(self):
        self.assertEqual(3, Solution().numberOfSubstrings("aaacb"))

    def test_numberOfSubstrings_2(self):
        self.assertEqual(1, Solution().numberOfSubstrings("abc"))
