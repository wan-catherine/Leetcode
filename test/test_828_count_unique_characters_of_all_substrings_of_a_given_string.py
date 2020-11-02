from unittest import TestCase
from problems.N828_Count_Unique_Characters_Of_All_Substrings_Of_A_Given_String import Solution

class TestSolution(TestCase):
    def test_uniqueLetterString(self):
        self.assertEqual(10, Solution().uniqueLetterString("ABC"))

    def test_uniqueLetterString_1(self):
        self.assertEqual(8, Solution().uniqueLetterString("ABA"))

    def test_uniqueLetterString_2(self):
        self.assertEqual(92, Solution().uniqueLetterString("LEETCODE"))
