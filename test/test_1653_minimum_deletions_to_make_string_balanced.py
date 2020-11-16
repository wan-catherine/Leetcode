from unittest import TestCase
from problems.N1653_Minimum_Deletions_To_Make_String_Balanced import Solution

class TestSolution(TestCase):
    def test_minimumDeletions(self):
        self.assertEqual(2, Solution().minimumDeletions("aababbab"))

    def test_minimumDeletions_1(self):
        self.assertEqual(2, Solution().minimumDeletions("bbaaaaabb"))