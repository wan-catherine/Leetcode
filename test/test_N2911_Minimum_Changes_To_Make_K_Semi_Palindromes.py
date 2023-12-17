from unittest import TestCase
from problems.N2911_Minimum_Changes_To_Make_K_Semi_Palindromes import Solution

class TestSolution(TestCase):
    def test_minimum_changes(self):
        self.assertEquals(1, Solution().minimumChanges(s = "abcac", k = 2))

    def test_minimum_changes_1(self):
        self.assertEquals(2, Solution().minimumChanges(s = "abcdef", k = 2))

    def test_minimum_changes_2(self):
        self.assertEquals(0, Solution().minimumChanges(s = "aabbaa", k = 3))
