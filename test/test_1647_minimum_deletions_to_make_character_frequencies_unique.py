from unittest import TestCase
from problems.N1647_Minimum_Deletions_To_Make_Character_Frequencies_Unique import Solution

class TestSolution(TestCase):
    def test_minDeletions(self):
        self.assertEqual(0, Solution().minDeletions("aab"))

    def test_minDeletions_1(self):
        self.assertEqual(2, Solution().minDeletions("aaabbbcc"))

    def test_minDeletions_2(self):
        self.assertEqual(2, Solution().minDeletions("ceabaacb"))
