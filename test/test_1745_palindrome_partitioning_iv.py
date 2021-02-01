from unittest import TestCase
from problems.N1745_Palindrome_Partitioning_IV import Solution

class TestSolution(TestCase):
    def test_checkPartitioning(self):
        self.assertTrue(Solution().checkPartitioning("abcbdd"))

    def test_checkPartitioning_1(self):
        self.assertFalse(Solution().checkPartitioning("bcbddxy"))

    def test_checkPartitioning_2(self):
        self.assertTrue(Solution().checkPartitioning("juchzcedhfesefhdeczhcujzzvbmoeombv"))
