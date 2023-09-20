from unittest import TestCase
from problems.N2746_Decremental_String_Concatenation import Solution

class TestSolution(TestCase):
    def test_minimize_concatenated_length(self):
        self.assertEquals(4, Solution().minimizeConcatenatedLength(["aa","ab","bc"]))

    def test_minimize_concatenated_length_1(self):
        self.assertEquals(2, Solution().minimizeConcatenatedLength(["ab","b"]))

    def test_minimize_concatenated_length_2(self):
        self.assertEquals(6, Solution().minimizeConcatenatedLength(["aaa","c","aba"]))

    def test_minimize_concatenated_length_3(self):
        self.assertEquals(7, Solution().minimizeConcatenatedLength(["bbc","cab","b","aa"]))

    def test_minimize_concatenated_length_4(self):
        self.assertEquals(6, Solution().minimizeConcatenatedLength(["aaa","bba","bb"]))
