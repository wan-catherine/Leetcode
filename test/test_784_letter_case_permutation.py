from unittest import TestCase
from problems.N784_Letter_Case_Permutation import Solution

class TestSolution(TestCase):
    def test_letterCasePermutation(self):
        self.assertListEqual(["a1b2","a1B2","A1b2","A1B2"], Solution().letterCasePermutation("a1b2"))

    def test_letterCasePermutation_1(self):
        self.assertListEqual(["3z4","3Z4"], Solution().letterCasePermutation("3z4"))

    def test_letterCasePermutation_2(self):
        self.assertListEqual(["12345"], Solution().letterCasePermutation("12345"))

    def test_letterCasePermutation_3(self):
        self.assertListEqual(["0"], Solution().letterCasePermutation("0"))
