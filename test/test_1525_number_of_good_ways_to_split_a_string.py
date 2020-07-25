from unittest import TestCase
from problems.N1525_Number_Of_Good_Ways_To_Split_A_String import Solution

class TestSolution(TestCase):
    def test_numSplits(self):
        self.assertEqual(2, Solution().numSplits("aacaba"))

    def test_numSplits_1(self):
        self.assertEqual(1, Solution().numSplits("abcd"))

    def test_numSplits_2(self):
        self.assertEqual(4, Solution().numSplits("aaaaa"))

    def test_numSplits_3(self):
        self.assertEqual(2, Solution().numSplits("acbadbaada"))