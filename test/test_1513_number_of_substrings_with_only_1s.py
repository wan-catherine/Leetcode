from unittest import TestCase
from problems.N1513_Number_Of_Substrings_With_Only_1S import Solution

class TestSolution(TestCase):
    def test_numSub(self):
        self.assertEqual(9, Solution().numSub("0110111"))

    def test_numSub_1(self):
        self.assertEqual(2, Solution().numSub("101"))

    def test_numSub_2(self):
        self.assertEqual(21, Solution().numSub("111111"))

    def test_numSub_3(self):
        self.assertEqual(0, Solution().numSub("000"))
