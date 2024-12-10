from unittest import TestCase
from problems.N2981_Find_Longest_Special_Substring_That_Occurs_Thrice import Solution

class TestSolution(TestCase):
    def test_maximum_length(self):
        self.assertEqual(2, Solution().maximumLength("aaaa"))

    def test_maximum_length_1(self):
        self.assertEqual(-1, Solution().maximumLength("abcdef"))

    def test_maximum_length_2(self):
        self.assertEqual(1, Solution().maximumLength("abcaba"))

    def test_maximum_length_3(self):
        self.assertEqual(1, Solution().maximumLength("eccdnmcnkl"))

    def test_maximum_length_4(self):
        self.assertEqual(-1, Solution().maximumLength("acc"))

    def test_maximum_length_5(self):
        self.assertEqual(11, Solution().maximumLength("ceeeeeeeeeeeebmmmfffeeeeeeeeeeeewww"))

    def test_maximum_length_6(self):
        self.assertEqual(3, Solution().maximumLength("dceeddedcedcdcdedcdddeeedddsssdcdcdeeeccdccedeeedd"))

    def test_maximum_length_8(self):
        self.assertEqual(-1, Solution().maximumLength("cbc"))

