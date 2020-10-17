from unittest import TestCase
from problems.N187_Repeated_DNA_Sequences import Solution

class TestSolution(TestCase):
    def test_findRepeatedDnaSequences(self):
        s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
        self.assertListEqual(["AAAAACCCCC", "CCCCCAAAAA"], Solution().findRepeatedDnaSequences(s))

    def test_findRepeatedDnaSequences_1(self):
        s = "GAGAGAGAGAGA"
        self.assertListEqual(["GAGAGAGAGA"], Solution().findRepeatedDnaSequences(s))