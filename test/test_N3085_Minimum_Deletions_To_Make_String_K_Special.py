from unittest import TestCase
from problems.N3085_Minimum_Deletions_To_Make_String_K_Special import Solution

class TestSolution(TestCase):
    def test_minimum_deletions(self):
        self.assertEquals(3, Solution().minimumDeletions(word = "aabcaba", k = 0))

    def test_minimum_deletions_1(self):
        self.assertEquals(2, Solution().minimumDeletions(word = "dabdcbdcdcd", k = 2))

    def test_minimum_deletions_2(self):
        self.assertEquals(1, Solution().minimumDeletions(word = "aaabaaa", k = 2))

    def test_minimum_deletions_3(self):
        self.assertEquals(2, Solution().minimumDeletions(word = "ahahnhahhah", k = 1))
