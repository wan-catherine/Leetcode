from unittest import TestCase
from problems.N1639_Number_Of_Ways_To_Form_A_Target_String_Given_A_Dictionary import Solution

class TestSolution(TestCase):
    def test_numWays(self):
        self.assertEqual(6, Solution().numWays(words = ["acca","bbbb","caca"], target = "aba"))

    def test_numWays_1(self):
        self.assertEqual(4, Solution().numWays(words = ["abba","baab"], target = "bab"))

    def test_numWays_2(self):
        self.assertEqual(1, Solution().numWays(words = ["abcd"], target = "abcd"))

    def test_numWays_3(self):
        self.assertEqual(16, Solution().numWays(words = ["abab","baba","abba","baab"], target = "abba"))
