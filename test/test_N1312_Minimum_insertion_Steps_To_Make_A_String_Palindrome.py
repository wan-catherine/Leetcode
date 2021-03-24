from unittest import TestCase
from problems.N1312_Minimum_insertion_Steps_To_Make_A_String_Palindrome import Solution

class TestSolution(TestCase):
    def test_min_insertions(self):
        self.assertEqual(0, Solution().minInsertions("zzazz"))

    def test_min_insertions_1(self):
        self.assertEqual(2, Solution().minInsertions("mbadm"))

    def test_min_insertions_2(self):
        self.assertEqual(5, Solution().minInsertions("leetcode"))

    def test_min_insertions_3(self):
        self.assertEqual(0, Solution().minInsertions("g"))

    def test_min_insertions_4(self):
        self.assertEqual(1, Solution().minInsertions("no"))

