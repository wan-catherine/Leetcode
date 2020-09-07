from unittest import TestCase
from problems.N1347_Minimum_Number_Of_Steps_To_Make_Two_Strings_Anagram import Solution

class TestSolution(TestCase):
    def test_minSteps(self):
        self.assertEqual(1, Solution().minSteps(s = "bab", t = "aba"))

    def test_minSteps_1(self):
        self.assertEqual(5, Solution().minSteps(s = "leetcode", t = "practice"))

    def test_minSteps_2(self):
        self.assertEqual(0, Solution().minSteps(s = "anagram", t = "mangaar"))

    def test_minSteps_3(self):
        self.assertEqual(0, Solution().minSteps(s = "xxyyzz", t = "xxyyzz"))

    def test_minSteps_4(self):
        self.assertEqual(4, Solution().minSteps(s = "friend", t = "family"))
